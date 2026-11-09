# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/Crypto/Cipher/Blowfish.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/Crypto/Cipher/Blowfish.py
__revision__ = '$Id$'
from Crypto.Cipher import blockalgo
import _Blowfish

class BlowfishCipher(blockalgo.BlockAlgo):

    def __init__(self, key, *args, **kwargs):
        blockalgo.BlockAlgo.__init__(self, _Blowfish, key, *args, **kwargs)


def new(key, *args, **kwargs):
    return BlowfishCipher(key, *args, **kwargs)


MODE_ECB = 1
MODE_CBC = 2
MODE_CFB = 3
MODE_PGP = 4
MODE_OFB = 5
MODE_CTR = 6
MODE_OPENPGP = 7
MODE_EAX = 9
block_size = 8
key_size = xrange(4, 57)
