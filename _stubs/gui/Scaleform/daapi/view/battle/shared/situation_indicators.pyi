# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/situation_indicators.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
import BigWorld as BigWorld
import WWISE as WWISE
from gui.Scaleform.daapi.view.meta.SituationIndicatorsMeta import SituationIndicatorsMeta as SituationIndicatorsMeta
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE, VEHICLE_VIEW_STATE_ID_TO_WEATHER_ZONE_NAME as VEHICLE_VIEW_STATE_ID_TO_WEATHER_ZONE_NAME
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.utils.functions import makeTooltip as makeTooltip
from helpers import dependency as dependency
from items import tankmen as tankmen
from items.components.perks_constants import PerkState as PerkState
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from ReplayEvents import g_replayEvents as g_replayEvents

class PerksSounds(CONST_CONTAINER):
    PERK = 'detachment_perk'
    PERK_STOP = 'detachment_perk_stop'

class WeatherState(object):
    INACTIVE = 0
    ACTIVE = 1

class SituationIndicators(SituationIndicatorsMeta):
    sessionProvider: Any
    def setPerks(self, perks):
        ...
    def updatePerks(self, changedPerks, prevPerks):
        ...
    def clearHUD(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _destroy(self):
        ...
    def _getLifeTime(self, perkData):
        ...
    def __onVehicleStateUpdated(self, state, value):
        ...
    def __onVehicleControlling(self, _):
        ...
    def _onReplayPaused(self, isPaused):
        ...

def _getTooltip(weatherName):
    ...
