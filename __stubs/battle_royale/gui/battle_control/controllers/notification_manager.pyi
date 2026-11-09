# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/battle_control/controllers/notification_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from enum import IntEnum as IntEnum
import BigWorld as BigWorld
from Event import Event as Event
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from math_common import round_py2_style_int as round_py2_style_int
from battle_royale.gui.Scaleform.daapi.view.battle.respawn_message_panel import RespawnMessagePanel as RespawnMessagePanel
logger: Any
InvalidMessageTypeRange: tuple
allMessageTypes: tuple
DeleteMsgTypeMapping: dict

class INotificationManagerListener(object):
    def addNotificationManager(self, notificationManager):
        ...

class RespawnMessage(CallbackDelayer):
    msgType: Any
    messageVO: Any
    delay: Any
    postDelay: Any
    time: Any
    showBefore: Any
    __endTime: Any
    __msgCallbackID: Any
    __delayCallbackID: Any
    __postDelayCallbackID: Any
    __stopCallbackID: Any
    hideCallback: Any
    __panel: Any
    __hiddenFromPanel: Any
    def __init__(self):
        ...
    def __repr__(self):
        ...
    def setHideCallback(self, hideCallback):
        ...
    def sendMessage(self, panel):
        ...
    def updateTime(self, newTime):
        ...
    def stop(self, skipPostDelay=False):
        ...
    def __hide(self):
        ...
    @property
    def timeLeft(self):
        ...
    def __startDelayTimer(self):
        ...
    def __onDelayFinished(self):
        ...
    def __setMsgCallback(self):
        ...
    def __stopByCallback(self):
        ...
    def __startPostDelayTimer(self):
        ...
    def _calculate(self):
        ...
    def __tick(self):
        ...

class MessageType(IntEnum):
    respActivatedMsg = 0
    respFinishedMsg = 1
    respNotAvailableMsg = 2
    allyInBattleMsg = 3
    stayInCoverMsg = 4
    pickUpSphereMsg = 5
    allyRespawnedMessage = 6
    respNotAvailableSoonMsg = 7
    vehicleDeadMsg = 8

class INotificationHandler(object):
    isActive: Any
    def __init__(self):
        ...
    def tryToProceed(self):
        ...
    def checkOtherHandlers(self, handlers):
        ...

class NotificationManager(object):
    RESPAWN_FAST_SHOW_TIME = 2
    RESPAWN_ADDITIONAL_DELAY = 2
    upgradeHandler: Any
    respawnHandler: Any
    _curHandler: Any
    __needToUpdate: Any
    def __init__(self):
        ...
    @property
    def handlersList(self):
        ...
    def fini(self):
        ...
    def addRespawnPanel(self, panel):
        ...
    def addRespawnMessage(self, message):
        ...
    def updateHandlersDependencies(self):
        ...
    def clearQueue(self):
        ...
    def addUpgradePanelHandler(self, handlerMethod):
        ...
    def setUpgradeVisibility(self, isVisible):
        ...
    def update(self):
        ...
    def setCurrentHandler(self, handler):
        ...
    def onHandlerRealised(self):
        ...

class UpgradeHandler(INotificationHandler):
    handleMethod: Any
    __lastUpdateState: Any
    __isUpgradeVisible: Any
    __isUpgradeVisibilityUpdated: Any
    hideTime: Any
    onUpdateNeeded: Any
    isActive: Any
    def __init__(self, handleMethod):
        ...
    @property
    def isUpgradeVisible(self):
        ...
    def setState(self, isVisible):
        ...
    def update(self):
        ...
    def tryToProceed(self):
        ...

class RespawnHandler(INotificationHandler):
    RESPAWN_FAST_SHOW_TIME = 2
    RESPAWN_ADDITIONAL_DELAY = 3
    panel: Any
    isHighPriority: Any
    _highPriorQueue: Any
    _messageQueue: Any
    _curMsg: Any
    __curStateMsg: Any
    __upgradeHidingTime: Any
    prevActiveState: Any
    onUpdateNeeded: Any
    isActive: Any
    def __init__(self, panel):
        ...
    @property
    def hasMessage(self):
        ...
    def checkOtherHandlers(self, handlers):
        ...
    def addMessage(self, message):
        ...
    def addMessageToQueues(self, newMsg):
        ...
    def updateQueues(self):
        ...
    def tryToProceed(self):
        ...
    def update(self):
        ...
    def send(self, message):
        ...
    def onMessageHide(self):
        ...
    def clearAll(self):
        ...
    def __getValidMessage(self):
        ...
    @staticmethod
    def __deleteMessageFromQueue(queue, deleteMsgTypes):
        ...
    @property
    def __upgradeHideTimeout(self):
        ...
