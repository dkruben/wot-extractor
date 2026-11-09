# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/Crypto/pct_warnings.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/Crypto/pct_warnings.py


class CryptoWarning(Warning):
    pass


class CryptoDeprecationWarning(DeprecationWarning, CryptoWarning):
    pass


class CryptoRuntimeWarning(RuntimeWarning, CryptoWarning):
    pass


class RandomPool_DeprecationWarning(CryptoDeprecationWarning):
    pass


class ClockRewindWarning(CryptoRuntimeWarning):
    pass


class GetRandomNumber_DeprecationWarning(CryptoDeprecationWarning):
    pass


class DisableShortcut_DeprecationWarning(CryptoDeprecationWarning):
    pass


class PowmInsecureWarning(CryptoRuntimeWarning):
    pass


import warnings as _warnings
_warnings.filterwarnings('always', category=ClockRewindWarning, append=1)
