# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/prime_time_servers_data_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.gen import R as R
from gui.impl import backport as backport
from gui.Scaleform.daapi.view.servers_data_provider import ServersDataProvider as ServersDataProvider

class PrimeTimesServersDataProvider(ServersDataProvider):
    primeTimes: Any
    __maxPeriodLen: Any
    def __init__(self, primeTimesForDay):
        ...
    def updatePrimeTimes(self, primeTimesForDay):
        ...
    def getDefaultSelectedServer(self, serversList):
        ...
    def _makeVO(self, index, item):
        ...
    def __getMaxPrimeTimes(self):
        ...
