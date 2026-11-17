# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/battle/battle_notifier/battle_notifier_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import deque as deque
import ArenaType as ArenaType
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from helpers import dependency as dependency
from items.vehicles import getVehicleType as getVehicleType, getVehicleClassFromVehicleType as getVehicleClassFromVehicleType
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.battle.battle_notifier.battle_notifier_view_model import BattleNotifierViewModel as BattleNotifierViewModel, ResultEnum as ResultEnum
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.money import Currency as Currency
from skeletons.gameplay import IGameplayLogic as IGameplayLogic
_logger: Any
_formatters: dict

class BattleNotifierView(ViewImpl):
    __slots__: tuple
    __resultsQueue: Any
    __uiReadyForData: Any
    __arenaLoaded: Any
    __prebattleStateReached: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def arenaLoadCompleted(self):
        ...
    def addBattleResults(self, message):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _sendNotificationData(self):
        ...
    def _fillComponentModel(self):
        ...
    def __onPrebattleStateReached(self, _=None, __=None):
        ...
    def __onResultShown(self):
        ...

def _randomBattleResults(message):
    ...
def _collectResults(message):
    ...
