# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/StoryModeAvatarComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from Event import Event as Event
from script_component.ScriptComponent import ScriptComponent as ScriptComponent

class StoryModeAvatarComponent(ScriptComponent):
    onSMAbilityWrongPoint: Any
    onPositionValidChanged: Any
    def set_wrongApplicationPoint(self, _):
        ...
    def set_isPositionValid(self, prevValue):
        ...
    def checkPositionForEquipment(self, equipmentId, position):
        ...
