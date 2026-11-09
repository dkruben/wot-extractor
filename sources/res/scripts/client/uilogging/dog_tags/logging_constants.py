# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/uilogging/dog_tags/logging_constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/dog_tags/logging_constants.py
from __future__ import absolute_import
from enum import Enum
FEATURE = 'dog_tags'
MIN_VIEW_TIME = 2

class DogTagActions(Enum):
    CLICK = 'click'
    VIEWED = 'viewed'
    DISPLAY = 'display'


class DogTagsViewKeys(Enum):
    HANGAR = 'hangar'
    DOG_TAG = 'dog_tag_view'
    ACCOUNT_DASHBOARD = 'account_dashboard'
    ANIMATED_DOG_TAG = 'animated_dog_tag'


class DogTagButtons(Enum):
    INFO = 'dog_tag_info_button'


class DogTagKeys(Enum):
    ANIMATION_TOOLTIP = 'animated_dog_tag_tooltip'
    ACHIEVEMENT_CARD = 'achievement_card'


class DogTagAchievementStates(Enum):
    IN_PROGRESS = 'in_progress'
    NO_PROGRESS = 'no_progress'
    COMPLETED = 'completed'
