# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/frameworks_common/state_machine/visitor.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from .transitions import BaseTransition as BaseTransition
from .exceptions import NodeError as NodeError
from .node import Node as Node
from . import State as State

def getAncestors(node, upper=None):
    ...
def isDescendantOf(node, ancestor):
    ...
def getDescendantIndex(node, ancestor, filter_=None):
    ...
def getLCA(nodes, upper=None):
    ...
def getEffectiveTargetStates(transition, history):
    ...
def getTransitionDomain(transition, history, upper=None):
    ...
