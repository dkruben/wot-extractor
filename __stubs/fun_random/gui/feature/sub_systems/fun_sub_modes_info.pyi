# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/feature/sub_systems/fun_sub_modes_info.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from itertools import chain as chain
from fun_random.gui.feature.fun_constants import FunSubModesState as FunSubModesState, STATE_TO_SINGLE as STATE_TO_SINGLE
from fun_random.gui.feature.util.fun_helpers import mergeIntervals as mergeIntervals
from fun_random.gui.feature.models.common import FunSubModesStatus as FunSubModesStatus
from fun_random.gui.feature.sub_systems.fun_performance_analyzers import PerformanceGroup as PerformanceGroup
from helpers import time_utils as time_utils
from shared_utils import first as first
from skeletons.gui.game_control import IFunRandomController as IFunRandomController
from gui.periodic_battles.models import PeriodType as PeriodType
from fun_random.gui.feature.sub_modes.base_sub_mode import IFunSubMode as IFunSubMode
_INNER_END_PERIODS: tuple
_OUTSIDE_PERIODS: tuple
_NO_BATTLES_PERIODS: Any

class FunSubModesInfo(IFunRandomController.IFunSubModesInfo):
    __subModes: Any
    def __init__(self, subModesHolder):
        ...
    def fini(self):
        ...
    def isAvailable(self):
        ...
    def isEntryPointAvailable(self):
        ...
    def getEventEndDate(self, now=None, subModesIDs=None):
        ...
    def getLeftTimeToPrimeTimesEnd(self, now=None, subModes=None):
        ...
    def getPrimeTimesForDay(self, selectedTime, groupIdentical=False):
        ...
    def getTimeLeftUntilCycleSequenceFinish(self, now=None, subModesIDs=None):
        ...
    def getPerformanceAlertGroup(self, subModesIDs=None):
        ...
    def getSubModesStatus(self, subModesIDs=None):
        ...
