# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/common/frontline_common/constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/common/frontline_common/constants.py
from __future__ import absolute_import

class AccountSettingsKeys(object):
    EVENT_KEY = 'frontline_keys'
    SKILL_POINTS_SHOWN = 'points_shown'
    WELCOME_SCREEN_VIEWED = 'welcome_screen_viewed'
    RENT_BANNER_CLICKED = 'rent_banner_clicked'
    REWARD_TOKENS_RECEIVED = 'rewardTokensReceived'


class CallbackDataNames(object):
    FL_MODIFIER = 'fl_modifier'


ACCOUNT_DEFAULT_SETTINGS = {(AccountSettingsKeys.EVENT_KEY): {(AccountSettingsKeys.SKILL_POINTS_SHOWN): {}, (AccountSettingsKeys.WELCOME_SCREEN_VIEWED): {}, (AccountSettingsKeys.RENT_BANNER_CLICKED): False, 
                                     (AccountSettingsKeys.REWARD_TOKENS_RECEIVED): []}}
