# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicle_systems/components/engine_state.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicle_systems/components/engine_state.py
from __future__ import absolute_import
from random import uniform
import BigWorld
from constants import ARENA_PERIOD
from helpers import dependency
from skeletons.gameplay import IGameplayLogic, GameplayStateID
from skeletons.gui.battle_session import IBattleSessionProvider

class EngineState(object):
    NORMAL = 0
    REPAIRED = 1
    CRITICAL = 2
    DESTROYED = 3


class EngineLoad(object):
    _STOPPED = 0
    _IDLE = 1
    _MEDIUM = 2
    _HIGH = 3


_StateConvertor = {'destroyed': (EngineState.DESTROYED), 
   'critical': (EngineState.CRITICAL), 
   'repaired': (EngineState.REPAIRED), 
   'normal': (EngineState.NORMAL)}

def getEngineStateFromName(stateName):
    return _StateConvertor.get(stateName, EngineState.NORMAL)


_ENGINE_START_STATE_IDS = (
 GameplayStateID.PREBATTLE, GameplayStateID.BATTLE)

def checkEngineStart(detailedEngineState, period):
    gameplayLogic = dependency.instance(IGameplayLogic)
    if period == ARENA_PERIOD.PREBATTLE:
        gameplayLogic.addOneshotObserver(_ENGINE_START_STATE_IDS, detailedEngineState, enterFn=_delayEngineStart)
        return True
    if period == ARENA_PERIOD.BATTLE:
        detailedEngineState.startEngineWithDelay(0.1, False)
        return True
    return False


def notifyEngineOnArenaPeriodChange(detailedEngineState, period):
    if period == ARENA_PERIOD.WAITING:
        gameplayLogic = dependency.instance(IGameplayLogic)
        gameplayLogic.addOneshotObserver(_ENGINE_START_STATE_IDS, detailedEngineState, enterFn=_delayEngineStart)
        return True
    else:
        if period == ARENA_PERIOD.PREBATTLE:
            sessionProvider = dependency.instance(IBattleSessionProvider)
            pbhCtrl = sessionProvider.dynamic.prebattleHighlightsController
            if pbhCtrl is not None and not pbhCtrl.pbhWasShown:
                gameplayLogic = dependency.instance(IGameplayLogic)
                gameplayLogic.addOneshotObserver(_ENGINE_START_STATE_IDS, detailedEngineState, enterFn=_delayEngineStart)
            else:
                detailedEngineState.startEngineWithDelay(0.1, False)
            return True
        return False


def _delayEngineStart(detailedEngineState, _=None, __=None):
    arena = BigWorld.player().arena
    if arena.period == ARENA_PERIOD.AFTERBATTLE:
        return
    if arena.period == ARENA_PERIOD.BATTLE:
        detailedEngineState.startEngineWithDelay(0.1, False)
        return
    maxTime = _getTimeToBattleStart(arena)
    maxTime = maxTime * 0.7 if maxTime > 0.0 else 1.0
    startEnginesIn = uniform(0.0, maxTime)
    detailedEngineState.startEngineWithDelay(startEnginesIn, True)


def _getTimeToBattleStart(arena):
    serverTime = BigWorld.serverTime()
    if serverTime <= 0.0:
        return arena.periodLength
    return min(arena.periodEndTime - serverTime, arena.periodLength)
