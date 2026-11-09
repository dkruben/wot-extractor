# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/weekly_quests_widget_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from comp7.gui.impl.gen.view_models.views.lobby.enums import MetaRootViews as MetaRootViews
from comp7.gui.impl.gen.view_models.views.lobby.weekly_quests_widget_model import WeeklyQuestsWidgetModel as WeeklyQuestsWidgetModel, State as State
from comp7.gui.impl.lobby.comp7_helpers.account_settings import setLastSeenQuestData as setLastSeenQuestData, getLastSeenQuestData as getLastSeenQuestData
from comp7.gui.impl.lobby.comp7_helpers.comp7_bonus_packer import getComp7BonusPacker as getComp7BonusPacker, packQuestBonuses as packQuestBonuses
from comp7.gui.impl.lobby.comp7_helpers.comp7_quest_helpers import isWeeklyRewardClaimed as isWeeklyRewardClaimed
from comp7.gui.impl.lobby.tooltips.weekly_quest_widget_tooltip import WeeklyQuestWidgetTooltip as WeeklyQuestWidgetTooltip
from comp7.gui.impl.lobby.user_missions.hangar_widget.overlap_ctrl import Comp7OverlapCtrlMixin as Comp7OverlapCtrlMixin
from comp7.gui.shared.event_dispatcher import showComp7MetaRootTab as showComp7MetaRootTab, showComp7WeeklyQuestsRewardsSelectionWindow as showComp7WeeklyQuestsRewardsSelectionWindow
from comp7.gui.shared.missions.packers.events import Comp7WeeklyQuestWidgetPacker as Comp7WeeklyQuestWidgetPacker
from comp7.skeletons.gui.game_control import IComp7WeeklyQuestsController as IComp7WeeklyQuestsController
from gui.impl.gen import R as R
from gui.impl.lobby.common.tooltips.extended_text_tooltip import ExtendedTextTooltip as ExtendedTextTooltip
from gui.impl.lobby.user_missions.hangar_widget.tooltip_positioner import TooltipPositionerMixin as TooltipPositionerMixin
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from helpers import dependency as dependency
from frameworks.wulf import Array as Array
from helpers.time_utils import getServerUTCTime as getServerUTCTime
from skeletons.gui.server_events import IEventsCache as IEventsCache
from frameworks.wulf.view.array import fillViewModelsArray as fillViewModelsArray
from gui.server_events.event_items import Quest as Quest

# base nao representavel no stub: ViewComponent[...]
class WeeklyQuestsWidgetPresenter(TooltipPositionerMixin, Comp7OverlapCtrlMixin, IGlobalListener):
    __eventsCache: Any
    __comp7WeeklyQuestsCtrl: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _updateViewModel(self):
        ...
    def _getEvents(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _finalize(self):
        ...
    def __onWeeklyQuestsUpdated(self, _):
        ...
    def _rawUpdate(self):
        ...
    def __updateQuestData(self, quest, questNumber):
        ...
    def __getQuestsState(self):
        ...
    def __onMarkAsViewed(self):
        ...
    @staticmethod
    def __setPrevQuestData(quest):
        ...
    @staticmethod
    def __onGoToWeeklyQuests():
        ...
    @staticmethod
    def __onGoToRewardsSelection():
        ...
    def __onPollServerTime(self):
        ...
