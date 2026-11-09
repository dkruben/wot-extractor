# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/Scaleform/daapi/view/lobby/states.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/Scaleform/daapi/view/lobby/states.py
from __future__ import absolute_import
from gui.lobby_state_machine.states import SFViewLobbyState, SubScopeSubLayerState
from gui.Scaleform.framework.entities.View import ViewKey
from gui.Scaleform.genConsts.FUNRANDOM_ALIASES import FUNRANDOM_ALIASES

def registerStates(machine):
    machine.addState(FunRandomPrimeTimeState())


def registerTransitions(machine):
    funRandomPrimeTime = machine.getStateByCls(FunRandomPrimeTimeState)
    machine.addNavigationTransitionFromParent(funRandomPrimeTime)


@SubScopeSubLayerState.parentOf
class FunRandomPrimeTimeState(SFViewLobbyState):
    STATE_ID = 'funRandomPrimeTime'
    VIEW_KEY = ViewKey(FUNRANDOM_ALIASES.FUN_RANDOM_PRIME_TIME)
