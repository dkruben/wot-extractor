# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/battle/battle_page/tab_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.views.battle.battle_page.personal_reserves_tab_view_model import PersonalReservesTabViewModel as PersonalReservesTabViewModel
from gui.impl.gen.view_models.views.battle.battle_page.player_list_model import PlayerListModel as PlayerListModel

class TabAlias(Enum):
    STATS = 'Stats'
    RESERVES = 'Reserves'

class TabViewModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=4, commands=0):
        ...
    @property
    def personalReserves(self):
        ...
    @staticmethod
    def getPersonalReservesType():
        ...
    @property
    def playerList(self):
        ...
    @staticmethod
    def getPlayerListType():
        ...
    def getTabSelection(self):
        ...
    def setTabSelection(self, value):
        ...
    def getShowCommendationAnimations(self):
        ...
    def setShowCommendationAnimations(self, value):
        ...
    def _initialize(self):
        ...
