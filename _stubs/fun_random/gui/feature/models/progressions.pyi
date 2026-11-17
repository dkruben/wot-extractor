# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/feature/models/progressions.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from fun_random.gui.feature.fun_constants import PROGRESSION_COUNTER_TEMPLATE as PROGRESSION_COUNTER_TEMPLATE, PROGRESSION_UNLIMITED_COUNTER_TEMPLATE as PROGRESSION_UNLIMITED_COUNTER_TEMPLATE
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from helpers import dependency as dependency, time_utils as time_utils
from shared_utils import findFirst as findFirst
from skeletons.gui.game_control import IFunRandomController as IFunRandomController
from fun_random.helpers.server_settings import FunProgressionConfig as FunProgressionConfig
from gui.server_events.bonuses import SimpleBonus as SimpleBonus
from gui.server_events.event_items import Quest as Quest
from fun_random.gui.server_events.event_items import FunProgressionTriggerQuest as FunProgressionTriggerQuest

# decorador original: @ReprInjector.simple(...)
class FunProgressionConditions(object):
    __counter: Any
    __finishTimestamp: Any
    __pConfig: Any
    __triggers: Any
    def __init__(self, pConfig, counter, triggers):
        ...
    @property
    def counter(self):
        ...
    @property
    def triggers(self):
        ...
    @property
    def counterName(self):
        ...
    @property
    def maximumCounter(self):
        ...
    @property
    def finishTimestamp(self):
        ...
    @property
    def text(self):
        ...
    def setCounter(self, counter):
        ...

# decorador original: @ReprInjector.simple(...)
class FunProgressionStage(object):
    __executorID: Any
    __requiredCounter: Any
    __prevRequiredCounter: Any
    __bonuses: Any
    __stageIndex: Any
    def __init__(self, pConfig, index, executor):
        ...
    @property
    def bonuses(self):
        ...
    @property
    def executorID(self):
        ...
    @property
    def prevRequiredCounter(self):
        ...
    @property
    def requiredCounter(self):
        ...
    @property
    def stageIndex(self):
        ...

# decorador original: @ReprInjector.simple(...)
class FunProgressionUnlimitedProgress(object):
    __unlimitedTrigger: Any
    __unlimitedExecutor: Any
    __maximumCounter: Any
    __counterName: Any
    __counter: Any
    def __init__(self, pConfig, trigger, executor, counter):
        ...
    @property
    def bonuses(self):
        ...
    @property
    def unlimitedTrigger(self):
        ...
    @property
    def unlimitedExecutor(self):
        ...
    @property
    def counterName(self):
        ...
    @property
    def counter(self):
        ...
    def setCounter(self, counter):
        ...
    @property
    def maximumCounter(self):
        ...

# decorador original: @ReprInjector.simple(...)
class FunProgressionState(object):
    __pConfig: Any
    __isFirst: Any
    __isLast: Any
    __isCompleted: Any
    __currentStageIndex: Any
    def __init__(self, pConfig, isFirst, isLast, condition, stages):
        ...
    @property
    def isCompleted(self):
        ...
    @property
    def isFirstProgression(self):
        ...
    @property
    def isLastProgression(self):
        ...
    @property
    def currentStageIndex(self):
        ...
    @property
    def maximumStageIndex(self):
        ...
    def updateState(self, condition, stages):
        ...

# decorador original: @ReprInjector.simple(...)
class FunProgression(object):
    __funRandomController: Any
    __conditions: Any
    __pConfig: Any
    __stages: Any
    __state: Any
    __unlimitedProgress: Any
    __resetTimestamp: Any
    __finishTimestamp: Any
    def __init__(self, pConfig, isFirst, isLast, counter, triggers, executors, unlimitedProgress):
        ...
    @property
    def isNotifiable(self):
        ...
    @property
    def activeStage(self):
        ...
    @property
    def conditions(self):
        ...
    @property
    def config(self):
        ...
    @property
    def stages(self):
        ...
    @property
    def state(self):
        ...
    def getAllBonuses(self):
        ...
    def updateCounter(self, counter):
        ...
    @property
    def hasUnlimitedProgression(self):
        ...
    @property
    def isInUnlimitedProgression(self):
        ...
    @property
    def unlimitedProgression(self):
        ...
    @property
    def resetTimestamp(self):
        ...
    def setResetTimestamp(self, timestamp):
        ...
    @property
    def statusTimer(self):
        ...
    @property
    def resetTimer(self):
        ...
