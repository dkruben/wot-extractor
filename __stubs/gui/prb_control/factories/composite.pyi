# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/factories/composite.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.prb_control.factories.ControlFactory import ControlFactory as ControlFactory
from gui.prb_control.factories.PreQueueFactory import PreQueueFactory as PreQueueFactory
from gui.prb_control.factories.LegacyFactory import LegacyFactory as LegacyFactory
from gui.prb_control.factories.UnitFactory import UnitFactory as UnitFactory
from gui.prb_control.settings import CTRL_ENTITY_TYPE as CTRL_ENTITY_TYPE, FUNCTIONAL_FLAG as FUNCTIONAL_FLAG
from soft_exception import SoftException as SoftException
_ORDER_TO_CREATE: tuple

class ControlFactoryComposite(ControlFactory):
    __factories: Any
    def __init__(self):
        ...
    def clear(self):
        ...
    def get(self, ctrlType):
        ...
    def createEntry(self, ctx):
        ...
    def createEntryByAction(self, action):
        ...
    def createEntity(self, ctx):
        ...
    def createLeaveCtx(self, flags=..., entityType=0):
        ...
    def createStateEntity(self, entity):
        ...
