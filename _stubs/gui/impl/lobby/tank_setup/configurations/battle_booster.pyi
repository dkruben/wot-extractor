# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/configurations/battle_booster.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.impl.common.tabs_controller import tabUpdateFunc as tabUpdateFunc
from gui.impl.lobby.tank_setup.array_providers.battle_booster import OptDeviceBattleBoosterProvider as OptDeviceBattleBoosterProvider, CrewBattleBoosterProvider as CrewBattleBoosterProvider
from gui.impl.lobby.tank_setup.configurations.base import BaseTankSetupTabsController as BaseTankSetupTabsController

class BattleBoosterTabs(object):
    OPT_DEVICE = 'optDevice'
    CREW = 'crew'
    ALL: tuple

class BattleBoostersTabsController(BaseTankSetupTabsController):
    __slots__: tuple
    def getDefaultTab(self):
        ...
    # decorador original: @tabUpdateFunc(...)
    def _updateOptDevice(self, viewModel, isFirst=False):
        ...
    # decorador original: @tabUpdateFunc(...)
    def _updateCrew(self, viewModel, isFirst=False):
        ...
    def tabOrderKey(self, tabName):
        ...
    def _getAllProviders(self):
        ...
