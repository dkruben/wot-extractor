# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/vehicle_compare/consumable.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.Scaleform.daapi.view.lobby.vehicle_compare import cmp_helpers as cmp_helpers
from gui.impl.lobby.tank_setup.array_providers.consumable import ConsumableDeviceProvider as ConsumableDeviceProvider
from gui.impl.lobby.tank_setup.configurations.consumable import ConsumableTabsController as ConsumableTabsController, ConsumableTabs as ConsumableTabs
from gui.impl.lobby.vehicle_compare.base_sub_view import CompareBaseSetupSubView as CompareBaseSetupSubView

class CompareConsumableDeviceProvider(ConsumableDeviceProvider):
    def _fillStatus(self, model, item, slotID):
        ...
    def _fillBuyPrice(self, *args, **kwargs):
        ...
    def _fillBuyStatus(self, model, item, isInstalledOrMounted):
        ...

class _CompareConsumableTabsController(ConsumableTabsController):
    def _getAllProviders(self):
        ...

class CompareConsumableSetupSubView(CompareBaseSetupSubView):
    def _createTabsController(self):
        ...
