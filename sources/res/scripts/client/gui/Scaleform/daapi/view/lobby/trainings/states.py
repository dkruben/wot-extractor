# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/trainings/states.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/trainings/states.py
from __future__ import absolute_import
import typing
from gui.Scaleform.framework.entities.View import ViewKey
from gui.Scaleform.genConsts.PREBATTLE_ALIASES import PREBATTLE_ALIASES
from gui.impl import backport
from gui.impl.gen.resources import R
from gui.lobby_state_machine.states import SubScopeSubLayerState, SFViewLobbyState, LobbyStateDescription
from gui.prb_control import prbEntityProperty
from gui.prb_control.entities.base.legacy.ctx import SetPlayerStateCtx
from gui.prb_control.entities.training.legacy.entity import TrainingEntity

def registerStates(machine):
    machine.addState(TrainingListState())
    machine.addState(TrainingRoomState())


def registerTransitions(machine):
    machine.addNavigationTransitionFromParent(machine.getStateByCls(TrainingListState))
    machine.addNavigationTransitionFromParent(machine.getStateByCls(TrainingRoomState))


@SubScopeSubLayerState.parentOf
class TrainingListState(SFViewLobbyState):
    STATE_ID = PREBATTLE_ALIASES.TRAINING_LIST_VIEW_PY
    VIEW_KEY = ViewKey(PREBATTLE_ALIASES.TRAINING_LIST_VIEW_PY)

    def getNavigationDescription(self):
        return LobbyStateDescription(backport.text(R.strings.menu.training.listTitle()))


@SubScopeSubLayerState.parentOf
class TrainingRoomState(SFViewLobbyState):
    STATE_ID = PREBATTLE_ALIASES.TRAINING_ROOM_VIEW_PY
    VIEW_KEY = ViewKey(PREBATTLE_ALIASES.TRAINING_ROOM_VIEW_PY)

    @prbEntityProperty
    def prbEntity(self):
        return

    def _onEntered(self, event):
        super(TrainingRoomState, self)._onEntered(event)
        silently = event.params.get('silently', False)
        if isinstance(self.prbEntity, TrainingEntity):
            self.prbEntity.setPlayerState(SetPlayerStateCtx(True, waitingID='prebattle/player_ready', silently=silently))

    def _onExited(self):
        super(TrainingRoomState, self)._onExited()
        if isinstance(self.prbEntity, TrainingEntity):
            self.prbEntity.setPlayerState(SetPlayerStateCtx(False, waitingID='prebattle/player_not_ready'))

    def getNavigationDescription(self):
        return LobbyStateDescription(backport.text(R.strings.pages.titles.trainingRoom()))
