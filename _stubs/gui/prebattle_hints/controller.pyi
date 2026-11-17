# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prebattle_hints/controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import importlib as importlib
import random as random
from logging import getLogger as getLogger
import typing as typing
from Event import Event as Event
from gui.shared import g_eventBus as g_eventBus, events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.event_dispatcher import showPrebattleHintsWindow as showPrebattleHintsWindow
from helpers import dependency as dependency
from hints_common.prebattle.manager import getInstance as getInstance
from hints_common.prebattle.schemas import BaseHintModel as BaseHintModel, configSchema as configSchema
from skeletons.gameplay import IGameplayLogic as IGameplayLogic, GameplayStateID as GameplayStateID
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.prebattle_hints.controller import IPrebattleHintsController as IPrebattleHintsController, IPrebattleHintsControlStrategy as IPrebattleHintsControlStrategy
from soft_exception import SoftException as SoftException
_logger: Any

class PrebattleHintsController(IPrebattleHintsController):
    __sessionProvider: Any
    __gameplayLogic: Any
    __strategies: Any
    __defaultStrategy: Any
    __hasHintToShow: Any
    _hintsClosed: Any
    def __init__(self):
        ...
    def fini(self):
        ...
    def isEnabled(self):
        ...
    def isEnabledForCurrentBattleSession(self):
        ...
    def addControlStrategy(self, arenaBonusType, strategy):
        ...
    def removeControlStrategy(self, arenaBonusTypes):
        ...
    def onShowHintsWindowSuccess(self, hint):
        ...
    def __getControlStrategy(self, arenaBonusType):
        ...
    def __handleBattleLoading(self, event):
        ...
    def __showHintsWindow(self):
        ...
    def __onBattleSessionStart(self):
        ...
    def __onBattleSessionStop(self):
        ...

class DefaultControlStrategy(IPrebattleHintsControlStrategy):
    def hasHintToShow(self, arenaBonusType):
        ...
    def getHintToShow(self, arenaBonusType):
        ...
    def onShowHintsWindowSuccess(self, hint):
        ...
