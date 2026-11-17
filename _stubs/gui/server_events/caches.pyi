# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/server_events/caches.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
_g_navInfo = None

class _NavigationInfo(object):
    tabID: Any
    _missionsTab: Any
    _marathonPrefix: Any
    _vehicleSelectorFilters: Any
    def __init__(self):
        ...
    def getMissionsTab(self):
        ...
    def getMarathonPrefix(self):
        ...
    def setMissionsTab(self, tabID):
        ...
    def setMarathonPrefix(self, marathonPrefix):
        ...
    def getVehicleSelectorFilters(self):
        ...
    def setVehicleSelectorFilters(self, filters):
        ...

def getNavInfo():
    ...
def clearNavInfo():
    ...
