# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/abilities/thunder_strike.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
import Math as Math
from typing import List as List
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
from constants import IS_CLIENT as IS_CLIENT
from helpers import dependency as dependency
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from items import vehicles as vehicles
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
import BigWorld as BigWorld

class ThunderStrike(object):
    ...

# decorador original: @registerComponent
class ThunderStrikeVisualizer(object):
    editorTitle = 'Thunder Strike Visualizer'
    group = 'Abilities'
    domain = CGF.Domain.Client
    strikePrefab: Any

class ThunderStrikeLoader(CallbackDelayer):
    __guiSessionProvider: Any
    __thunderStrikeEntity: Any
    __transform: Any
    __go: Any
    equipment: Any
    __prefabGO: Any
    __loadedEffectIsAlly: Any
    def __init__(self, thunderStrike, transform, go):
        ...
    def activate(self):
        ...
    def deactivate(self):
        ...
    def __launch(self):
        ...
    def __showGuiMarker(self, delay):
        ...
    def __isAttackerAlly(self):
        ...
    def __onPrefabLoaded(self, objects, queue):
        ...
    def __processHit(self):
        ...
    def __removePrefab(self):
        ...
    def __onUpdateObservedVehicleData(self, *args):
        ...

class ThunderStrikeSystem(CGF.System):
    ThunderStrikeActivated: Any
    ThunderLoaderActivated: Any
    ThunderLoaderDeactivated: Any
    Reactions: Any
    def update(self):
        ...
    def visualizeThunderStrike(self, _, __, go, queue):
        ...
