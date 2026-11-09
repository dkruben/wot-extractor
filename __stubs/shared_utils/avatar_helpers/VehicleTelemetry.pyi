# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client_common/shared_utils/avatar_helpers/VehicleTelemetry.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import zlib as zlib
import math as math
import os.path
import datetime as datetime
from builtins import open as open
from future.moves import pickle as pickle
from future.utils import viewitems as viewitems
import ResMgr as ResMgr
from debug_utils import LOG_WARNING as LOG_WARNING, LOG_ERROR as LOG_ERROR, LOG_CODEPOINT_WARNING as LOG_CODEPOINT_WARNING
from constants import ENABLE_DEBUG_DYNAMICS_INFO as ENABLE_DEBUG_DYNAMICS_INFO
from physics_shared import G as G
from py2to3.compat.ioCompat import UnicodeFileAdapter as UnicodeFileAdapter

class VehicleTelemetry(object):
    physicsDebugInfo: Any
    DYNAMICS_LOG_DIR = 'dynamics_log'
    NAME_DELIMITER = '$'
    HEADER_TEMPLATE: str
    LOG_LINE_TEMPLATE: Any
    avatar: Any
    logName: Any
    saveTextLog: Any
    dynamicsLog: Any
    dynamicsData: Any
    scenarioName: Any
    recordStarted: Any
    __physicsDebugInfoEnabled: Any
    __physicsDebugInfo: Any
    __completionFlag: Any
    logPath: Any
    refTime: Any
    refDist: Any
    def __init__(self, avatar):
        ...
    def enableVehiclePhysicsTelemetry(self, enabled=None):
        ...
    def __checkDynLogDir(self):
        ...
    def __generateDynamicsLogName(self):
        ...
    def recordVehicleDynamics(self, scenarioName, cmd, rapidModeSpeedup=1, saveTextLog=False):
        ...
    def isSimulationComplete(self):
        ...
    def __openDynamicsLog(self, refTime, refDist):
        ...
    def __writeHeader(self):
        ...
    def __closeDynamicsLog(self):
        ...
    def __onStop(self):
        ...
    def __logDynamics(self, paramNamesMap, snapshots):
        ...
    def receivePhysicsDebugInfo(self, info, modifDict):
        ...
