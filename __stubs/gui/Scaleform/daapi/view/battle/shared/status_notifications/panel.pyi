# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/status_notifications/panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
from helpers import dependency as dependency
import BattleReplay as BattleReplay
from ReplayEvents import g_replayEvents as g_replayEvents
from gui.Scaleform.daapi.view.battle.shared.status_notifications import components as components
from gui.Scaleform.daapi.view.battle.shared.status_notifications import replay_components as replay_components
from gui.Scaleform.daapi.view.meta.StatusNotificationsPanelMeta import StatusNotificationsPanelMeta as StatusNotificationsPanelMeta
from gui.Scaleform.genConsts.BATTLE_NOTIFICATIONS_TIMER_COLORS import BATTLE_NOTIFICATIONS_TIMER_COLORS as _COLORS
from gui.battle_control import event_dispatcher as gui_event_dispatcher
from gui.battle_control.battle_constants import CROSSHAIR_VIEW_ID as CROSSHAIR_VIEW_ID
from gui.shared.items_parameters import isAutoReloadGun as isAutoReloadGun
from gui.shared.utils.MethodsRules import MethodsRules as MethodsRules
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_logger: Any

class StatusNotificationTimerPanel(StatusNotificationsPanelMeta, MethodsRules):
    _sessionProvider: Any
    _DEFAULT_Y_SHIFT = 114
    _VERTICAL_SHIFT_WITH_AUTOLOADER_IN_SNIPER_MODE: Any
    _viewID: Any
    __container: Any
    __vehicleID: Any
    def __init__(self):
        ...
    def _populate(self):
        ...
    def _addListeners(self):
        ...
    def _removeListeners(self):
        ...
    def _dispose(self):
        ...
    def _getComponentClass(self):
        ...
    def _generateItems(self):
        ...
    def _generateNotificationTimerSettings(self):
        ...
    def _calcVerticalOffset(self, vehicle):
        ...
    def _addNotificationTimerSetting(self, data, typeId, iconName, linkage, color=..., noiseVisible=False, text='', countdownVisible=True, iconOffsetY=0, iconSmallName='', isReversedTimerDirection=False, canBlink=False, descriptionFontSize=14, descriptionOffsetY=0):
        ...
    def _updatePanelPosition(self):
        ...
    def __onTimeWarpFinish(self):
        ...
    def __onReplayPaused(self, isPaused):
        ...
    def __onCollectionUpdated(self, vOs):
        ...
    # decorador original: @MethodsRules.delayable(...)
    def _onVehicleControlling(self, vehicle):
        ...
    # decorador original: @MethodsRules.delayable(...)
    def __onCrosshairViewChanged(self, viewID):
        ...
    def __setVerticalOffset(self, verticalOffset):
        ...
    @classmethod
    def __logDataCollection(cls, vOs):
        ...
