# wot-extractor: codigo DESCOMPILADO de sources/res/advent_calendar/scripts/client/advent_calendar/gui/feature/constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: advent_calendar/scripts/client/advent_calendar/gui/feature/constants.py
from __future__ import absolute_import
from enum import Enum
from advent_calendar.gui.impl.gen.view_models.views.lobby.progression_reward_item_view_model import RewardType
ADVENT_CALENDAR_PREFIX = 'advent'
ADVENT_CALENDAR_OPEN_DOOR_TOKEN_PREFIX = ADVENT_CALENDAR_PREFIX + ':open'
ADVENT_CALENDAR_QUEST_POSTFIX = ':open'
ADVENT_CALENDAR_TOKEN = ADVENT_CALENDAR_PREFIX + ':points'
ADVENT_CALENDAR_QUEST_PREFIX = ADVENT_CALENDAR_PREFIX + ':day:'
ADVENT_CALENDAR_QUEST_RE_PATTERN = ADVENT_CALENDAR_QUEST_PREFIX + '\\d+' + ADVENT_CALENDAR_QUEST_POSTFIX
ADVENT_CALENDAR_DAY_TOKEN_PREFIX = ADVENT_CALENDAR_PREFIX + ':day:'
ADVENT_CALENDAR_PROGRESSION_QUEST = ADVENT_CALENDAR_PREFIX + ':progression:'
ADVENT_CALENDAR_PROGRESSION_QUEST_PREFIX = ADVENT_CALENDAR_PROGRESSION_QUEST + '{id}'
PROGRESSION_REWARD_TYPE_TO_ICON = {(RewardType.CREW_MEMBER.value): 'tankwoman', 
   (RewardType.BIG_LOOTBOX.value): 'lootBox'}
MIN_AVAILABLE_DOORS_REQUIRED_FOR_NOTIFICATION = 2
GUARANTEED_REWARD_GROUP_NAME = 'guaranteed'
ADVENT_CALENDAR_DOORS_AVAILABLE_NOTIFICATION_NAME = 'AdventCalendarDoorsAvailable'

class GraphicsPresetSystemSettings(Enum):
    ULTRA = 0
    MAX = 1
    HIGH = 2
    MEDIUM = 3
    LOW = 4


ADVENT_PRESETS_WITH_DISABLED_ANIMATION = (
 GraphicsPresetSystemSettings.LOW.value,)
