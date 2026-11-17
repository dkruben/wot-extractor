# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/PlatoonLighting.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from enum import Enum as Enum
import BigWorld as BigWorld
import AnimationSequence as AnimationSequence
import Math as Math
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, g_eventBus as g_eventBus, events as events
from skeletons.gui.game_control import IPlatoonController as IPlatoonController
from vehicle_systems.stricted_loading import makeCallbackWeak as makeCallbackWeak
from ClientSelectableObject import ClientSelectableObject as ClientSelectableObject
from helpers import dependency as dependency
_logger: Any

class _PlatoonLightingStateMachineTriggers(Enum):
    PLATOON_LEFT_ENTER = 'PlatoonLeftEnter'
    PLATOON_LEFT_EXIT = 'PlatoonLeftExit'
    PLATOON_RIGHT_ENTER = 'PlatoonRightEnter'
    PLATOON_RIGHT_EXIT = 'PlatoonRightExit'
    PLATOON_PLAYER_ENTER = 'PlatoonPlayerEnter'
    PLATOON_PLAYER_EXIT = 'PlatoonPlayerExit'

class _PlatoonLightingStateMachineStates(Enum):
    PLAYER_ORIGINAL_LIGHTING = 'PlayerOriginalLighting'
    PLAYER_PLATOON_LIGHTING = 'PlayerPlatoonLighting'
    RIGHT_TANK_READY = 'PlatoonRightTankReady'
    LEFT_TANK_READY = 'PlatoonLeftTankReady'
    FULL_PLATOON = 'PlatoonBothTanksReady'

class PlatoonLighting(ClientSelectableObject):
    __platoonController: Any
    __animator: Any
    def __init__(self):
        ...
    def onEnterWorld(self, prereqs):
        ...
    def onLeaveWorld(self):
        ...
    def __enterPlatoon(self):
        ...
    def __onAnimatorLoaded(self, resourceList):
        ...
    def __onPlatoonTankEnter(self, event):
        ...
    def __onPlatoonTankLeave(self, event):
        ...
    def __leavePlatoon(self):
        ...
    def __enablePlatoonLighting(self, isEnabled):
        ...
