# wot-extractor: STUB (.pyi) gerado a partir de sources/res/resource_well/scripts/client/resource_well/gui/feature/resource_well_sync_data.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import Dict as Dict
from account_helpers import AccountSyncData as AccountSyncData
from resource_well_common.feature_constants import RESOURCE_WELL_PDATA_KEY as RESOURCE_WELL_PDATA_KEY
from shared_utils.account_helpers.diff_utils import synchronizeDicts as synchronizeDicts

class ResourceWellSyncData(object):
    __cache: Any
    def __init__(self):
        ...
    def clear(self):
        ...
    def getSeason(self):
        ...
    def getCurrentPoints(self):
        ...
    def getBalance(self):
        ...
    def getReward(self):
        ...
    def getCurrentRewardID(self):
        ...
    def getInitialNumberAmounts(self):
        ...
    def update(self, clientDiff):
        ...
