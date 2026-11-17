# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/shared/hw_indicators.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import weakref as weakref
import CommandMapping as CommandMapping
from gui.impl.gen import R as R
from constants import EQUIPMENT_STAGES as EQUIPMENT_STAGES
from gui.impl import backport as backport
from gui.Scaleform.daapi.view.common.keybord_helpers import getHotKeyList as getHotKeyList
from gui.Scaleform.genConsts.MECHANICS_WIDGET_CONST import MECHANICS_WIDGET_CONST as MECHANICS_WIDGET_CONST
from gui.shared.utils.functions import makeTooltip as makeTooltip
from helpers import dependency as dependency
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from halloween.gui.scaleform.daapi.view.meta.NitroIndicatorMeta import NitroIndicatorMeta as NitroIndicatorMeta
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE, CROSSHAIR_VIEW_ID as CROSSHAIR_VIEW_ID
from skeletons.gui.impl import IGuiLoader as IGuiLoader

class HWRocketAcceleratorIndicator(NitroIndicatorMeta):
    sessionProvider: Any
    settingsCore: Any
    NITRO_EQUIPMENT_NAME = 'nitroRamDamage'
    STAGE_TO_INDICATOR_STATE: dict
    TIMER_UPDATE_INTERVAL = 0.1
    __isEnabled: Any
    __item: Any
    __intCD: Any
    __activeEndTime: Any
    _callbackDelayer: Any
    __curState: Any
    def __init__(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    @property
    def _hasTabScreen(self):
        ...
    def _updateTimer(self):
        ...
    def _updateProgress(self, item):
        ...
    def __onVehicleControlling(self, vehicle):
        ...
    def __onVehicleStateUpdated(self, state, value):
        ...
    def __onCrosshairPositionChanged(self, *args):
        ...
    def __onCrosshairViewChanged(self, viewID):
        ...
    def __updateVisibility(self):
        ...
    def __onEquipmentUpdated(self, intCD, item):
        ...
    def __onEquipmentsCleared(self):
        ...
    def __setState(self, state):
        ...
    def __handleNitroPressed(self):
        ...
    def __startTimerUpdate(self):
        ...
    def __stopTimerUpdate(self):
        ...
