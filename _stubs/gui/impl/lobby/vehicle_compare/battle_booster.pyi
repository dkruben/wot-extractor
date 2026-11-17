# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/vehicle_compare/battle_booster.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.impl.gen.view_models.constants.item_highlight_types import ItemHighlightTypes as ItemHighlightTypes
from gui.impl.lobby.tank_setup.array_providers.battle_booster import OptDeviceBattleBoosterProvider as OptDeviceBattleBoosterProvider, CrewBattleBoosterProvider as CrewBattleBoosterProvider
from gui.impl.lobby.tank_setup.configurations.battle_booster import BattleBoostersTabsController as BattleBoostersTabsController, BattleBoosterTabs as BattleBoosterTabs
from gui.impl.lobby.vehicle_compare.base_sub_view import CompareBaseSetupSubView as CompareBaseSetupSubView
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA

class _CompareOptDeviceBattleBoosterProvider(OptDeviceBattleBoosterProvider):
    def _fillBuyPrice(self, *args, **kwargs):
        ...
    def _fillBuyStatus(self, *args, **kwargs):
        ...
    def _getItemCriteria(self):
        ...

class _CompareCrewBattleBoosterProvider(CrewBattleBoosterProvider):
    def _fillBuyPrice(self, *args, **kwargs):
        ...
    def _fillBuyStatus(self, *args, **kwargs):
        ...
    def _fillHighlights(self, model, item):
        ...

class _CompareBattleBoostersTabsController(BattleBoostersTabsController):
    def _getAllProviders(self):
        ...

class CompareBattleBoosterSetupSubView(CompareBaseSetupSubView):
    def _createTabsController(self):
        ...
