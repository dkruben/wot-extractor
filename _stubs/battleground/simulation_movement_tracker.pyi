# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/battleground/simulation_movement_tracker.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import itertools as itertools
import logging as logging
from collections import namedtuple as namedtuple, deque as deque
import BigWorld as BigWorld
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME
from constants import ARENA_PERIOD as ARENA_PERIOD
from gun_rotation_shared import decodeGunAngles as decodeGunAngles
from helpers import isPlayerAvatar as isPlayerAvatar
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from PlayerEvents import g_playerEvents as g_playerEvents
_logger: Any
SimulationMovementData: Any
ShotMapData: Any

class SimulationMovementTracker(CallbackDelayer):
    __MAX_TIME_TILL_DEATH = 60.0
    __PENDING_SHOT_ID = 'pending'
    __isTrackingActive: Any
    __tickDelay: Any
    __snapshotLength: Any
    __maxDataPoints: Any
    __data: Any
    __lastPointTime: Any
    __snapshots: Any
    __shotsMap: Any
    __snapshotsMap: Any
    __pointsCaptured: Any
    __isStartRequested: Any
    def __init__(self, tickDelay, snapshotLength):
        ...
    def create(self):
        ...
    def destroy(self):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def getData(self, shotID):
        ...
    def getSnapshot(self, shotID, isKill):
        ...
    def saveSnapshot(self, shotID=0, isKill=False):
        ...
    def clearSnapshot(self, shotID, isKill=None):
        ...
    def setPendingShotID(self, shotID):
        ...
    def __onArenaPeriodChange(self, period, periodEndTime, periodLength, periodAdditionalInfo):
        ...
    def __onTracerReceived(self, shotID):
        ...
    @staticmethod
    def __makeSnapshotID(shotID, isKill):
        ...
    def __tick(self):
        ...
    def __cleanupSnapshots(self):
        ...
    @staticmethod
    def __getGunAngles(veh):
        ...
