# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/Crypto/Util/Padding.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/Crypto/Util/Padding.py
__all__ = [
 'ValueError', 'pad', 'unpad']
from Crypto.Util.py3compat import *

def pad(data_to_pad, block_size, style='pkcs7'):
    padding_len = block_size - len(data_to_pad) % block_size
    if style == 'pkcs7':
        padding = bchr(padding_len) * padding_len
    elif style == 'x923':
        padding = bchr(0) * (padding_len - 1) + bchr(padding_len)
    elif style == 'iso7816':
        padding = bchr(128) + bchr(0) * (padding_len - 1)
    else:
        raise ValueError('Unknown padding style')
    return data_to_pad + padding


def unpad(padded_data, block_size, style='pkcs7'):
    pdata_len = len(padded_data)
    if pdata_len % block_size:
        raise ValueError('Input data is not padded')
    if style in ('pkcs7', 'x923'):
        padding_len = bord(padded_data[-1])
        if padding_len < 1 or padding_len > min(block_size, pdata_len):
            raise ValueError('Padding is incorrect.')
        if style == 'pkcs7':
            if padded_data[-padding_len:] != bchr(padding_len) * padding_len:
                raise ValueError('PKCS#7 padding is incorrect.')
        elif padded_data[-padding_len:-1] != bchr(0) * (padding_len - 1):
            raise ValueError('ANSI X.923 padding is incorrect.')
    elif style == 'iso7816':
        padding_len = pdata_len - padded_data.rfind(bchr(128))
        if padding_len < 1 or padding_len > min(block_size, pdata_len):
            raise ValueError('Padding is incorrect.')
        if padding_len > 1 and padded_data[1 - padding_len:] != bchr(0) * (padding_len - 1):
            raise ValueError('ISO 7816-4 padding is incorrect.')
    else:
        raise ValueError('Unknown padding style')
    return padded_data[:-padding_len]
