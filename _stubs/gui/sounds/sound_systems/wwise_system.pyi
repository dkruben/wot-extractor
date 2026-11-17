# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/sounds/sound_systems/wwise_system.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import WWISE as WWISE
import Sound as Sound
import BigWorld as BigWorld
from debug_utils import LOG_DEBUG as LOG_DEBUG, LOG_ERROR as LOG_ERROR, LOG_WARNING as LOG_WARNING
from gui.sounds.abstract import SoundSystemAbstract as SoundSystemAbstract
from gui.sounds.sound_constants import SoundSystems as SoundSystems, SPEAKERS_CONFIG as SPEAKERS_CONFIG
_LAPTOP_SOUND_PRESET = 2
_LOGIN = 0
_LOBBY = 1
_QUEUE = 2
_BATTLE_LOADING = 3
_BATTLE = 4
_BATTLE_RESULT = 5
_envTransition: tuple

class _EnvironmentListNode(object):
    __slots__: tuple
    __prev: Any
    __next: Any
    __environment: Any
    __enterState: Any
    __exitState: Any
    __envID: Any
    __cbkID: Any
    def __init__(self, environment, start_state, exit_state, envID, previous=None):
        ...
    def pushEnv(self, nextNode):
        ...
    def setPrev(self, prevState):
        ...
    def setNext(self, nextState):
        ...
    def popEnv(self):
        ...
    def setDelayedEnter(self, prevID):
        ...
    def __setEnterState(self):
        ...
    def __setExitState(self):
        ...

class _EnvironmentStatesSubSys(object):
    _envStateDefs: dict
    _head: Any
    def __init__(self):
        ...
    def onEnvStart(self, environment):
        ...
    def onEnvStop(self, newEnvironment):
        ...

class WWISESoundSystem(SoundSystemAbstract):
    __envStatesSubSys: Any
    def __init__(self):
        ...
    def getID(self):
        ...
    def isMSR(self):
        ...
    def enableDynamicPreset(self):
        ...
    def disableDynamicPreset(self):
        ...
    def setBassBoost(self, isEnabled):
        ...
    def getSystemSpeakersPresetID(self):
        ...
    def getUserSpeakersPresetID(self):
        ...
    def setUserSpeakersPresetID(self, presetID):
        ...
    def setSoundSystem(self, soundSystemID):
        ...
    def sendGlobalEvent(self, eventName, **params):
        ...
    def onEnvStart(self, environment):
        ...
    def onEnvStop(self, environment):
        ...
