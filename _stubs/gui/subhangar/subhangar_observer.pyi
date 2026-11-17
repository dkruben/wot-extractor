# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/subhangar/subhangar_observer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import namedtuple as namedtuple
import CGF as CGF
import Hangar as Hangar
import Math as Math
import ResMgr as ResMgr
import typing as typing
from shared_utils import first as first
from cgf_components.hangar_camera_manager import HangarCameraSystem as HangarCameraSystem
from frameworks_common.state_machine import BaseStateObserver as BaseStateObserver
from gui.subhangar.subhangar_state_groups import SubhangarStateGroupConfigProvider as SubhangarStateGroupConfigProvider
from helpers import dependency as dependency
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from vehicle_systems.tankStructure import getVehicleAABB as getVehicleAABB, selectItemByTankSize as selectItemByTankSizeBase
from typing import Union as Union, Iterable as Iterable, Sized as Sized, Optional as Optional
from frameworks_common.state_machine import StateEvent as StateEvent
from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine as LobbyStateMachine
from gui.lobby_state_machine.states import LobbyState as LobbyState
from gui.shared.events import NavigationEvent as NavigationEvent
_logger: Any
_CONFIG_PATH = 'spaces/subhangars.xml'
_GroupConfig: Any
T: Any
SubhangarActivationConfig: Any

class _SubhangarConfig(object):
    __stateGroupsToGroups: Any
    def __init__(self, path):
        ...
    def getGroups(self, stateGroups):
        ...
    def _getStates(self, rawString):
        ...
    def _parseConfig(self, path):
        ...

class SubhangarObserver(BaseStateObserver):
    __hangarSpace: Any
    __activatedSubHangars: Any
    __subHangarsToActivate: Any
    __subHangarsToDeactivate: Any
    __config: Any
    __lsm: Any
    def __init__(self, lsm, path=...):
        ...
    def isObservingState(self, state):
        ...
    def clear(self):
        ...
    def onEnterState(self, state, event):
        ...
    def onExitState(self, state, event):
        ...
    def __navigationsFinished(self, *_):
        ...
    def __configureSubHangars(self):
        ...

def hangarVehicleAABB():
    ...
def selectItemByTankSize(tankSizeLowerBounds, items, default=None):
    ...
