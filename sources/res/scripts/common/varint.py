# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/varint.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/varint.py
from __future__ import absolute_import
from py2to3.moves.io import FastBytesIO
from struct_helpers import unpackByte, packByte

def encode_zigzag64(n):
    return n << 1 ^ n >> 63


def decode_zigzag(n):
    return n >> 1 ^ -(n & 1)


def encode(number):
    buf = FastBytesIO()
    while True:
        towrite = number & 127
        number >>= 7
        if number:
            buf.write(packByte(towrite | 128))
        else:
            buf.write(packByte(towrite))
            break

    return buf.getvalue()


def decode_stream(stream):
    shift = 0
    result = 0
    while True:
        i = _read_one(stream)
        result |= (i & 127) << shift
        shift += 7
        if not i & 128:
            return result


def decode_bytes(buf):
    return decode_stream(FastBytesIO(buf))


def _read_one(stream):
    c = stream.read(1)
    if c == '':
        raise EOFError('Unexpected EOF while reading bytes')
    return unpackByte(c)
