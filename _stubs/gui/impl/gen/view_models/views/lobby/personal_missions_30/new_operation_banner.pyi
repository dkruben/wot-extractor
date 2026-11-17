# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/personal_missions_30/new_operation_banner.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class BannerState(Enum):
    DEFAULT = 'default'
    COMPLETED_WITH_HONOR = 'completedWithHonor'
    COMPLETED = 'completed'

class NewOperationBanner(ViewModel):
    __slots__: tuple
    def __init__(self, properties=4, commands=0):
        ...
    def getOperationId(self):
        ...
    def setOperationId(self, value):
        ...
    def getBannerState(self):
        ...
    def setBannerState(self, value):
        ...
    def getFirstTimeEntrance(self):
        ...
    def setFirstTimeEntrance(self, value):
        ...
    def getEnabled(self):
        ...
    def setEnabled(self, value):
        ...
    def _initialize(self):
        ...
