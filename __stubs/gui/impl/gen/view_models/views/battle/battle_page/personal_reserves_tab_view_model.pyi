# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/battle/battle_page/personal_reserves_tab_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import IntEnum as IntEnum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.common.personal_reserves.reserves_group_model import ReservesGroupModel as ReservesGroupModel

class TabAlias(IntEnum):
    STATS = 0
    RESERVES = 1

class PersonalReservesTabViewModel(ViewModel):
    __slots__: tuple
    onBoosterActivate: Any
    def __init__(self, properties=2, commands=1):
        ...
    def getReserveGroups(self):
        ...
    def setReserveGroups(self, value):
        ...
    @staticmethod
    def getReserveGroupsType():
        ...
    def getTabSelection(self):
        ...
    def setTabSelection(self, value):
        ...
    def _initialize(self):
        ...
