# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/uilogging/clan_supply/constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/clan_supply/constants.py
from __future__ import absolute_import
from enum import Enum
FEATURE = 'clan_supply'

class ClanSupplyLogAction(Enum):
    CLOSE = 'close'
    OPEN = 'open'


class ClanSupplyLogKeys(Enum):
    QUESTS_SCREEN = 'tour_task_screen_window'
    PROGRESSION_SCREEN = 'map_screen_window'
    CLAN_LANDING = 'clan_landing'
    NOTIFICATION = 'notification'
    HANGAR_HEADER = 'hangar_header'
    BACK_BUTTON = 'back_button'
    SIDEBAR_PROGRESSION = 'sidebar_map'
    SIDEBAR_QUEST = 'sidebar_quest'
