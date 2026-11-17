# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/page/header/header_state_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import Map as Map, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.common.router_model import RouterModel as RouterModel

class HeaderType(Enum):
    HANGAR = 'hangar'
    DEFAULT = 'default'

class HeaderStateModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=2, commands=0):
        ...
    @property
    def router(self):
        ...
    @staticmethod
    def getRouterType():
        ...
    def getFeatures(self):
        ...
    def setFeatures(self, value):
        ...
    @staticmethod
    def getFeaturesType():
        ...
    def _initialize(self):
        ...
