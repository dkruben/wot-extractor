# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/AvatarCommendations.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/AvatarCommendations.py
from __future__ import absolute_import
import logging
from typing import TYPE_CHECKING
import AccountCommands
from Event import Event
from constants import CommendationsState
from script_component.DynamicScriptComponent import DynamicScriptComponent
if TYPE_CHECKING:
    from typing import Dict, List
    from commendations_common.CommendationHelpers import CommendationStateType, CommendationsSource
_logger = logging.getLogger(__name__)

class AvatarCommendations(DynamicScriptComponent):

    def __init__(self):
        super(AvatarCommendations, self).__init__()
        _logger.debug('CommendationsController initialised!')
        self._messageStateMap = {}
        self.onStateUpdate = Event()

    def onDestroy(self):
        super(AvatarCommendations, self).onDestroy()
        self.onStateUpdate.clear()

    def set_commendationsState(self, oldState):
        self.updateMessageStateMap()

    def setNested_commendationsState(self, path, oldState):
        self.updateMessageStateMap()

    def updateMessageStateMap(self):
        self._messageStateMap = {state['vehID']: CommendationsState(state['messageState']) for state in self.commendationsState}
        self.onStateUpdate()

    def getMessageStateForVehID(self, vehID):
        return self._messageStateMap.get(vehID, CommendationsState.UNSENT)

    def sendCommendation(self, recipientID, source):
        self.cell.sendCommendation(recipientID, source)

    def clearMessageState(self, callback=None):
        if callback is None:

            def __defaultLogger(resultID, errorCode):
                _logger.debug('Action performed: "activateGoodie" resultID=%s, errorCode=%s', resultID, errorCode)

            callback = __defaultLogger
        self.entity._doCmdNoArgs(AccountCommands.CMD_CLEAR_COMMENDATIONS_MESSAGE_STATE, (lambda requestID, resultID, errorCode, ext=None: callback(resultID, errorCode)))
        return
