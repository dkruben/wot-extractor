# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/Crypto/Random/Fortuna/SHAd256.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/Crypto/Random/Fortuna/SHAd256.py
__revision__ = '$Id$'
__all__ = ['new', 'digest_size']
import sys
if sys.version_info[0] == 2 and sys.version_info[1] == 1:
    from Crypto.Util.py21compat import *
from Crypto.Util.py3compat import *
from binascii import b2a_hex
from Crypto.Hash.SHA256 import SHA256

class _SHAd256(object):
    digest_size = SHA256.digest_size
    _internal = object()

    def __init__(self, internal_api_check, sha256_hash_obj):
        if internal_api_check is not self._internal:
            raise AssertionError('Do not instantiate this class directly.  Use %s.new()' % (__name__,))
        self._h = sha256_hash_obj

    def copy(self):
        return _SHAd256(SHAd256._internal, self._h.copy())

    def digest(self):
        retval = SHA256.new(self._h.digest()).digest()
        return retval

    def hexdigest(self):
        retval = b2a_hex(self.digest())
        if sys.version_info[0] == 2:
            return retval
        else:
            return retval.decode()

    def update(self, data):
        self._h.update(data)


digest_size = _SHAd256.digest_size

def new(data=None):
    if not data:
        data = b('')
    sha = _SHAd256(_SHAd256._internal, SHA256.new(data))
    sha.new = globals()['new']
    return sha
