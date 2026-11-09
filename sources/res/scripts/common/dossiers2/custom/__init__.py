# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/dossiers2/custom/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/dossiers2/custom/__init__.py
from __future__ import absolute_import

def init():
    from dossiers2.custom.cache import buildCache
    buildCache()
    from dossiers2.custom.collector20 import loadCollector20Config
    loadCollector20Config()
    from dossiers2.custom.dependencies import init as dependencies_init
    dependencies_init()
