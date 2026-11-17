# wot-extractor: STUB (.pyi) gerado a partir de sources/res/open_bundle/scripts/client/open_bundle/helpers/sync_data.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from account_helpers import AccountSyncData as AccountSyncData
from open_bundle_common.constants import OPEN_BUNDLE_PDATA_KEY as OPEN_BUNDLE_PDATA_KEY
from shared_utils.account_helpers.diff_utils import synchronizeDicts as synchronizeDicts
from typing import Dict as Dict

class OpenBundleSyncData(object):
    __cache: Any
    def __init__(self):
        ...
    def clear(self):
        ...
    def update(self, clientDiff):
        ...
    def getTrackedByNameSections(self, bundleID):
        ...
