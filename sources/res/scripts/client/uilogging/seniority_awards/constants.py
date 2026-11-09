# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/uilogging/seniority_awards/constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/seniority_awards/constants.py
from __future__ import absolute_import
from enum import Enum

class SeniorityAwardsFeatures(str, Enum):
    FEATURE = 'seniority_awards'
    VEHICLE_SELECTION_FEATURE = 'seniority_awards_vehicle_selection'


class SeniorityAwardsLogKeys(str, Enum):
    COINS_NOTIFICATION = 'coins_notification'
    REWARD_NOTIFICATION = 'reward_notification'
    VEHICLE_SELECTION_NOTIFICATION = 'vehicle_selection_notification'
    MULTIPLE_TOKENS_NOTIFICATION_ERROR = 'multiple_tokens_notification_error'
    TIMEOUT_NOTIFICATION_ERROR = 'timeout_notification_error'


class SeniorityAwardsLogSpaces(str, Enum):
    HANGAR = 'hangar'
    NOTIFICATION_CENTER = 'notification_center'


class SeniorityAwardsLogButtons(str, Enum):
    SHOP_BUTTON = 'shop_button'
    CLAIM_BUTTON = 'claim_button'
    SELECT_BUTTON = 'select_button'


class SeniorityAwardsLogActions(str, Enum):
    CLICK = 'click'
    DISPLAYED = 'displayed'
