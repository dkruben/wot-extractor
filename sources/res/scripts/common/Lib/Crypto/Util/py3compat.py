# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/Crypto/Util/py3compat.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/Crypto/Util/py3compat.py
__revision__ = '$Id$'
import sys
if sys.version_info[0] == 2:
    from types import UnicodeType as _UnicodeType

    def b(s):
        return s


    def bchr(s):
        return chr(s)


    def bstr(s):
        return str(s)


    def bord(s):
        return ord(s)


    def tobytes(s):
        if isinstance(s, _UnicodeType):
            return s.encode('latin-1')
        else:
            return ('').join(s)


    def tostr(bs):
        return unicode(bs, 'latin-1')


    from StringIO import StringIO as BytesIO
else:

    def b(s):
        return s.encode('latin-1')


    def bchr(s):
        return bytes([s])


    def bstr(s):
        if isinstance(s, str):
            return bytes(s, 'latin-1')
        else:
            return bytes(s)


    def bord(s):
        return s


    def tobytes(s):
        if isinstance(s, bytes):
            return s
        else:
            if isinstance(s, str):
                return s.encode('latin-1')
            return bytes(s)


    def tostr(bs):
        return bs.decode('latin-1')


    from io import BytesIO
