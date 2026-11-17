# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/views/battle_type_selector_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class BattleType(Enum):
    SOLO = 'solo'
    PLATOON = 'platoon'
    TEAM = 'team'

class AnimationState(Enum):
    NONE = 'none'
    FIRSTSHOW = 'firstShow'
    IDLEBLINK = 'idleBlink'

class BattleTypeSelectorViewModel(ViewModel):
    __slots__: tuple
    onSelectTab: Any
    def __init__(self, properties=3, commands=1):
        ...
    def getSelectedTab(self):
        ...
    def setSelectedTab(self, value):
        ...
    def getAnimationState(self):
        ...
    def setAnimationState(self, value):
        ...
    def getIsHintShown(self):
        ...
    def setIsHintShown(self, value):
        ...
    def _initialize(self):
        ...
