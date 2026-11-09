# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/xml/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/xml/__init__.py
__all__ = [
 'dom', 'parsers', 'sax', 'etree']
_MINIMUM_XMLPLUS_VERSION = (0, 8, 4)
try:
    import _xmlplus
except ImportError:
    pass

try:
    v = _xmlplus.version_info
except AttributeError:
    pass

if v >= _MINIMUM_XMLPLUS_VERSION:
    import sys
    _xmlplus.__path__.extend(__path__)
    sys.modules[__name__] = _xmlplus
else:
    del v
