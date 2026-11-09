# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/destroy_times_mapping.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import listvalues as listvalues, viewitems as viewitems
import SoundGroups as SoundGroups
from constants import VEHICLE_MISC_STATUS as VEHICLE_MISC_STATUS, DEATH_ZONES as DEATH_ZONES
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.Scaleform.genConsts.BATTLE_NOTIFICATIONS_TIMER_TYPES import BATTLE_NOTIFICATIONS_TIMER_TYPES as BATTLE_NOTIFICATIONS_TIMER_TYPES
_TIMER_STATES = BATTLE_NOTIFICATIONS_TIMER_TYPES

class FrontendMapping(object):
    __slots__: tuple
    __miscStatuses: Any
    __deathZonesCodes: Any
    __deathZonesSounds: Any
    def __init__(self, miscStatuses=None, deathZonesCodes=None, deathZonesSoundIDs=None, deathZonesTexts=None):
        ...
    def clear(self):
        ...
    def getTimerTypeIDByMiscCode(self, code):
        ...
    def getTimerTypeIDByDeathZoneCode(self, code):
        ...
    def getDestroyTimersTypesIDs(self):
        ...
    def getDeathZoneTimersTypesIDs(self):
        ...
    def getSoundByDeathZone(self, code, level):
        ...
    @staticmethod
    def __loadDeathZoneSounds(soundsIDs):
        ...

def getDefaultMiscStatuses():
    ...
def getDefaultDeathZonesCodes():
    ...
def getDefaultDeathZonesTexts():
    ...
def getTimerViewTypeID(level):
    ...
