# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/common/comp7_ranks_common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import total_ordering as total_ordering
from past.builtins import cmp as cmp
from typing import Optional as Optional, FrozenSet as FrozenSet, Tuple as Tuple, Dict as Dict
from cache import cached_property as cached_property
from intervals import Interval as Interval
from soft_exception import SoftException as SoftException
EXTRA_RANK_TAG = 'extra'
COMP7_UNDEFINED_RANK_ID = 0
COMP7_UNDEFINED_DIVISION_ID = 0
COMP7_UNDEFINED_DIVISION_SERIAL_IDX = 0

# decorador original: @total_ordering
class Comp7Division(object):
    __slots__: tuple
    range: Any
    rank: Any
    dvsnID: Any
    index: Any
    tags: Any
    activityPointsPerBattle: Any
    ratingPointsPenalty: Any
    hasRankInactivity: Any
    seasonPoints: Any
    serialIdx: Any
    def __init__(self, serialIdx, divisionInfo):
        ...
    def __eq__(self, other):
        ...
    def __lt__(self, other):
        ...
    def __hash__(self):
        ...
    def __compare(self, other):
        ...
    def __repr__(self):
        ...

class Comp7Rank(object):
    __slots__: tuple
    id: Any
    name: Any
    def __init__(self, rankDict):
        ...
    @property
    def index(self):
        ...

class Comp7RanksConfig(object):
    _config: Any
    def __init__(self, config):
        ...
    # decorador original: @cached_property
    def businessDayStartHour(self):
        ...
    # decorador original: @cached_property
    def divisions(self):
        ...
    # decorador original: @cached_property
    def ranks(self):
        ...
    def getDivisionByRating(self, points, hasEliteEntitlement):
        ...
    def getStartRatingForDivision(self, divisionSerialIdx):
        ...
    # decorador original: @cached_property
    def eliteDivision(self):
        ...
    def getActivityPointsForBattle(self, rank, divisionIdx):
        ...
