# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/configurations/shell.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.impl.common.tabs_controller import tabUpdateFunc as tabUpdateFunc
from gui.impl.lobby.tank_setup.array_providers.shell import ShellProvider as ShellProvider
from gui.impl.lobby.tank_setup.configurations.base import BaseTankSetupTabsController as BaseTankSetupTabsController, BaseDealPanel as BaseDealPanel

class ShellTabs(object):
    SHELLS = 'shells'
    ALL: tuple

class ShellTabsController(BaseTankSetupTabsController):
    __slots__: tuple
    def getDefaultTab(self):
        ...
    # decorador original: @tabUpdateFunc(...)
    def _updateDefault(self, viewModel, isFirst=False):
        ...
    def _getAllProviders(self):
        ...

class ShellDealPanel(BaseDealPanel):
    @classmethod
    def addItem(cls, vehicle, item, prices):
        ...
