// Bounded range downloads for the separately checked-out CDN engine.
import fs from 'node:fs';
import path from 'node:path';

export function createCdnFetch(nativeFetch, options = {}) {
  const chunkBytes = options.chunkBytes ?? 32 * 1024 * 1024;
  const timeoutMs = options.timeoutMs ?? 45000;
  const attempts = options.attempts ?? 3;
  const log = options.log ?? console.log;
  const metrics = { requests: 0, bodyBytes: 0, rangeRequests: 0, failedRequests: 0 };
  let nextProgress = 256 * 1024 * 1024;

  async function readBody(response) {
    const reader = response.body.getReader();
    const chunks = [];
    let length = 0;
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      chunks.push(value);
      length += value.byteLength;
      metrics.bodyBytes += value.byteLength;
      if (metrics.bodyBytes >= nextProgress) {
        log(`[cdn-fetch] received ${(metrics.bodyBytes / 1048576).toFixed(0)} MiB`);
        nextProgress = metrics.bodyBytes + 256 * 1024 * 1024;
      }
    }
    const result = new Uint8Array(length);
    let offset = 0;
    for (const chunk of chunks) { result.set(chunk, offset); offset += chunk.byteLength; }
    return result;
  }

  async function part(url, init, start, end, expectedTotal) {
    let last;
    for (let attempt = 0; attempt < attempts; attempt++) {
      const target = new URL(url);
      // Some regional CDN edges behave differently over HTTPS. Retry the same
      // immutable versioned object there; never invent another CDN hostname.
      if (target.protocol === 'http:' && attempt % 2 === 1) target.protocol = 'https:';
      const headers = new Headers(init.headers);
      headers.set('Range', `bytes=${start}-${end}`);
      metrics.requests++;
      metrics.rangeRequests++;
      let response;
      try {
        const timeout = AbortSignal.timeout(timeoutMs);
        const signal = init.signal ? AbortSignal.any([init.signal, timeout]) : timeout;
        response = await nativeFetch(target, { ...init, headers, signal });
        const match = /^bytes (\d+)-(\d+)\/(\d+)$/.exec(response.headers.get('Content-Range') ?? '');
        if (response.status !== 206 || !match || Number(match[1]) !== start || Number(match[2]) !== end ||
            Number(match[3]) <= end || (expectedTotal !== undefined && Number(match[3]) !== expectedTotal)) {
          await response.body?.cancel();
          throw new Error(`Invalid range response: ${response.status} ${response.headers.get('Content-Range')}`);
        }
        const bytes = await readBody(response);
        if (bytes.byteLength !== end - start + 1) throw new Error('Truncated range body');
        return { bytes, total: Number(match[3]) };
      } catch (error) {
        metrics.failedRequests++;
        last = error;
        log(`[cdn-fetch] attempt ${attempt + 1}/${attempts} failed: ${target.host} bytes=${start}-${end}: ${error.message}`);
        if (init.signal?.aborted) throw error;
      }
    }
    throw last;
  }

  async function wrapped(input, supplied = {}) {
    const url = input instanceof Request ? input.url : String(input);
    const init = { ...supplied, headers: new Headers(supplied.headers ?? (input instanceof Request ? input.headers : undefined)) };
    const range = init.headers.get('Range');
    if (!range) {
      metrics.requests++;
      const timeout = AbortSignal.timeout(timeoutMs);
      const signal = init.signal ? AbortSignal.any([init.signal, timeout]) : timeout;
      const response = await nativeFetch(input, { ...init, signal });
      const bytes = await readBody(response);
      return new Response(bytes, { status: response.status, statusText: response.statusText, headers: response.headers });
    }
    const match = /^bytes=(\d+)-(\d+)$/.exec(range);
    if (!match) throw new Error(`Unsupported range: ${range}`);
    const start = Number(match[1]), end = Number(match[2]);
    if (!Number.isSafeInteger(start) || !Number.isSafeInteger(end) || end < start) throw new Error('Invalid range bounds');
    const firstEnd = Math.min(end, start + chunkBytes - 1);
    const first = await part(url, init, start, firstEnd);
    let firstBytes = first.bytes;
    let cursor = firstEnd + 1;
    const stream = new ReadableStream({
      async pull(controller) {
        if (firstBytes) { controller.enqueue(firstBytes); firstBytes = null; return; }
        if (cursor > end) { controller.close(); return; }
        try {
          const last = Math.min(end, cursor + chunkBytes - 1);
          const result = await part(url, init, cursor, last, first.total);
          cursor = last + 1;
          controller.enqueue(result.bytes);
        } catch (error) { controller.error(error); }
      },
    });
    return new Response(stream, { status: 206, headers: {
      'Content-Range': `bytes ${start}-${end}/${first.total}`,
      'Content-Length': String(end - start + 1),
    } });
  }
  return { fetch: wrapped, metrics };
}

export function installCdnFetch(options) {
  const result = createCdnFetch(globalThis.fetch.bind(globalThis), options);
  globalThis.fetch = result.fetch;
  return result.metrics;
}

if (process.env.WG_CDN_FETCH_AUTO === '1') {
  const metrics = installCdnFetch();
  process.on('exit', () => {
    if (!metrics.requests || !process.env.WG_CDN_METRICS_PATH) return;
    fs.mkdirSync(path.dirname(process.env.WG_CDN_METRICS_PATH), { recursive: true });
    fs.writeFileSync(process.env.WG_CDN_METRICS_PATH, JSON.stringify(metrics, null, 2));
  });
}
