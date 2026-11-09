# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/epic_missions_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from builtins import range as range
from collections import defaultdict as defaultdict
from collections import namedtuple as namedtuple
import BigWorld as BigWorld
from future.utils import viewitems as viewitems, viewvalues as viewvalues
import BattleReplay as BattleReplay
import Event as Event
from ReplayEvents import g_replayEvents as g_replayEvents
from constants import SECTOR_STATE as SECTOR_STATE, PLAYER_RANK as PLAYER_RANK
from debug_utils import verify as verify, LOG_ERROR as LOG_ERROR, LOG_DEBUG as LOG_DEBUG
from epic_constants import EPIC_BATTLE_TEAM_ID as EPIC_BATTLE_TEAM_ID
from frontline_common.frontline_constants import FLBattleReservesModifier as FLBattleReservesModifier
from gui import makeHtmlString as makeHtmlString
from gui.Scaleform.genConsts.EPIC_CONSTS import EPIC_CONSTS as EPIC_CONSTS
from gui.Scaleform.genConsts.GAME_MESSAGES_CONSTS import GAME_MESSAGES_CONSTS as GAME_MESSAGES_CONSTS
from gui.Scaleform.locale.EPIC_BATTLE import EPIC_BATTLE as EPIC_BATTLE
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.battle_control.controllers.game_messages_ctrl import PlayerMessageData as PlayerMessageData
from gui.battle_control.controllers.game_notification_ctrl import EPIC_NOTIFICATION as EPIC_NOTIFICATION, OVERTIME_DURATION_WARNINGS as OVERTIME_DURATION_WARNINGS
from gui.battle_control.view_components import IViewComponentsController as IViewComponentsController
from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers import dependency as dependency, i18n as i18n
from items.vehicles import getVehicleClassFromVehicleType as getVehicleClassFromVehicleType
from shared_utils import first as first
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController
from SectorBase import SectorBase as SectorBase
TIMER_WARNINGS: list
RANK_TO_TRANSLATION: dict
MSG_ID_TO_DURATION: Any
MSG_ID_TO_PRIORITY: Any
HQ_DAMAGE_DEBOUNCE_PERIOD = 120
CONTESTED_DEBOUNCE_PERIOD = 120
CONTESTED_CAPTURE_POINTS_THRESHOLD = 0.1
MissionTriggerArgs: Any

class PlayerMission(object):
    PlayerMissionData: Any
    missionType: Any
    missionText: Any
    subText: Any
    id: Any
    def __init__(self):
        ...
    def generateData(self):
        ...
    def isEmptyMission(self):
        ...
    def isObjectivesMission(self):
        ...
    def isBaseMission(self):
        ...

class EpicMissionsController(IViewComponentsController):
    __epicController: Any
    EMPTY_SUB_TITLE_TEXT = ''
    __sessionProvider: Any
    __ready: Any
    __ui: Any
    __currentMission: Any
    __activeMissionData: Any
    __numDestructiblesToDestroy: Any
    __currentEndTime: Any
    __currentLane: Any
    __nearestObjective: Any
    __nearestObjectiveDistance: Any
    __objMsgSent: Any
    __overtimeCB: Any
    __overTimeEnd: Any
    __isRegisterEpicMissionPanel: Any
    __missionPanelDelayQueue: Any
    __orderBattleAbilities: Any
    __isLaneContested: Any
    __contestedEndTime: Any
    __lastTimeHQDamaged: Any
    __retreatMissionResults: Any
    __activeMessages: Any
    __eManager: Any
    __capturedBases: Any
    onPlayerMissionUpdated: Any
    onPlayerMissionReset: Any
    onPlayerMissionTimerSet: Any
    onNearestObjectiveChanged: Any
    onObjectiveBattleStarted: Any
    onIngameMessageReady: Any
    _notificationTypeToMissionTriggerArgs: Any
    def __init__(self, setup):
        ...
    def epicMissionPanelDelayQueue(self, value):
        ...
    @staticmethod
    def isVehicleAliveAndStarted():
        ...
    def setViewComponents(self, *components):
        ...
    def clearViewComponents(self):
        ...
    def getControllerID(self):
        ...
    def startControl(self):
        ...
    def getUI(self):
        ...
    def stopControl(self):
        ...
    def getCurrentMission(self):
        ...
    def getNearestObjectiveData(self):
        ...
    def getRankUpdateData(self, newRank):
        ...
    def __isAttacker(self):
        ...
    def __onReady(self):
        ...
    def __onGameNotificationRecieved(self, notificationType, data):
        ...
    def __onBeforeMissionInvalidation(self):
        ...
    def __onSectorBasePointsUpdate(self, baseId, isPlayerTeam, points, capturingStopped, invadersCount, expectedCaptureTime):
        ...
    def __showBaseContestedMessage(self, points, baseId):
        ...
    def __onPlayerPhysicalLaneUpdated(self, laneID):
        ...
    def __invalidateMissionStatus(self, force=False):
        ...
    def __generateMissionFromData(self):
        ...
    def __onWaypointsForPlayerActivated(self, waypointSectorTimeTuple):
        ...
    def __onPlayerSectorGroupChanged(self, *_):
        ...
    def __onSectorTransitionTimeChanged(self, sectorId, oldTime, newTime):
        ...
    def onSectorBaseCaptured(self, baseId, vehiclesUnlocked=False):
        ...
    def __nextObjectiveMessage(self, isAttacker):
        ...
    def __onSectorBaseActiveStateChanged(self, baseId, isActive):
        ...
    def __onDestructibleEntityIsActiveChanged(self, destructibleEntityID, isActive):
        ...
    def __onDestructibleEntityHealthChanged(self, objID, newHealth, maxHealth, attackerID, attackReason, hitFlags):
        ...
    def __updatePositions(self):
        ...
    def __setNearestObjective(self):
        ...
    def __onSpecificTimeReached(self, minutes, seconds):
        ...
    def __onCrewRoleFactorAndRankUpdate(self, newFactor, allyVehID, allyNewRank):
        ...
    def __onPlayerRankUpdated(self, rank, crewRoleFactor=0.0):
        ...
    def __onOvertimeStart(self, endTime):
        ...
    def __onOvertimeOver(self):
        ...
    def __overtimeTick(self):
        ...
    def __makeMessageData(self, msgType, data):
        ...
    def __sendNotification(self, messageType):
        ...
    def __sendIngameMessage(self, msgData):
        ...
    def __isWaitingForNotification(self):
        ...
    def __onReplayTimeWarpStart(self):
        ...
    def __onReplayTimeWarpFinished(self):
        ...
    def __resetMission(self):
        ...
    def __isInRetreatArea(self):
        ...
    def __onEquipmentAdded(self, intCD, item):
        ...
    def __onEquipmentReset(self, oldIntCD, newIntCD, _):
        ...
    def __onEquipmentsCleared(self):
        ...
