# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/LSArenaPhasesComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
import Event as Event
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import GameEvent as GameEvent
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from helpers.EffectsList import effectsFromSection as effectsFromSection, EffectsListPlayer as EffectsListPlayer
from helpers import newFakeModel as newFakeModel, isPlayerAvatar as isPlayerAvatar
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from ls_dyn_object_cache import LSEffects as LSEffects, getEffectSection as getEffectSection
from last_stand_common.last_stand_constants import INVALID_PHASE as INVALID_PHASE
_logger: Any

class LSEnvironmentSwitcher(object):
    _isSwitchInProcess: Any
    _callbackDelayer: Any
    _fakeModel: Any
    _effectsPlayer: Any
    _spaceID: Any
    _effects: Any
    _envSwitchDelay: Any
    def __init__(self, spaceID):
        ...
    def onDestroy(self):
        ...
    def setupEnvironment(self, envName, isInstantSwitch=False):
        ...
    def _cancelOngoingSwitcher(self):
        ...
    def _switchEnvironment(self, envName):
        ...

class LSArenaPhasesComponent(DynamicScriptComponent):
    onPhaseChanged: Any
    onPhaseTimeChanged: Any
    onHideVehicleOnMinimap: Any
    onCleanBCMarkersRequested: Any
    envSwitcher: Any
    def __init__(self):
        ...
    def onDestroy(self):
        ...
    def _onAvatarReady(self):
        ...
    def set_activePhase(self, prev):
        ...
    def set_timeLeft(self, prev):
        ...
    def set_activeEnvironment(self, prev):
        ...
    def set_isBCMarkersCleanupEnabled(self, prev):
        ...
    def _setupEnvironment(self, isInstant=False):
        ...
    def hideVehicleOnMinimap(self, vehicleID):
        ...
    def cleanBCMarkers(self):
        ...
    def isLastPhase(self):
        ...
    @staticmethod
    def getInstance():
        ...
    def _onBattleLoading(self, event):
        ...
