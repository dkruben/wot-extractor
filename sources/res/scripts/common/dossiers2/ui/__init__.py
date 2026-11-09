# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/dossiers2/ui/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/dossiers2/ui/__init__.py
from __future__ import absolute_import
from dossiers2.ui.layouts import init as ui_layouts_init
from dossiers2.ui.achievements import init as achieves_init

def init():
    achieves_init('scripts/item_defs/achievements.xml')
    ui_layouts_init()
