# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/dossier/achievements/abstract/mixins/HasVehicleList.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from gui import nationSortKeyByIndex as nationSortKeyByIndex
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache

class HasVehiclesList(object):
    _LIST_NAME = 'vehicles'
    VehicleData: Any
    itemsCache: Any
    def getVehiclesData(self):
        ...
    @classmethod
    def getVehiclesListTitle(cls):
        ...
    def _getVehiclesDescrsList(self):
        ...
    def hasVehiclesList(self):
        ...
    @classmethod
    def _sortKey(cls, v):
        ...
