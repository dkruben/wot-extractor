# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/gui/hangar_presets/fort_rush_presets_reader.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/gui/hangar_presets/fort_rush_presets_reader.py
from __future__ import absolute_import
from gui.hangar_presets.obsolete.hangar_presets_reader import DefaultPresetReader

class FortRushPresetsReader(DefaultPresetReader):
    _CONFIG_PATH = 'fort_rush/gui/configs/fort_rush_hangar_gui_presets.xml'

    @staticmethod
    def isDefault():
        return False
