# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/gsw_cards/quests_card_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import namedtuple as namedtuple
import typing as typing
from cache import cached_property as cached_property
from constants import DailyQuestDecorationMap as DailyQuestDecorationMap
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow, createTooltipData as createTooltipData
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.server_events.awards_formatters import AWARDS_SIZES as AWARDS_SIZES
from gui.server_events.event_items import ServerEventAbstract as ServerEventAbstract
from halloween.gui.game_control.halloween_artefacts_controller import getBonusPriority as getBonusPriority
from halloween.gui.impl.lobby.tooltips.tooltip_positioner import TooltipPositionerMixin as TooltipPositionerMixin
from halloween.skeletons.halloween_anomalies_controller import IHalloweenAnomaliesController as IHalloweenAnomaliesController
from halloween.skeletons.halloween_artefacts_controller import IHalloweenArtefactsController as IHalloweenArtefactsController
from halloween.skeletons.halloween_controller import IHalloweenController as IHalloweenController
from helpers import dependency as dependency
from halloween.gui.impl.lobby.hw_helpers import getQuestSmallestFinishTimeLeft as getQuestSmallestFinishTimeLeft, fillBaseBonusProperties as fillBaseBonusProperties, getHWMetaAwardFormatter as getHWMetaAwardFormatter, PROMINENT_REWARD_TOOLTIP_ID as PROMINENT_REWARD_TOOLTIP_ID, HalloweenBonusesAwardsComposer as HalloweenBonusesAwardsComposer, INF_DISPLAY_BONUSES as INF_DISPLAY_BONUSES
from halloween.gui.impl.lobby.tooltips.daily_quests_tooltip import DailyQuestsTooltip as DailyQuestsTooltip
from gui.impl.gen import R as R
from gui.server_events.cond_formatters import postbattle as postbattleFrmt, bonus as bonusFrmt
from gui.Scaleform.genConsts.MISSIONS_ALIASES import MISSIONS_ALIASES as MISSIONS_ALIASES
from gui.shared.utils.scheduled_notifications import SimpleNotifier as SimpleNotifier
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from halloween.gui.impl.gen.view_models.views.lobby.widgets.quests_card_view_model import QuestsCardViewModel as QuestsCardViewModel
from halloween.gui.impl.gen.view_models.views.lobby.widgets.quests_list_view_model import QuestsListViewModel as QuestsListViewModel
from typing import Optional as Optional
from frameworks.wulf import View as View, Window as Window, ViewEvent as ViewEvent
from gui.server_events.awards_formatters import QuestsBonusComposer as QuestsBonusComposer
from gui.server_events.event_items import Quest as Quest
from halloween_common.configs.halloween_gsw import CardModel as CardModel
_logger: Any
QuestData: Any

# base nao representavel no stub: ViewComponent[...]
class QuestsCardPresenter(TooltipPositionerMixin):
    _hwArtifactsCtrl: Any
    _hwAnomaliesCtrl: Any
    _halloweenCtrl: Any
    _itemsCache: Any
    _eventsCache: Any
    __postBattleCondFormatter: Any
    __bonusCondFormatter: Any
    __statusChangeNotifier: Any
    __quests: Any
    __isGSW: Any
    def __init__(self, isGSW=False):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def _fullRefresh(self):
        ...
    def __getTimeToStatusChange(self):
        ...
    @staticmethod
    def __validateQuest(quest):
        ...
    def __checkTokenCondition(self, card):
        ...
    def __getActualQuest(self, card):
        ...
    # decorador original: @cached_property
    def __bonusFormatter(self):
        ...
    def __getQuestBonus(self, quest):
        ...
    def __refreshData(self):
        ...
    @staticmethod
    def __getFirstConditionIcon(quest, formatter):
        ...
    def __getFirstBonusConditionCumulativeProgress(self, quest):
        ...
    def __refreshModel(self):
        ...
