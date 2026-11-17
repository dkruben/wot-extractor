# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/notification/settings.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import namedtuple as namedtuple
from gui.impl import backport as backport
from gui.impl.gen import R as R
from shared_utils import ScalarTypes as ScalarTypes
log: Any
LIST_SCROLL_STEP_FACTOR = 10
DEF_ICON_NAME = '{0:>s}_1'
DEF_ICON_PATH = '../maps/icons/library/{0:>s}-1.png'
NotificationData: Any
ITEMS_MAX_LENGTHS: dict

class NOTIFICATION_STATE(object):
    POPUPS = 0
    LIST = 1

class NOTIFICATION_TYPE(object):
    UNDEFINED = 0
    MESSAGE = 1
    INVITE = 2
    FRIENDSHIP_RQ = 3
    WGNC_POP_UP = 4
    CLAN_INVITES = 5
    CLAN_APPS = 6
    CLAN_APP_ACTION = 7
    CLAN_INVITE_ACTION = 8
    CLAN_INVITE = 9
    CLAN_APP = 10
    PROGRESSIVE_REWARD = 11
    MISSING_EVENTS = 12
    RECRUIT_REMINDER = 13
    EMAIL_CONFIRMATION_REMINDER = 14
    BATTLE_PASS_SWITCH_CHAPTER_REMINDER = 15
    SENIORITY_AWARDS_TOKENS = 16
    SENIORITY_AWARDS_QUEST = 17
    RESOURCE_WELL_START = 18
    AUCTION_STAGE_START = 19
    AUCTION_STAGE_FINISH = 20
    WINBACK_SELECTABLE_REWARD_AVAILABLE = 21
    BATTLE_MATTERS_TASK_REMINDER = 22
    PRESTIGE_FIRST_ENTRY = 23
    COLLECTIONS_ENTRY = 24
    COLLECTIONS_RENEW = 25
    SENIORITY_AWARDS_VEHICLE_SELECTION = 26
    COMP7_OFFER_TOKENS = 27
    EXCHANGE_RATE_GOLD_DISCOUNT = 28
    EXCHANGE_RATE_XP_DISCOUNT = 29
    ADVENT_CALENDAR_DOORS_AVAILABLE = 30
    VEH_SKILL_TREE_PERK_AVAILABLE = 31
    OPEN_BUNDLE_ENTRY = 32
    CHALLENGES_START = 33
    CHALLENGES_REMINDER = 34
    HO_DOG_REMINDER = 35
    HO_MARKETPLACE_AVAILABLE = 36
    HO_FRIEND_RESOURCE_COLLECTING_AVAILABLE = 37
    HO_RESOURCE_REMINDER = 38
    HO_FRIEND_RESOURCE_REMINDER = 39
    HO_NO_FRIENDS_REMINDER = 40
    RANGE: Any

class NOTIFICATION_BUTTON_STATE(object):
    HIDDEN = 0
    VISIBLE = 1
    ENABLED = 2
    DEFAULT: Any

def makePathToIcon(iconName):
    ...
