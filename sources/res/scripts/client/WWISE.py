# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/WWISE.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/WWISE.py
from __future__ import absolute_import, print_function
enabled = True
try:
    from _WWISE import *
    import _WWISE
except ImportError:
    print('WARNING: WWISE support is not enabled.')
    enabled = False
