# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/battle/radar.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BattleReplay as BattleReplay
import CommandMapping as CommandMapping
from constants import ARENA_PERIOD as ARENA_PERIOD
from gui.Scaleform.daapi.view.meta.RadarButtonMeta import RadarButtonMeta as RadarButtonMeta
from gui.Scaleform.genConsts.ANIMATION_TYPES import ANIMATION_TYPES as ANIMATION_TYPES
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE
from gui.battle_control.controllers.period_ctrl import IAbstractPeriodView as IAbstractPeriodView
from battle_royale.gui.battle_control.controllers.radar_ctrl import RadarResponseCode as RadarResponseCode, IReplayRadarListener as IReplayRadarListener
from gui.impl import backport as backport
from gui.impl.backport import image as image
from gui.impl.gen import R as R
from gui.shared.tooltips.consumables_panel import TOOLTIP_FORMAT as TOOLTIP_FORMAT
from gui.shared.utils.key_mapping import getScaleformKey as getScaleformKey
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_RADAR_FAILED_MSG = 'radarInCooldown'
_RADAR_IS_READY_TO_USE_MGS = 'RADAR_IS_READY_TO_USE'

class RadarButton(RadarButtonMeta, IReplayRadarListener, IAbstractPeriodView):
    __sessionProvider: Any
    __arenaPeriod: Any
    __isAvailable: Any
    __isVehicleAlive: Any
    __radarIsReady: Any
    def __init__(self):
        ...
    def onClick(self):
        ...
    def setCoolDownTimeSnapshot(self, time):
        ...
    def startTimeOut(self, timeLeft, duration):
        ...
    def radarIsReady(self, isReady):
        ...
    def reset(self):
        ...
    def timeOutDone(self):
        ...
    def radarActivationFailed(self, code):
        ...
    def setPeriod(self, period):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __getCommandStr(self):
        ...
    def __getVehicleStateCtrl(self):
        ...
    def __onVehicleStateUpdated(self, stateID, _):
        ...
    def __updateAvailability(self):
        ...
    def __reset(self):
        ...
