# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/battle/battle_page/prebattle_ammunition_panel_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import IntEnum as IntEnum
from gui.impl.gen.view_models.views.battle.battle_page.prebattle_ammunition_panel_model import PrebattleAmmunitionPanelModel as PrebattleAmmunitionPanelModel
from gui.impl.gen.view_models.views.lobby.tank_setup.ammunition_panel_view_model import AmmunitionPanelViewModel as AmmunitionPanelViewModel

class State(IntEnum):
    BATTLELOADING = 0
    PREBATTLE = 1
    PREBATTLENOTCONFIRMED = 2

class PrebattleAmmunitionPanelViewModel(AmmunitionPanelViewModel):
    __slots__: tuple
    def __init__(self, properties=10, commands=1):
        ...
    @property
    def ammunitionPanel(self):
        ...
    @staticmethod
    def getAmmunitionPanelType():
        ...
    def getTimeTillBattleStart(self):
        ...
    def setTimeTillBattleStart(self, value):
        ...
    def getState(self):
        ...
    def setState(self, value):
        ...
    def _initialize(self):
        ...
