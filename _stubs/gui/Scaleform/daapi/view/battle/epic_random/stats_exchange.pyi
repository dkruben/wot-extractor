# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/epic_random/stats_exchange.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.Scaleform.daapi.view.battle.classic.stats_exchange import ClassicStatisticsDataController as ClassicStatisticsDataController, DynamicVehicleStatsComponent as DynamicVehicleStatsComponent
from gui.Scaleform.daapi.view.battle.shared.stats_exchange import createExchangeBroker as createExchangeBroker
from gui.Scaleform.daapi.view.battle.shared.stats_exchange import broker as broker
from gui.Scaleform.daapi.view.battle.shared.stats_exchange import vehicle as vehicle
from gui.battle_control.arena_info.arena_vos import EPIC_RANDOM_KEYS as EPIC_RANDOM_KEYS

class EpicRandomVehicleInfoComponent(vehicle.VehicleInfoComponent):
    def addVehicleInfo(self, vInfoVO, overrides):
        ...

class EpicRandomStatisticsDataController(ClassicStatisticsDataController):
    def _createExchangeBroker(self, exchangeCtx):
        ...
