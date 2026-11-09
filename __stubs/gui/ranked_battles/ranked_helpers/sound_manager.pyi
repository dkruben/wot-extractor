# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/ranked_battles/ranked_helpers/sound_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import WWISE as WWISE
from sound_gui_manager import CommonSoundSpaceSettings as CommonSoundSpaceSettings
from gui.Scaleform.genConsts.RANKEDBATTLES_ALIASES import RANKEDBATTLES_ALIASES as RANKEDBATTLES_ALIASES
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
RANKED_MAIN_PAGE_SOUND_SPACE: Any
RANKED_OVERLAY_SOUND_SPACE: Any
RANKED_SUBVIEW_SOUND_SPACE: Any
_DIVISION_TO_PROGRESSION_SOUND: dict
_TYPE_TO_AMBIENT: dict

class AmbientType(CONST_CONTAINER):
    NATURE = 1
    HANGAR = 2

class Sounds(CONST_CONTAINER):
    FIRST_SELECT_EVENT = 'gui_rb_rank_Entrance_first'
    SELECT_EVENT = 'gui_rb_rank_Entrance'
    DESELECT_EVENT = 'gui_rb_rank_Exit'
    OVERLAY_SPACE_NAME = 'ranked_overlay'
    OVERLAY_HANGAR_GENERAL = 'STATE_overlay_hangar_general'
    OVERLAY_HANGAR_GENERAL_ON = 'STATE_overlay_hangar_general_on'
    OVERLAY_HANGAR_GENERAL_OFF = 'STATE_overlay_hangar_general_off'
    SUBVIEW_SPACE_NAME = 'ranked_subview'
    SUBVIEW_HANGAR_GENERAL = 'STATE_subview_hangar_general'
    SUBVIEW_HANGAR_GENERAL_ON = 'STATE_subview_hangar_general_on'
    SUBVIEW_HANGAR_GENERAL_OFF = 'STATE_subview_hangar_general_off'
    OVERLAY_HANGAR_FILTERED = 'STATE_hangar_filtered'
    OVERLAY_HANGAR_FILTERED_ON = 'STATE_hangar_filtered_on'
    OVERLAY_HANGAR_FILTERED_OFF = 'STATE_hangar_filtered_off'
    SUBVIEW_HANGAR_FILTERED = 'STATE_subview_hangar_filtered'
    SUBVIEW_HANGAR_FILTERED_ON = 'STATE_subview_hangar_filtered_on'
    SUBVIEW_HANGAR_FILTERED_OFF = 'STATE_subview_hangar_filtered_off'
    HANGAR_PLACE_STATE = 'STATE_hangar_place'
    HANGAR_PLACE_GARAGE = 'STATE_hangar_place_garage'
    MAIN_PAGE_SPACE_NAME = 'ranked_main_page'
    MAIN_PAGE_STATE = 'STATE_gamemode_progress_page'
    MAIN_PAGE_STATE_ON = 'STATE_gamemode_progress_page_on'
    MAIN_PAGE_STATE_OFF = 'STATE_gamemode_progress_page_off'
    MAIN_PAGE_AMBIENT_ON_EVENT = 'gui_rb_rank_progress_page_ambient_Entrance'
    MAIN_PAGE_AMBIENT_OFF_EVENT = 'gui_rb_rank_progress_page_ambient_Exit'
    MAIN_PAGE_AMBIENT_STATE = 'STATE_rank_ambient'
    MAIN_PAGE_AMBIENT_STATE_1 = 'STATE_rank_ambient_01'
    MAIN_PAGE_AMBIENT_STATE_2 = 'STATE_rank_ambient_02'
    PROGRESSION_STATE = 'STATE_rank_level'
    PROGRESSION_STATE_DEFAULT = 'STATE_rank_level_00'
    PROGRESSION_STATE_QUALIFICATION = 'STATE_rank_level_01'
    PROGRESSION_STATE_3_DIVISION = 'STATE_rank_level_02'
    PROGRESSION_STATE_2_DIVISION = 'STATE_rank_level_03'
    PROGRESSION_STATE_1_DIVISION = 'STATE_rank_level_04'
    PROGRESSION_STATE_LEAGUES = 'STATE_rank_level_05'
    PROGRESSION_STATE_SHOP = 'STATE_rank_level_05'

class RankedSoundManager(object):
    __slots__: tuple
    __isFirstEntrance: Any
    def __init__(self):
        ...
    def clear(self):
        ...
    def onSoundModeChanged(self, isRankedSoundMode, initialProgressionState=None):
        ...
    def setCustomProgressSound(self, state):
        ...
    def setDefaultProgressSound(self):
        ...
    def setProgressSound(self, divisionUserID=None, isLoud=True):
        ...
    def setAmbient(self, ambientType=...):
        ...
    def setOverlayStateOn(self):
        ...
    def setOverlayStateOff(self):
        ...
