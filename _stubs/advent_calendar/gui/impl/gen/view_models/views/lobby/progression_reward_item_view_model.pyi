# wot-extractor: STUB (.pyi) gerado a partir de sources/res/advent_calendar/scripts/client/advent_calendar/gui/impl/gen/view_models/views/lobby/progression_reward_item_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class ProgressionState(Enum):
    REWARD_RECEIVED = 'rewardReceived'
    REWARD_IN_PROGRESS = 'rewardInProgress'
    REWARD_LOCKED = 'rewardLocked'

class RewardType(Enum):
    STYLE_2D = 'style2D'
    CREW_MEMBER = 'crewMember'
    BIG_LOOTBOX = 'lootBox'

class ProgressionRewardItemViewModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=6, commands=0):
        ...
    def getRequiredOpenedDoorsAmount(self):
        ...
    def setRequiredOpenedDoorsAmount(self, value):
        ...
    def getActualOpenedDoorsAmount(self):
        ...
    def setActualOpenedDoorsAmount(self, value):
        ...
    def getState(self):
        ...
    def setState(self, value):
        ...
    def getTooltipId(self):
        ...
    def setTooltipId(self, value):
        ...
    def getTooltipContentId(self):
        ...
    def setTooltipContentId(self, value):
        ...
    def getRewardType(self):
        ...
    def setRewardType(self, value):
        ...
    def _initialize(self):
        ...
