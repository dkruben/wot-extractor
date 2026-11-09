# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/sounds/filters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import WWISE as WWISE
from gui.sounds.sound_constants import SoundFilters as SoundFilters
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
_ON_PATTERN = '{}_on'
_OFF_PATTERN = '{}_off'
_filters: dict

class StatesGroup(CONST_CONTAINER):
    HANGAR_FILTERED = 'STATE_hangar_filtered'
    HANGAR_PLACE = 'STATE_hangar_place'
    HANGAR_PLACE_BATTLE_PASS = 'STATE_hangar_place_battle_pass'
    OVERLAY_HANGAR_GENERAL = 'STATE_overlay_hangar_general'
    VIDEO_OVERLAY = 'STATE_video_overlay'
    HANGAR_PLACE_TASKS = 'STATE_hangar_place_tasks'

class States(CONST_CONTAINER):
    OVERLAY_HANGAR_GENERAL_ON: Any
    OVERLAY_HANGAR_GENERAL_OFF: Any
    HANGAR_FILTERED_ON: Any
    HANGAR_FILTERED_OFF: Any
    VIDEO_OVERLAY_ON: Any
    VIDEO_OVERLAY_OFF: Any
    HANGAR_PLACE_GARAGE = 'STATE_hangar_place_garage'
    HANGAR_PLACE_TASKS_DAILY = 'STATE_hangar_place_tasks_daily'
    HANGAR_PLACE_TASKS_MISSIONS = 'STATE_hangar_place_tasks_missions'
    HANGAR_PLACE_TASKS_EVENTS = 'STATE_hangar_place_tasks_events'
    HANGAR_PLACE_TASKS_BATTLE_MATTERS = 'STATE_hangar_place_tasks_battle_matters'

class Events(CONST_CONTAINER):
    BOB_ENTER = 'gui_bb_bloggers_progress_page_ambient_Entrance'
    BOB_EXIT = 'gui_bb_bloggers_progress_page_ambient_Exit'
    MARATHON_ENTER = 'ev_hangar_marathon_enter'
    MARATHON_EXIT = 'ev_hangar_marathon_exit'
    BATTLE_MATTERS_ENTER = 'bm_enter'
    BATTLE_MATTERS_EXIT = 'bm_exit'

class _StateKeeper(object):
    __stateHoldersCounts: dict
    @classmethod
    def checkinHolder(cls, stateName):
        ...
    @classmethod
    def checkoutHolder(cls, stateName):
        ...

class _SoundFilterAbstract(object):
    def start(self):
        ...
    def stop(self):
        ...
    def stopView(self, view):
        ...

class EmptySoundFilter(_SoundFilterAbstract):
    def __repr__(self):
        ...

class _WWISEStateAmbient(_SoundFilterAbstract):
    _stateID: Any
    def __init__(self, stateID):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def _getStartState(self):
        ...
    def _getStopState(self):
        ...
    def __repr__(self):
        ...

class WWISEFilteredHangarFilter(_WWISEStateAmbient):
    def __init__(self):
        ...
    def stopView(self, view):
        ...

class WWISEHangarOverlayFilter(_WWISEStateAmbient):
    def __init__(self):
        ...

class WWISEBattlePassFilter(_WWISEStateAmbient):
    def __init__(self):
        ...

class WWISEHangarTasksFilter(_WWISEStateAmbient):
    def __init__(self):
        ...
    def _getStopState(self):
        ...

class WWISEHangarTasksDailyFilter(WWISEHangarTasksFilter):
    def _getStartState(self):
        ...

class WWISEHangarTasksMissionsFilter(WWISEHangarTasksFilter):
    def _getStartState(self):
        ...

class WWISEMarathonPageFilter(WWISEHangarTasksFilter):
    def start(self):
        ...
    def stop(self):
        ...
    def _getStartState(self):
        ...

class WWISEEventPageFilter(WWISEHangarTasksFilter):
    def _getStartState(self):
        ...

class WWISEBattleMattersFilter(WWISEHangarTasksFilter):
    def _getStartState(self):
        ...

def switchHangarFilteredFilter(on=True):
    ...
def switchHangarOverlaySoundFilter(on=True):
    ...
def switchVideoOverlaySoundFilter(on=True):
    ...
def getEmptyFilter():
    ...
def get(filterID):
    ...
def _selectFilter(wwise):
    ...
def _setState(stateGroup, stateName):
    ...
def _switchOverlaySoundFilter(group, stateOn, stateOff, on=True):
    ...
