# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/tank_setup/array_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.lobby.tank_setup.array_providers.consumable import ConsumableDeviceProvider as ConsumableDeviceProvider
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from gui.impl import backport as backport
from gui.impl.gen import R as R

class HalloweenConsumableProvider(ConsumableDeviceProvider):
    INCLUDE_TAGS: Any
    EXCLUDE_TAGS: Any
    def createSlot(self, item, ctx):
        ...
    def _getItemCriteria(self):
        ...
