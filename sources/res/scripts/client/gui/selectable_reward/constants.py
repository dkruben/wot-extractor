# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/selectable_reward/constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/selectable_reward/constants.py
from enum import Enum
from battle_pass_common import BATTLE_PASS_OFFER_TOKEN_PREFIX
from gui.ranked_battles.constants import YEAR_AWARD_SELECTABLE_OPT_DEVICE_PREFIX
from epic_constants import EPIC_OFFER_TOKEN_PREFIX

class Features(Enum):
    UNDEFINED = 0
    BATTLE_PASS = 1
    RANKED = 2
    EPIC = 3


FEATURE_TO_PREFIX = {(Features.BATTLE_PASS): BATTLE_PASS_OFFER_TOKEN_PREFIX, 
   (Features.RANKED): YEAR_AWARD_SELECTABLE_OPT_DEVICE_PREFIX, 
   (Features.EPIC): EPIC_OFFER_TOKEN_PREFIX}
SELECTABLE_BONUS_NAME = 'selectableBonus'
