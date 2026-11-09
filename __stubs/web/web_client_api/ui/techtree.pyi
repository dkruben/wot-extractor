# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/ui/techtree.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from helpers import dependency as dependency
from gui.shared import event_dispatcher as event_dispatcher
from skeletons.gui.shared import IItemsCache as IItemsCache
from web.web_client_api import W2CSchema as W2CSchema, w2c as w2c, Field as Field

class _OpenTechTreeSchema(W2CSchema):
    vehicle_id: Any

class TechTreeTabWebApiMixin(object):
    itemsCache: Any
    # decorador original: @w2c(...)
    def openTechTree(self, cmd):
        ...
    # decorador original: @w2c(...)
    def openResearch(self, cmd):
        ...
    # decorador original: @w2c(...)
    def openVehicleHubOverview(self, cmd):
        ...
