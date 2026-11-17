# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/HWArenaPhasesComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from helpers import isPlayerAvatar as isPlayerAvatar
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
import Event as Event
import logging as logging
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from helpers.EffectsList import effectsFromSection as effectsFromSection, EffectsListPlayer as EffectsListPlayer
from helpers import newFakeModel as newFakeModel, dependency as dependency
from halloween_dyn_object_cache import HWEffects as HWEffects, getEffectSection as getEffectSection
from halloween_common.halloween_constants import INVALID_PHASE as INVALID_PHASE
from halloween.gui.halloween_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_logger: Any

class HWEnvironmentSwitcher(object):
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

class HWArenaPhasesComponent(DynamicScriptComponent):
    onPhaseChanged: Any
    onPhaseModifierChanged: Any
    onPhaseTimeChanged: Any
    onHideVehicleOnMinimap: Any
    onBossVulnerableChanged: Any
    onMinimapAutoZoomChanged: Any
    guiSessionProvider: Any
    envSwitcher: Any
    def __init__(self):
        ...
    def onDestroy(self):
        ...
    def _onAvatarReady(self):
        ...
    @property
    def hwBattleGuiCtrl(self):
        ...
    def set_activePhase(self, prev):
        ...
    def set_modifierName(self, prev):
        ...
    def set_modifierColor(self, prev):
        ...
    def set_timeLeft(self, prev):
        ...
    def set_activeEnvironment(self, prev):
        ...
    def set_isBossVulnerable(self, prev):
        ...
    def set_minimapAutoZoom(self, prev):
        ...
    def _setupEnvironment(self, isInstant=False):
        ...
    def hideVehicleOnMinimap(self, vehicleID):
        ...
    def notifyPhaseTimeChanged(self, looterID, ownerID, amount):
        ...
    def isLastPhase(self):
        ...
    @staticmethod
    def getInstance():
        ...
    def _onAvatarVehicleChanged(self):
        ...
