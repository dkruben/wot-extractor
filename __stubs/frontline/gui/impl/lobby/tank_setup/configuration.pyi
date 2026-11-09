# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/impl/lobby/tank_setup/configuration.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frontline.gui.impl.lobby.tank_setup.array_provider import BattleAbilityProvider as BattleAbilityProvider
from gui.impl.common.tabs_controller import tabUpdateFunc as tabUpdateFunc
from gui.impl.lobby.tank_setup.configurations.base import BaseTankSetupTabsController as BaseTankSetupTabsController, BaseDealPanel as BaseDealPanel

class EpicBattleTabs(object):
    BATTLE_ABILITY = 'battleAbility'
    ALL: tuple

class EpicBattleTabsController(BaseTankSetupTabsController):
    __slots__: tuple
    def getDefaultTab(self):
        ...
    # decorador original: @tabUpdateFunc(...)
    def _updateOptDevice(self, viewModel, isFirst=False):
        ...
    def tabOrderKey(self, tabName):
        ...
    def _getAllProviders(self):
        ...

class EpicBattleDealPanel(BaseDealPanel):
    @classmethod
    def updateDealPanelPrice(cls, vehicle, items, dealPanelModel):
        ...
