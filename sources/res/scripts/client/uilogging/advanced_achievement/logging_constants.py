# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/uilogging/advanced_achievement/logging_constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/advanced_achievement/logging_constants.py
from __future__ import absolute_import
from enum import Enum
FEATURE = 'advanced_achievement'

class AdvancedAchievementActions(Enum):
    CLICK = 'click'
    DISPLAY = 'display'


class AdvancedAchievementViewKey(Enum):
    HANGAR = 'hangar'
    NOTIFICATION_CENTER = 'notification_center'
    PLAYER_COLLECTION = 'player_collection'
    CATALOG = 'catalog'
    REWARD_SCREEN = 'reward_screen'
    EARNING = 'earning_notification_view'


class AdvancedAchievementButtons(Enum):
    TO_ACHIEVEMENT = 'go_to_achievement_button'
    TO_RECEIVED = 'go_to_received_button'
    MORE_REWARDS = 'more_rewards_button'
    GOBLET = 'goblet_button'
    DOG_TAG_PREVIEW = 'dog_tag_preview_button'
    CATALOG = 'catalog_button'


class AdvancedAchievementKeys(Enum):
    SUBCATEGORY = 'subcategory'
    UPCOMING = 'upcoming_achievement'
    EARNING_NOTIFICATION = 'earning_notification'
    ACHIEVEMENT_CARD = 'achievement_card'
    ANOTHER_PLAYER = 'another_player_click'


class AdvancedAchievementSubcategory(Enum):
    VEHICLE = 'vehicle'
    NATIONS = 'nations'
    CUSTOMIZATION = 'customization'
    TROPHY = 'trophy'


class AdvancedAchievementInfoKeys(Enum):
    MULTIPLE = 'multiple'
    SINGLE = 'single'
    PLAYER = 'player'
    ANOTHER_PLAYER = 'another_player'


class AdvancedAchievementStates(Enum):
    IN_PROGRESS = 'in_progress'
    NO_PROGRESS = 'no_progress'
    COMPLETED = 'completed'
