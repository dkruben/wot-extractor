# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/battle_control/controllers/battle_gui_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import logging as logging
from Event import EventManager as EventManager, Event as Event
from halloween.gui.halloween_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID, FEEDBACK_EVENT_ID as FEEDBACK_EVENT_ID
from halloween.gui.scaleform.daapi.view.battle.buffs_notification_panel import BuffsNotificationSystem as BuffsNotificationSystem
from halloween.gui.scaleform.daapi.view.battle.buffs_panel import findBuffsPanelComponents as findBuffsPanelComponents
from helpers import dependency as dependency, isPlayerAvatar as isPlayerAvatar
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from HWArenaInfoBossHealthBarComponent import getArenaInfoBossHealthBarComponent as getArenaInfoBossHealthBarComponent
from HWArenaPhasesComponent import HWArenaPhasesComponent as HWArenaPhasesComponent
from gui.battle_control.arena_info.interfaces import IArenaVehiclesController as IArenaVehiclesController
from halloween.gui.battle_control.halloween_battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
_logger: Any

class EventBattleGoal(object):
    UNKNOWN = None
    COLLECT_SOULS = 'halloween.collectSouls'
    GET_TO_COLLECTOR = 'halloween.getToCollector'
    SELECT_UPGRADE = 'halloween.delayForUpgradePanel'

class HWBattleGUIController(IArenaVehiclesController):
    guiSessionProvider: Any
    _TIME_TO_END_NOTIFY = 10
    _UPDATE_PERIOD = 0.5
    __eManager: Any
    onApplyBuff: Any
    onUnapplyBuff: Any
    onBuffStateChanged: Any
    onVehicleDetectorChangeDistance: Any
    onBattleGoalChanged: Any
    onBossAuraVictimMarkerIcon: Any
    onVehicleBuffIconAdded: Any
    onVehicleBuffIconRemoved: Any
    onPhaseChanged: Any
    onSoulCollectorProgress: Any
    onHandleEquipmentPressed: Any
    onShowPanelBuffNotification: Any
    onBossHealthActivated: Any
    onBossHealthChanged: Any
    onBossLivesChanged: Any
    onBossMinionsCountChanged: Any
    onBossHPBarVisibilityChanged: Any
    onBossVulnerableChanged: Any
    onSoulsContainerReady: Any
    onVehicleMaxHealthChanged: Any
    onUpgradeOptionsUpdated: Any
    onChangeAnomaliesViewVisibility: Any
    onSelectAnomaly: Any
    onUpdateUsedAnomalies: Any
    onPhaseTimeChangedNotification: Any
    onUpdateVehicleModifiers: Any
    onVehicleModelHidden: Any
    _callbackDelayer: Any
    _currentGoal: Any
    _currentCollector: Any
    _vehiclesInRadius: Any
    _isCollectorFull: Any
    _vehicleMarkerIcons: Any
    _hiddenVehicleIDs: Any
    _ignoreBuffNotification: Any
    _currentUpgradeOptions: Any
    _isAnomaliesViewVisible: Any
    _isPhaseEndNotificationVisible: Any
    def __init__(self):
        ...
    @property
    def currentGoal(self):
        ...
    @property
    def vehicleMarkerIcons(self):
        ...
    @property
    def battleHintsCtrl(self):
        ...
    def getControllerID(self):
        ...
    def startControl(self, battleCtx, arenaVisitor):
        ...
    def stopControl(self):
        ...
    def onSoulsCollectorSpawned(self, collector):
        ...
    def onSoulsCollectorDestroyed(self, collector):
        ...
    @property
    def currentUpgradeOptions(self):
        ...
    @property
    def isAnomaliesViewVisible(self):
        ...
    def setVehicleHidden(self, vehicleID, isHidden):
        ...
    def isVehicleHidden(self, vehicleID):
        ...
    def applyBuff(self, ctx):
        ...
    def unapplyBuff(self, ctx):
        ...
    def buffStateChanged(self, ctx):
        ...
    def addVehicleMarkerIcon(self, vehicleID, iconName, iconPriority):
        ...
    def removeVehicleMarkerIcon(self, vehicleID, iconName, iconPriority):
        ...
    def vehicleDetectorChangeDistance(self, ctx):
        ...
    def getCurrentCollectorSoulsInfo(self):
        ...
    def updateCollector(self, collector):
        ...
    def updateAnomalyViewVisibility(self, isVisible):
        ...
    def updateUpgradesSelector(self, newUpgrades):
        ...
    def initIgnoreBuffNotification(self):
        ...
    def clearIgnoreBuffNotification(self):
        ...
    def notifyPhaseTimeChanged(self, looterID, ownerID, amount):
        ...
    def _onCollectorFull(self):
        ...
    def setVehicleMaxHealth(self, vehicleID, maxHealth):
        ...
    def _onPhaseChanged(self, arenaPhases):
        ...
    def _onPhaseTimeChanged(self, timeLeft, prev, lastPhase):
        ...
    def _onBossVulnerableChanged(self, isBossVulnerable):
        ...
    def _update(self):
        ...
    def _getRelevantGoal(self):
        ...
    def _getAliveAllyVehicles(self):
        ...
    def _showRelevantBattleHint(self, prevGoal, newGoal):
        ...
    def _isPlayerVehicle(self, vehicleID):
        ...
    def __removeAllBCMarkers(self, arenaPhases):
        ...
