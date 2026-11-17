# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/holiday_final_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum, IntEnum as IntEnum
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.awards_widget_model import AwardsWidgetModel as AwardsWidgetModel
from gui.impl.gen.view_models.views.lobby.battle_pass.battle_pass_buy_rewards_view_model import BattlePassBuyRewardsViewModel as BattlePassBuyRewardsViewModel

class ChapterStates(IntEnum):
    ACTIVE = 0
    PAUSED = 1
    COMPLETED = 2
    NOTSTARTED = 3

class FinalRewardTypes(Enum):
    VEHICLE = 'vehicle'
    STYLE = 'style'
    TANKMAN = 'tankman'

class HolidayFinalViewModel(ViewModel):
    __slots__: tuple
    BUY_STATE = 'buyState'
    REWARDS_STATE = 'rewardsState'
    TANKMEN_STATE = 'tankmenState'
    SELECTABLE_REWARDS_STATE = 'selectableRewardsState'
    FINAL_STATE = 'finalState'
    onTakeRewardsClick: Any
    showTankmen: Any
    onPreviewVehicle: Any
    showHangar: Any
    onClose: Any
    def __init__(self, properties=10, commands=5):
        ...
    @property
    def rewards(self):
        ...
    @staticmethod
    def getRewardsType():
        ...
    @property
    def awardsWidget(self):
        ...
    @staticmethod
    def getAwardsWidgetType():
        ...
    def getState(self):
        ...
    def setState(self, value):
        ...
    def getNotChosenRewardCount(self):
        ...
    def setNotChosenRewardCount(self, value):
        ...
    def getIsChooseRewardsEnabled(self):
        ...
    def setIsChooseRewardsEnabled(self, value):
        ...
    def getChapterID(self):
        ...
    def setChapterID(self, value):
        ...
    def getCurrentLevel(self):
        ...
    def setCurrentLevel(self, value):
        ...
    def getChapterState(self):
        ...
    def setChapterState(self, value):
        ...
    def getFinalRewardType(self):
        ...
    def setFinalRewardType(self, value):
        ...
    def getIsSeasonEndingSoon(self):
        ...
    def setIsSeasonEndingSoon(self, value):
        ...
    def _initialize(self):
        ...
