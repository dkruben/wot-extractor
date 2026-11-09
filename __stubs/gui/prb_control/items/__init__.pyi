# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/items/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from constants import PREBATTLE_TYPE as PREBATTLE_TYPE, QUEUE_TYPE as QUEUE_TYPE
from gui.prb_control.items.prb_items import PlayerPrbInfo as PlayerPrbInfo
from gui.prb_control.items.unit_items import PlayerUnitInfo as PlayerUnitInfo
from gui.prb_control.settings import CTRL_ENTITY_TYPE as CTRL_ENTITY_TYPE, FUNCTIONAL_FLAG as FUNCTIONAL_FLAG, PREBATTLE_RESTRICTION as PREBATTLE_RESTRICTION, QUEUE_TYPE_TO_PREBATTLE_TYPE as QUEUE_TYPE_TO_PREBATTLE_TYPE, PREBATTLE_TYPE_TO_QUEUE_TYPE as PREBATTLE_TYPE_TO_QUEUE_TYPE
from gui.shared.utils.decorators import ReprInjector as ReprInjector
SelectResult: Any
CreationResult: Any
ValidationResult: Any

# decorador original: @ReprInjector.simple(...)
class FunctionalState(object):
    __slots__: tuple
    ctrlTypeID: Any
    entityTypeID: Any
    hasModalEntity: Any
    hasLockedState: Any
    isIntroMode: Any
    funcState: Any
    funcFlags: Any
    rosterType: Any
    def __init__(self, ctrlTypeID=0, entityTypeID=0, hasModalEntity=False, hasLockedState=False, isIntroMode=False, funcState=None, funcFlags=..., rosterType=0):
        ...
    def isInLegacy(self, prbType=0):
        ...
    def isInSpecialPrebattle(self):
        ...
    def isInUnit(self, prbType=0):
        ...
    def isInPreQueue(self, queueType=0):
        ...
    def isQueueSelected(self, queueType):
        ...
    def doLeaveToAcceptInvite(self, prbType=0):
        ...
    def isReadyActionSupported(self):
        ...
    def isNavigationDisabled(self):
        ...
    def __getQueueTypeByPrbType(self, prbType):
        ...

# decorador original: @ReprInjector.simple(...)
class PlayerDecorator(object):
    __slots__: tuple
    isCreator: Any
    isReady: Any
    def __init__(self, isCreator=False, isReady=False):
        ...
