# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/tutorial/data/conditions.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import functools as functools
from tutorial.data.has_id import HasID as HasID
__all__: tuple

class CONDITION_TYPE(object):
    FLAG = 0
    GLOBAL_FLAG = 1
    WINDOW_ON_SCENE = 3
    GAME_ITEM_SIMPLE_STATE = 4
    GAME_ITEM_RELATE_STATE = 5
    VAR_DEFINED = 6
    VAR_COMPARE = 7
    EFFECT_TRIGGERED = 8
    SERVICE = 10
    COMPONENT_ON_SCENE = 11
    CURRENT_SCENE = 12
    VIEW_PRESENT = 13
    CONNECTED_ITEM = 14
    CONDITION_AND = 15
    CONDITION_OR = 16
    CLASS_CONDITION = 17
    FIRST_CUSTOM = 100
    BASE_RANGE: tuple
    COMPLEX: tuple

# decorador original: @functools.total_ordering
class _StateValue(object):
    __slots__: tuple
    value: Any
    def __init__(self, value):
        ...
    def __repr__(self):
        ...
    def __invert__(self):
        ...
    def __neg__(self):
        ...
    def __eq__(self, other):
        ...
    def __gt__(self, other):
        ...
    def __hash__(self):
        ...
    @property
    def base(self):
        ...
    @property
    def positive(self):
        ...
    @property
    def negative(self):
        ...

class CONDITION_STATE(object):
    UNDEFINED: Any
    ACTIVE: Any
    EQUALS: Any
    SELECTED: Any
    PREMIUM: Any
    UNLOCKED: Any
    IN_INVENTORY: Any
    XP_ENOUGH: Any
    MONEY_ENOUGH: Any
    LEVEL: Any
    MAY_INSTALL: Any
    INSTALLED: Any
    CREW_HAS_ANY_SKILL: Any
    HAS_REGULAR_CONSUMABLES: Any
    HAS_OPTIONAL_DEVICES: Any
    RANGE: tuple
    GAME_ITEM_SIMPLE_STATE: tuple
    GAME_ITEM_RELATE_STATE: tuple

class Condition(HasID):
    _state: Any
    def __init__(self, entityID, condType, state):
        ...
    def getBaseState(self):
        ...
    def isPositiveState(self):
        ...
    def isNegativeState(self):
        ...

class ActiveCondition(Condition):
    def __init__(self, entityID, condType, state=...):
        ...

class CompareCondition(Condition):
    _compareID: Any
    def __init__(self, entityID, condType, compareID, state=...):
        ...
    def getCompareID(self):
        ...

class FlagCondition(ActiveCondition):
    def __init__(self, entityID, state=...):
        ...

class GlobalFlagCondition(ActiveCondition):
    def __init__(self, entityID, state=...):
        ...

class WindowOnSceneCondition(ActiveCondition):
    def __init__(self, entityID, state=...):
        ...

class ComponentOnSceneCondition(ActiveCondition):
    def __init__(self, entityID, state=...):
        ...

class CurrentSceneCondition(ActiveCondition):
    def __init__(self, entityID, state=...):
        ...

class ViewPresentCondition(ActiveCondition):
    __layer: Any
    __viewAlias: Any
    def __init__(self, layer, viewAlias, state=...):
        ...
    def getLayer(self):
        ...
    def getViewAlias(self):
        ...

class VarDefinedCondition(ActiveCondition):
    def __init__(self, entityID, state=...):
        ...

class VarCompareCondition(CompareCondition):
    def __init__(self, entityID, compareID, state=...):
        ...

class EffectTriggeredCondition(ActiveCondition):
    def __init__(self, entityID, state=...):
        ...

class GameItemSimpleStateCondition(Condition):
    def __init__(self, entityID, state):
        ...

class GameItemRelateStateCondition(Condition):
    __otherIDs: Any
    def __init__(self, entityID, otherIDs, state):
        ...
    def getOtherIDs(self):
        ...

class ServiceCondition(ActiveCondition):
    __serviceClass: Any
    def __init__(self, entityID, serviceClass, state=...):
        ...
    def getServiceClass(self):
        ...

class ClassCondition(ActiveCondition):
    __conditionClass: Any
    __arguments: Any
    def __init__(self, entityID, conditionClass, arguments, state=...):
        ...
    def getConditionClass(self):
        ...
    def getArguments(self):
        ...

class ConnectedItemCondition(Condition):
    __isShown: Any
    def __init__(self, entityID, isShown, state=...):
        ...
    def isShown(self):
        ...

class _ComplexCondition(Condition):
    __conditionList: Any
    def __init__(self, items, conditionType):
        ...
    def getConditionList(self):
        ...

class ComplexConditionAnd(_ComplexCondition):
    def __init__(self, items):
        ...

class ComplexConditionOr(_ComplexCondition):
    def __init__(self, items):
        ...

class Conditions(list):
    _eitherBlocks: Any
    def __init__(self, *args):
        ...
    def __repr__(self):
        ...
    def appendEitherBlock(self, block):
        ...
    def eitherBlocks(self):
        ...
    def clear(self):
        ...
    def getUnwrappedConditions(self):
        ...
    @staticmethod
    def __unwrapComplexConditions(conditions):
        ...
