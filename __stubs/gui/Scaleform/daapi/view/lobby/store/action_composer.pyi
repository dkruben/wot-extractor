# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/store/action_composer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import lmap as lmap, viewvalues as viewvalues
from debug_utils import LOG_WARNING as LOG_WARNING
from shared_utils import findFirst as findFirst, first as first

class ComposedActionsCollection(object):
    _actions: Any
    finishTime: Any
    value: Any
    def __init__(self, action):
        ...
    def add(self, action):
        ...
    def compose(self):
        ...

class SimpleMixCollection(ComposedActionsCollection):
    _localizationKey = ''
    _groupMarkers: tuple
    def compose(self):
        ...
    def _composeActions(self, actions, compositionKey='mixed'):
        ...
    def _canCompose(self, action1, action2):
        ...
    def _separateActions(self):
        ...
    def _buildCompositionName(self, compositionType):
        ...
    @classmethod
    def _findBetter(cls, actionsGroup):
        ...
    @staticmethod
    def _cmpActions(action1, action2):
        ...

class TankmenActionsCollection(SimpleMixCollection):
    _localizationKey = 'tankmen'

class DropSkillsActionsCollection(SimpleMixCollection):
    _localizationKey = 'dropSkills'

class ShellActionsCollection(SimpleMixCollection):
    _localizationKey = 'shell'

class EquipmentActionsCollection(SimpleMixCollection):
    _localizationKey = 'equipment'

class PremiumActionsCollection(SimpleMixCollection):
    _localizationKey = 'premiumPacket'
    _groupMarkers: tuple
    def compose(self):
        ...

class CompositionRule(object):
    _applicableParamsNames: list
    @classmethod
    def applicableTo(cls, action):
        ...
    @classmethod
    def getType(cls):
        ...
    @staticmethod
    def canAdd(collection, action):
        ...

class TankmenRule(CompositionRule):
    collectionClass = TankmenActionsCollection
    _applicableParamsNames: tuple

class DropSkillsRule(CompositionRule):
    collectionClass = DropSkillsActionsCollection
    _applicableParamsNames: tuple

class ShellsRule(CompositionRule):
    collectionClass = ShellActionsCollection
    _applicableParamsNames: tuple

class EquipmentRule(CompositionRule):
    collectionClass = EquipmentActionsCollection
    _applicableParamsNames: tuple

class PremiumRule(CompositionRule):
    collectionClass = PremiumActionsCollection
    _applicableParamsNames: tuple

class ActionComposer(object):
    __compositionRules: tuple
    __collections: Any
    __singleActions: Any
    def __init__(self):
        ...
    def add(self, action):
        ...
    def getActions(self):
        ...
    def __composeCollections(self):
        ...
