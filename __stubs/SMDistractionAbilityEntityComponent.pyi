# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/SMDistractionAbilityEntityComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import AnimationSequence as AnimationSequence
import BigWorld as BigWorld
import Math as Math
from Event import Event as Event
from helpers import dependency as dependency
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from story_mode_common.story_mode_constants import DISTRACTION_ABILITY as DISTRACTION_ABILITY

class SMDistractionAbilityEntityComponent(DynamicScriptComponent):
    _SEQUENCE_RADIUS = 200.0
    guiSessionProvider: Any
    onSMDistractionAbilityActivated: Any
    _animator: Any
    def __init__(self):
        ...
    def _onAvatarReady(self):
        ...
    def set_spottedVehiclesIDs(self, _):
        ...
    def onDestroy(self):
        ...
    def _addEffect(self):
        ...
