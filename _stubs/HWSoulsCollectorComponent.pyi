# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/HWSoulsCollectorComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import functools as functools
import BigWorld as BigWorld
import CGF as CGF
import Math as Math
import constants as constants
from halloween.cgf_components.soul_collector_wrappers import SoulCollectorWrapper as SoulCollectorWrapper
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from WeakMethod import WeakMethod as WeakMethod
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from halloween.gui.halloween_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from halloween.gui.sounds.souls_collector_sound import SoulsCollectorSound as SoulsCollectorSound
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from halloween_dyn_object_cache import HWPrefabs as HWPrefabs, getPrefabPath as getPrefabPath
from typing import List as List, Callable as Callable

class HWSoulsCollectorComponent(DynamicScriptComponent):
    POLL_RATE = 0.01
    guiSessionProvider: Any
    go: Any
    _visualComponent: Any
    _soundComponent: Any
    _callbacks: Any
    def __init__(self):
        ...
    def onDestroy(self):
        ...
    def set_capacity(self, prev):
        ...
    def set_collected(self, prev):
        ...
    def set_vehiclesInRadius(self, prev):
        ...
    def set_isCampActivated(self, prev):
        ...
    def updateVisualCollectingState(self):
        ...
    @property
    def progress(self):
        ...
    @property
    def isFull(self):
        ...
    @property
    def hwBattleGuiCtrl(self):
        ...
    def updateVisualProgress(self):
        ...
    @property
    def _isReady(self):
        ...
    def _updateVisualCollectingState(self):
        ...
    def _onAvatarReady(self):
        ...
    def _onPrefabLoaded(self, objects, queue):
        ...
    def _waitAllComponentsReady(self):
        ...
    def _onAvatarVehicleChanged(self):
        ...

def _onPrefabLoaded(callback, objects, queue):
    ...
