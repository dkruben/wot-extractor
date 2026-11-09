# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/battle_control/controllers/battle_royale_appearance_cache_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import BigWorld as BigWorld
from gui.battle_control.controllers.appearance_cache_ctrls import getWholeVehModels as getWholeVehModels
from gui.battle_control.controllers.appearance_cache_ctrls.default_appearance_cache_ctrl import DefaultAppearanceCacheController as DefaultAppearanceCacheController
from items.vehicles import VehicleDescriptor as VehicleDescriptor

class BattleRoyaleAppearanceCacheController(DefaultAppearanceCacheController):
    FORCED_CACHED_VEHICLES: tuple
    EQUIPMENT_VEHICLES: tuple
    def arenaLoadCompleted(self):
        ...
    def _precacheExtraResources(self):
        ...
