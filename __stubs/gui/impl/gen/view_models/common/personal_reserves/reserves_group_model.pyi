# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/common/personal_reserves/reserves_group_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.common.personal_reserves.booster_model import BoosterModel as BoosterModel

class GroupCategory(Enum):
    XP = 'xp'
    CREDITS = 'credits'
    COMBINED_XP = 'combined'
    EVENT = 'event'
    CLAN = 'clan'

class ReservesGroupModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=2, commands=0):
        ...
    def getCategory(self):
        ...
    def setCategory(self, value):
        ...
    def getReserves(self):
        ...
    def setReserves(self, value):
        ...
    @staticmethod
    def getReservesType():
        ...
    def _initialize(self):
        ...
