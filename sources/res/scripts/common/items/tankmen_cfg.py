# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/items/tankmen_cfg.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/items/tankmen_cfg.py
from __future__ import absolute_import
from typing import TYPE_CHECKING
from constants import ITEM_DEFS_PATH
from items.readers import skills_readers
from items.readers import tankmen_readers
if TYPE_CHECKING:
    from items.components import tankmen_components
_g_loreConfig = None
_g_autoFillConfig = None

def getLoreConfig():
    global _g_loreConfig
    if _g_loreConfig is None:
        _g_loreConfig = tankmen_readers.readLoreConfig(ITEM_DEFS_PATH + 'tankmen/common/lore.xml')
    return _g_loreConfig


def getAutoFillConfig():
    global _g_autoFillConfig
    if _g_autoFillConfig is None:
        _g_autoFillConfig = skills_readers.readAutoFillConfig(ITEM_DEFS_PATH + 'tankmen/common/autofill.xml')
    return _g_autoFillConfig
