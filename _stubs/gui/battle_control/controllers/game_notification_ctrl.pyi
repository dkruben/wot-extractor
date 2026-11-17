# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/game_notification_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import defaultdict as defaultdict
import BigWorld as BigWorld
import Event as Event
import SoundGroups as SoundGroups
import TriggersManager as TriggersManager
from debug_utils import LOG_DEBUG as LOG_DEBUG, LOG_ERROR as LOG_ERROR
from gui.sounds.epic_sound_constants import EPIC_SOUND as EPIC_SOUND, EPIC_OVERTIME_SOUND_NOTIFICATIONS as EPIC_OVERTIME_SOUND_NOTIFICATIONS
from gui.sounds.epic_sound_constants import BF_EB_MAIN_OBJECTIVES_SOUND_NOTIFICATIONS as BF_EB_MAIN_OBJECTIVES_SOUND_NOTIFICATIONS
from gui.battle_control.view_components import IViewComponentsController as IViewComponentsController
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from epic_constants import EPIC_BATTLE_TEAM_ID as EPIC_BATTLE_TEAM_ID
from gui.Scaleform.genConsts.GAME_MESSAGES_CONSTS import GAME_MESSAGES_CONSTS as GAME_MESSAGES_CONSTS
from gui.battle_control import avatar_getter as avatar_getter
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from arena_component_system.sector_base_arena_component import ID_TO_BASENAME as ID_TO_BASENAME
from PlayerEvents import g_playerEvents as g_playerEvents
OVERTIME_DURATION_WARNINGS: list

class GameNotificationsController(IViewComponentsController, TriggersManager.ITriggerListener):
    __slots__: tuple
    _sessionProvider: Any
    _notificationMap: Any
    __ui: Any
    __eManager: Any
    __soundNotificationOnlyOneLeft: Any
    onGameNotificationRecieved: Any
    def __init__(self, setup):
        ...
    def onMessagePlaybackEnded(self, messageID, data):
        ...
    def onMessagePlaybackStarted(self, messageID, data):
        ...
    def onMessagePlaybackPhaseStarted(self, messageID, data):
        ...
    def onMessagePlaybackHide(self, messageID, data):
        ...
    def _setupNotificationMap(self):
        ...
    def setViewComponents(self, *components):
        ...
    def clearViewComponents(self):
        ...
    def getControllerID(self):
        ...
    def getUI(self):
        ...
    def startControl(self):
        ...
    def __start(self):
        ...
    def stopControl(self):
        ...
    def onTriggerDeactivated(self, args):
        ...
    def translateMsgId(self, msgId):
        ...

class EPIC_NOTIFICATION(CONST_CONTAINER):
    END_GAME = 1
    SPECIFIC_TIME = 2
    OVERTIME = 3
    ZONE_CAPTURED = 4
    ZONE_CONTESTED = 5
    RANK_CHANGE = 6
    HQ_DESTROYED = 7
    HQ_ACTIVE = 8
    BASE_ACTIVE = 9
    RETREAT = 10
    HQ_UNDER_ATTACK = 11
    GENERAL_APPEARED = 12
    HQ_BATTLE_START = 13
    RETREAT_SUCCESSFUL = 14

class EpicGameNotificationsController(GameNotificationsController):
    __playMsgOvertimeTriggered: Any
    __shutDownSoundNotifications: Any
    __soundNotificationOnlyOneLeft: Any
    def __init__(self, setup):
        ...
    def _setupNotificationMap(self):
        ...
    def startControl(self):
        ...
    def stopControl(self):
        ...
    def __onEpicRoundFinished(self, winnerTeam, reason):
        ...
    def notify(self, messageID, data):
        ...
    def onMessagePlaybackEnded(self, messageID, data):
        ...
    def onMessagePlaybackPhaseStarted(self, messageID, data):
        ...
    def onMessagePlaybackStarted(self, messageID, data):
        ...
    def onMessagePlaybackHide(self, messageID, data):
        ...
    def overtimeSoundTriggered(self, val):
        ...
    def _isPlayerLaneByBaseId(self, componentSystem, sectorBaseId):
        ...
    def _getBaseNameByBaseId(self, sectorBaseId):
        ...
    def __selectSoundNotifObjDestroy(self, componentSystem, type_, objectiveId):
        ...
    def __playSound(self, eventName):
        ...
