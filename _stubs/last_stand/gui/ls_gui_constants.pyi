# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/ls_gui_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import IntEnum as IntEnum
from constants_utils import ConstInjector as ConstInjector
from gui.battle_control.controllers.battle_hints.queues import BattleHintQueueParams as BattleHintQueueParams
from gui.prb_control import settings as settings
from gui.Scaleform.daapi.settings import views as views
from last_stand_common.last_stand_constants import DifficultyLevelToken as DifficultyLevelToken, QUEUE_TYPE as QUEUE_TYPE, LS_CHAT_CHANNELS as LS_CHAT_CHANNELS
from gui.battle_control.battle_constants import FEEDBACK_EVENT_ID as _FET, BATTLE_CTRL_ID as _BASE_CTRL_ID
from messenger.m_constants import LAZY_CHANNEL as CHANNEL
QUEUE_TYPE_TO_DIFFICULTY_LEVEL: dict
DIFFICULTY_TOKEN_TO_LEVEL: dict
DIFFICULTY_LEVEL_TO_TOKEN: dict
LS_RENT_VEHICLE_TOOLTIP = 'lsRentVehicle'
LS_CAROUSEL_VEHICLE_TOOLTIP = 'lsCarouselVehicle'
LS_ABILITY_TOOLTIP = 'lsAbility'
LS_MAIN_SHELL = 'lsMainShell'
LS_TOOLTIP_SET: list
LS_INFO_PAGE_KEY = 'infoPageLastStand'
LS_INTRO_VIDEO_KEY = 'lsIntroVideo'
LS_BATTLE_HINTS_QUEUE_ID: Any
LSDailyQuestDecorationMap: dict

class PREBATTLE_ACTION_NAME(settings.PREBATTLE_ACTION_NAME, ConstInjector):
    _const_type: Any
    LAST_STAND = 'last_stand'
    LAST_STAND_SQUAD = 'last_stand_squad'

class FUNCTIONAL_FLAG(settings.FUNCTIONAL_FLAG, ConstInjector):
    LAST_STAND = 17179869184

class SELECTOR_BATTLE_TYPES(settings.SELECTOR_BATTLE_TYPES, ConstInjector):
    _const_type: Any
    LAST_STAND = 'last_stand'

class VIEW_ALIAS(views.VIEW_ALIAS, ConstInjector):
    _const_type: Any
    LAST_STAND_BATTLE_PAGE = 'LastStandBattlePage'
    LS_OVERLAY_WEB_STORE = 'lsOverlayWebStore'
    LS_BATTLE_RESULTS = 'lsBattleResults'

class DifficultyLevel(IntEnum):
    EASY = 1
    MEDIUM = 2
    HARD = 3

class AmmoPanelSwitchPreset(object):
    PRESET_1 = 1
    PRESET_2 = 2
    ALL: list

class FEEDBACK_EVENT_ID(_FET, ConstInjector):
    LS_GAMEPLAY_ACTION = 106
    LS_NO_HIT = 107

class BATTLE_CTRL_ID(_BASE_CTRL_ID, ConstInjector):
    LS_BATTLE_GUI_CTRL = 104
    LS_VOIP_CTRL = 106

class LAZY_CHANNEL(CHANNEL, ConstInjector):
    _const_type: Any
    LAST_STAND_GLOBAL_CHANNEL = LS_CHAT_CHANNELS.LS_CHAT_CHANNEL
    LAST_STAND_GLOBAL_CHANNEL_EASY = LS_CHAT_CHANNELS.LS_CHAT_CHANNEL_EASY
    LAST_STAND_GLOBAL_CHANNEL_MEDIUM = LS_CHAT_CHANNELS.LS_CHAT_CHANNEL_MEDIUM
    LAST_STAND_GLOBAL_CHANNEL_HARD = LS_CHAT_CHANNELS.LS_CHAT_CHANNEL_HARD

class LSDailyQuestsDecorations(object):
    DAMAGE_TO_OBELISK_ICON_KEY = 'ls_obeliskDamage'
