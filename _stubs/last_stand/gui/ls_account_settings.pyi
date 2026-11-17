# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/ls_account_settings.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from copy import deepcopy as deepcopy
from future.utils import viewitems as viewitems
from account_helpers import AccountSettings as AccountSettings
from constants import Configs as Configs
from last_stand.gui.ls_gui_constants import DifficultyLevel as DifficultyLevel, AmmoPanelSwitchPreset as AmmoPanelSwitchPreset
from realm import CURRENT_REALM as CURRENT_REALM
ACCOUNT_DEFAULT_SETTINGS: dict

class AccountSettingsKeys(object):
    EVENT_KEY: Any
    PERSISTENT_EVENT_KEY: Any
    SELECTED_LEVEL = 'selected_level'
    UNLOCK_LEVELS = 'unlock_levels'
    AWARD_UNLOCK_LEVELS = 'award_unlock_level'
    META_INTRO_VIEW_SHOWED = 'meta_into_view_showed'
    FAVORITES_VEHICLE = 'favorites'
    AMMO_PANEL_PRESET = 'ammo_preset'
    SOUND = 'sound'
    CHAT_FIRST_SEEN = 'chat_first_seen'
    STORY_POINT_VOICEOVER_MUTED = 'story_point_voiceover_muted'
    PROMO_SCREEN_SHOWED = 'promo_screen_showed'
    CAROUSEL_FILTER_DEF = 'carousel_filter_def'
    IS_EVENT_NEW = 'ls_event_is_new'
    IS_BANNER_FIRST_APPEARANCE_SEEN = 'bannerFirstAppearanceSeen'
    IS_VOIP_IN_BATTLE_ACTIVATED = 'isVOIPInBattleActivated'

def getSettings(name, section=...):
    ...
def setSettings(name, value, section=...):
    ...
def isSoundPlayed(name, difficultyLevel):
    ...
def setSoundPlayed(name, difficultyLevel):
    ...
def setAwardUnlockedLevel(level):
    ...
def setNewStatusUnlockLevel(level, status):
    ...
def getFirstNewStatusUnlockLevel():
    ...
def clearNewStatusUnlockLevel(level):
    ...
def setChatFirstSeen(key, value):
    ...
