# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/halloween_account_settings.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from copy import deepcopy as deepcopy
from account_helpers import AccountSettings as AccountSettings
from halloween.gui.halloween_gui_constants import DifficultyLevel as DifficultyLevel, AmmoPanelSwitchPreset as AmmoPanelSwitchPreset
ACCOUNT_DEFAULT_SETTINGS: dict

class AccountSettingsKeys(object):
    EVENT_KEY = 'hw26'
    SELECTED_LEVEL = 'selected_level'
    UNLOCK_LEVELS = 'unlock_levels'
    AWARD_UNLOCK_LEVELS = 'award_unlock_level'
    META_INTRO_VIEW_SHOWED = 'meta_into_view_showed'
    FAVORITES_VEHICLE = 'favorites'
    AMMO_PANEL_PRESET = 'ammo_preset'
    SOUND = 'sound'
    CHAT_FIRST_SEEN = 'chat_first_seen'
    ARTEFACT_VOICEOVER_MUTED = 'artefact_voiceover_muted'
    PROMO_SCREEN_SHOWED = 'promo_screen_showed'
    IS_EVENT_NEW = 'event_is_new'
    IS_BANNER_FIRST_APPEARANCE_SEEN = 'bannerFirstAppearanceSeen'
    BESTIARY_ENEMIES_SEEN = 'bestiaryEnemiesSeen'
    LAST_SELECTED_BESTIARY_ENEMIES = 'lastSelectedBestiaryEnemiesSeen'
    ANOMALIES_SYSTEM_AVAILABLE = 'anomaliesSystemAvailable'
    ANOMALIES_SHOWED = 'anomaliesShowed'

def getSettings(name):
    ...
def setSettings(name, value):
    ...
def isSoundPlayed(name, difficultyLevel):
    ...
def setSoundPlayed(name, difficultyLevel):
    ...
def setAwardUnlockedLevel(level):
    ...
def setNewStatusUnlockLevel(level, status):
    ...
