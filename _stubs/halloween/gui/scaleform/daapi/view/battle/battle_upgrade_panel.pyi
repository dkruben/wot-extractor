# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/battle_upgrade_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import BigWorld as BigWorld
import BattleReplay as BattleReplay
import CommandMapping as CM
from halloween.gui.scaleform.daapi.view.battle.anomalies_utils import selectAnomaly as selectAnomaly, isAnomalyNew as isAnomalyNew
from halloween.gui.sounds import playSound as playSound
from halloween.gui.sounds.sound_constants import AnomaliesSounds as AnomaliesSounds
from halloween.skeletons.halloween_anomalies_controller import IHalloweenAnomaliesController as IHalloweenAnomaliesController
from shared_utils import first as first
from ReplayEvents import g_replayEvents as g_replayEvents
from frameworks.wulf import WindowLayer as WindowLayer
from helpers import dependency as dependency
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui import InputHandler as InputHandler, makeHtmlString as makeHtmlString
from gui.impl import backport as backport
from gui.impl.gen import R as R
from halloween.gui.scaleform.daapi.view.meta.HWBattleUpgradePanelMeta import HWBattleUpgradePanelMeta as HWBattleUpgradePanelMeta
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control.arena_info.interfaces import IArenaVehiclesController as IArenaVehiclesController
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE
from gui.Scaleform.daapi.view.common.keybord_helpers import getHotKeyList as getHotKeyList, getHotKeysInfo as getHotKeysInfo
from halloween.gui.scaleform.daapi.view.battle.anomalies_utils import isAnomalyInCombo as isAnomalyInCombo, anomalyDescriptionList as anomalyDescriptionList, anomalyTitle as anomalyTitle
from halloween.gui.halloween_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from VehicleRespawnComponent import VehicleRespawnComponent as VehicleRespawnComponent
from typing import Optional as Optional, List as List
from gui.Scaleform.daapi.view.battle.shared import SharedPage as SharedPage
logger: Any
ICONS_PATH = R.images.halloween.gui.maps.icons.anomalies.s_58x58
_KEYS_INFO: list
REASON_EMPTY = -1
_EMPTY_BTN_LABEL = '...'
_EMPTY_BTN_V_KEY = 'NONE'

class _AttentionEffectPlayer(object):
    __slots__: tuple
    _SHOW_DELAY = 60
    __viewRef: Any
    __callbackID: Any
    __delayTime: Any
    __isPlaying: Any
    def __init__(self, viewRef):
        ...
    def setVisible(self, visible):
        ...
    def destroy(self):
        ...
    def __startTimer(self):
        ...
    def __disposeTimer(self):
        ...
    def __stopAnimation(self):
        ...
    def __stopEffect(self):
        ...
    def __onDelayFinished(self):
        ...

class HWBattleUpgradePanel(HWBattleUpgradePanelMeta, IArenaVehiclesController):
    __slots__: tuple
    appLoader: Any
    sessionProvider: Any
    hwAnomaliesCtrl: Any
    TEXT_PATH_PANEL_INFO = R.strings.halloween_battle.upgradePanel
    _IN_COMBAT_DELAY = 1
    _COOLDOWN_DELAY = 5
    _EPIC_ANOMALY_TYPE = 'epic'
    __attentionEffect: Any
    __localVisible: Any
    __textInited: Any
    __callbackDelayer: Any
    __keyInfoList: Any
    __lockReason: Any
    def __init__(self):
        ...
    @property
    def hwBattleGuiCtrl(self):
        ...
    @property
    def upgradeOptions(self):
        ...
    def onSelectItem(self, itemID):
        ...
    def onAppear(self):
        ...
    def onItemHover(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _canBeShown(self):
        ...
    def _onVehicleRespawned(self, vehicle):
        ...
    def __playEffect(self, state):
        ...
    def __onReplayTimeWarpStart(self):
        ...
    def __updateVisibility(self, isVisible):
        ...
    def __onVehicleStateUpdated(self, stateID, _):
        ...
    def __onLockCooldownFinish(self):
        ...
    def __onChangeAnomaliesViewVisibility(self, isVisible):
        ...
    def __onSelectAnomaly(self, anomalyIdx):
        ...
    def __toggleAlertState(self, isLocked, text, reasonID):
        ...
    def __updateUpgrades(self, upgrades):
        ...
    def __onMappingChanged(self, *_):
        ...
    def __getItemInfo(self, index):
        ...
    def __getHotKeyString(self, command):
        ...
    def __getBattlePage(self):
        ...
    def __handleKeyEvent(self, event):
        ...
    def __makeHtmlFormat(self, text, format):
        ...

def _getAnomaliesMatrixHotkey():
    ...
