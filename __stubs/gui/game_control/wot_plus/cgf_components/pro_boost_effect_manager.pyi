# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/wot_plus/cgf_components/pro_boost_effect_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from typing import TYPE_CHECKING as TYPE_CHECKING, Optional as Optional, Callable as Callable, Dict as Dict, List as List
import BigWorld as BigWorld
import CGF as CGF
import Math as Math
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle, g_currentVehicle as g_currentVehicle
from frameworks.wulf import WindowStatus as WindowStatus
from gui.game_control.wot_plus.utils import ProBoostUtils as ProBoostUtils
from gui.lobby_state_machine.states import isInHangarState as isInHangarState
from gui.shared import g_eventBus as g_eventBus, events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from helpers import dependency as dependency
from renewable_subscription_common.settings_constants import PRO_BOOST_PDATA_KEY as PRO_BOOST_PDATA_KEY, PRO_BOOSTED_VEHICLE as PRO_BOOSTED_VEHICLE
from skeletons.gui.game_control import IWotPlusController as IWotPlusController
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from cgf_script.registration import registerModule as registerModule
from gui.game_control.wot_plus_controller import WotPlusController as WotPlusController
from gui.impl.gui_loader import GuiLoader as GuiLoader
_ACTIVATION_TIMEOUT = 0.5
_ACTIVATION_PREFAB = 'content/CGFPrefabs/Lobby/proboost_activation.prefab'
_DEACTIVATION_PREFAB = 'content/CGFPrefabs/Lobby/proboost_deactivation.prefab'
_logger: Any

class WotPlusProBoostSystem(CGF.System):
    _wotPlusCtrl: Any
    _uiLoader: Any
    Reactions: Any
    _boostedVehicleInvID: Any
    _delayer: Any
    _activationEffectGO: Any
    _deactivationEffectGO: Any
    _windowsManager: Any
    _loadingInProgressMap: Any
    def __init__(self):
        ...
    def onMappingLoaded(self):
        ...
    def onMappingUnloaded(self):
        ...
    @property
    def isCurrentVehicleAvailableAndBoosted(self):
        ...
    def _loadProBoostActivationEffect(self):
        ...
    def _loadProBoostDeactivationEffect(self):
        ...
    def _loadPrefabWithCallback(self, prefab, callback):
        ...
    def _onControllerDataChanged(self, diff):
        ...
    def _activateEffect(self):
        ...
    def _deactivateEffect(self):
        ...
    def __toggleEffects(self, prefabToActivate, prefabToDeactivate, loadingMethod):
        ...
    def _onActivationPrefabLoaded(self, objects, queue):
        ...
    def _onDeactivationPrefabLoaded(self, objects, queue):
        ...
    def _onWindowStatusChanged(self, _, status):
        ...
    def _onPrbSwitch(self, _):
        ...

# decorador original: @registerModule
class WotPlusProBoostModule(object):
    name = 'WoT plus boost'
    group = 'Hangar'
    systems: list
