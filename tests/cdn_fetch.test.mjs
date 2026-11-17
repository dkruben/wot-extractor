import test from 'node:test';
import assert from 'node:assert/strict';
import http from 'node:http';
import { createCdnFetch } from '../scripts/cdn_fetch.mjs';

test('reassembles exact ranges across chunks and retries a truncated body', async () => {
  const data = new TextEncoder().encode('0123456789abcdef');
  const ranges = [];
  let truncate = true;
  const native = async (url, init) => {
    const range = new Headers(init.headers).get('Range');
    ranges.push(range);
    const [, left, right] = /^bytes=(\d+)-(\d+)$/.exec(range);
    const start = Number(left), end = Number(right);
    let body = data.slice(start, end + 1);
    if (truncate) { body = body.slice(0, -1); truncate = false; }
    return new Response(body, { status: 206, headers: { 'Content-Range': `bytes ${start}-${end}/${data.length}` } });
  };
  const client = createCdnFetch(native, { chunkBytes: 4, attempts: 2, log: () => {} });
  const result = await client.fetch('http://example.test/archive', { headers: { Range: 'bytes=2-12' } });
  assert.equal(new TextDecoder().decode(await result.arrayBuffer()), '23456789abc');
  assert.deepEqual(ranges, ['bytes=2-5', 'bytes=2-5', 'bytes=6-9', 'bytes=10-12']);
  assert.equal(client.metrics.failedRequests, 1);
});

test('rejects a server ignoring ranges instead of downloading the full object', async () => {
  const client = createCdnFetch(async () => new Response('whole object'), { attempts: 2, log: () => {} });
  await assert.rejects(client.fetch('http://example.test/archive', { headers: { Range: 'bytes=0-3' } }), /Invalid range/);
  assert.equal(client.metrics.requests, 2);
  assert.equal(client.metrics.bodyBytes, 0);
});

test('rejects a changed object size between chunks', async () => {
  let calls = 0;
  const client = createCdnFetch(async (url, init) => {
    const [, start, end] = /^bytes=(\d+)-(\d+)$/.exec(new Headers(init.headers).get('Range'));
    return new Response('abcd', { status: 206, headers: { 'Content-Range': `bytes ${start}-${end}/${++calls === 1 ? 8 : 9}` } });
  }, { chunkBytes: 4, attempts: 1, log: () => {} });
  const result = await client.fetch('http://example.test/archive', { headers: { Range: 'bytes=0-7' } });
  await assert.rejects(result.arrayBuffer(), /Invalid range/);
});

test('times out a response that stalls after sending headers and partial data', async () => {
  const server = http.createServer((request, response) => {
    response.writeHead(206, { 'Content-Range': 'bytes 0-3/4', 'Content-Length': '4' });
    response.write('a');
  });
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  try {
    const client = createCdnFetch(fetch, { timeoutMs: 50, attempts: 1, log: () => {} });
    await assert.rejects(client.fetch(`http://127.0.0.1:${server.address().port}/archive`,
      { headers: { Range: 'bytes=0-3' } }), /abort|timeout/i);
    assert.equal(client.metrics.failedRequests, 1);
  } finally {
    server.closeAllConnections();
    await new Promise(resolve => server.close(resolve));
  }
});
