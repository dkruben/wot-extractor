# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/epic_constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/epic_constants.py
from __future__ import absolute_import
from constants import IS_CLIENT, OFFER_TOKEN_PREFIX, IS_WEB
from items.components.supply_slot_categories import SlotCategories
EPIC_TOKEN_PREFIX = 'epic:'
EPIC_OFFER_TOKEN_PREFIX = OFFER_TOKEN_PREFIX + EPIC_TOKEN_PREFIX
EPIC_SELECT_BONUS_NAME = 'epicSelectToken'
EPIC_SKILL_TOKEN_NAME = 'abilityToken'
LEVELUP_TOKEN_TEMPLATE = 'epicmetagame:levelup:'
EPIC_OFFER_TYPES = ('brochure', 'battleBooster', 'expequipments')
EPIC_CHOICE_REWARD_OFFER_TOKENS = tuple(EPIC_OFFER_TOKEN_PREFIX + oType + ':' for oType in EPIC_OFFER_TYPES)
EPIC_CHOICE_REWARD_OFFER_GIFT_TOKENS = tuple(EPIC_OFFER_TOKEN_PREFIX + oType + '_gift:' for oType in EPIC_OFFER_TYPES)
EPICS_CHOICE_REWARD_OFFER_TOKEN_FREE_POSTFIX = 'free:'
EPIC_CHOICE_REWARD_OFFER_TOKEN_PAID_POSTFIX = 'paid:'

class EPIC_BATTLE_TEAM_ID(object):
    TEAM_ATTACKER = 1
    TEAM_DEFENDER = 2


FRONTLINE_BONUSES_ORDER = (
 'battlePassPoints',
 EPIC_SKILL_TOKEN_NAME,
 'crystal',
 'epicSelectToken',
 'goodies',
 'crewBooks')
EPIC_BATTLE_LEVEL_IMAGE_INDEX = (
 (0, ),
 (1, 2, 3, 4),
 (5, 6, 7, 8, 9),
 (10, 11, 12, 13, 14),
 (15, 16, 17, 18, 19),
 (20, ))
CATEGORIES_ORDER = [
 SlotCategories.FIRESUPPORT,
 SlotCategories.RECONNAISSANCE,
 SlotCategories.TACTICS]
if IS_CLIENT or IS_WEB:
    from shared_utils import CONST_CONTAINER

    class SECTOR_EDGE_STATE(CONST_CONTAINER):
        NONE = 0
        SAFE = 1
        DANGER = 2
