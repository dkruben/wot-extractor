# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/feature/models/common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin as FunAssetPacksMixin
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.periodic_battles.models import PeriodInfo as PeriodInfo
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from season_common import GameSeason as GameSeason

# decorador original: @ReprInjector.simple(...)
class FunSubModesStatus(object):
    __slots__: tuple
    rightBorder: Any
    primeDelta: Any
    endTime: Any
    state: Any
    def __init__(self, state, rightBorder=None, primeDelta=None, endTime=None):
        ...

class FunRandomSeason(GameSeason):
    __assetsPointer: Any
    def __init__(self, cycleInfo, seasonData, assetsPointer):
        ...
    def getUserName(self):
        ...

class FunPeriodInfo(PeriodInfo, FunAssetPacksMixin):
    def getVO(self, withBNames=False, withBDeltas=False, deltaFmt=None, timeFmt=None, dateFmt=None):
        ...
