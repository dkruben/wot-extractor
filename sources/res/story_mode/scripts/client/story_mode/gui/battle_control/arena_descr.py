# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/battle_control/arena_descr.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/battle_control/arena_descr.py
from __future__ import absolute_import
from gui.battle_control.arena_info import settings
from gui.battle_control.arena_info.arena_descrs import ArenaWithLabelDescription

class ArenaDescription(ArenaWithLabelDescription):

    def getScreenIcon(self):
        return settings.DEFAULT_SCREEN_MAP_IMAGE_RES_PATH
