# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/shared/missions/packers/events.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.pages.quest_card_model import QuestCardModel as QuestCardModel, CardState as CardState
from comp7.gui.impl.gen.view_models.views.lobby.weekly_quest_model import WeeklyQuestModel as WeeklyQuestModel
from comp7.gui.impl.lobby.comp7_helpers.account_settings import getLastSeenQuestData as getLastSeenQuestData
from gui.impl.gen.view_models.common.missions.conditions.condition_group_model import ConditionGroupModel as ConditionGroupModel
from gui.impl.gen.view_models.common.missions.conditions.preformatted_condition_model import PreformattedConditionModel as PreformattedConditionModel
from gui.periodic_battles.models import PeriodType as PT
from gui.shared.missions.packers.conditions import BonusConditionPacker as BonusConditionPacker, PostBattleConditionPacker as PostBattleConditionPacker
from gui.shared.missions.packers.events import findFirstConditionModel as findFirstConditionModel
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from typing import Optional as Optional, Tuple as Tuple
from gui.server_events.event_items import Quest as Quest

class Comp7WeeklyQuestPacker(object):
    __comp7Controller: Any
    __slots__: tuple
    __isUnavailablePeriod: Any
    __isComp7Available: Any
    __hasSuitableVehicles: Any
    def __init__(self):
        ...
    def pack(self, quest):
        ...
    @staticmethod
    def getData(quest):
        ...
    def __getQuestState(self, quest):
        ...

class Comp7WeeklyQuestWidgetPacker(Comp7WeeklyQuestPacker):
    def pack(self, quest):
        ...

class Comp7TokenQuestPacker(object):
    @staticmethod
    def getData(quest):
        ...
