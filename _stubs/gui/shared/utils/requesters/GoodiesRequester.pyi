# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/utils/requesters/GoodiesRequester.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from future.utils import iteritems as iteritems
import BigWorld as BigWorld
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester as AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IGoodiesRequester as IGoodiesRequester
GoodieVariable: Any

# base nao representavel no stub: namedtuple(...)
class _ClanReserveInfo:
    __slots__: tuple
    def __new__(cls, finishTime, value, duration=3600):
        ...

class GoodiesRequester(AbstractSyncDataRequester, IGoodiesRequester):
    def _requestCache(self, callback=None):
        ...
    @property
    def goodies(self):
        ...
    def getActiveClanReserves(self):
        ...
    def _preprocessValidData(self, data):
        ...
