# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/gsw_cards/quests_card_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import constants as constants
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow, createTooltipData as createTooltipData
from gui.impl.lobby.user_missions.hangar_widget.presenters.base_child_presenter import UserMissionChildPresenter as UserMissionChildPresenter
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.server_events import IEventsCache as IEventsCache
from gui.server_events.event_items import ServerEventAbstract as ServerEventAbstract
from helpers import dependency as dependency, time_utils as time_utils
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from last_stand.gui.impl.lobby.ls_helpers import getQuestFinishTimeLeft as getQuestFinishTimeLeft, fillRewards as fillRewards
from last_stand.gui.impl.lobby.tooltips.daily_quests_tooltip import DailyQuestsTooltip as DailyQuestsTooltip
from last_stand.gui.impl.lobby.tooltips.points_tooltip import PointsTooltipView as PointsTooltipView
from shared_utils import first as first
from gui.impl.gen import R as R
from gui.server_events.cond_formatters import postbattle as postbattleFrmt, bonus as bonusFrmt
from gui.Scaleform.genConsts.MISSIONS_ALIASES import MISSIONS_ALIASES as MISSIONS_ALIASES
from gui.shared.utils.scheduled_notifications import SimpleNotifier as SimpleNotifier
from last_stand.gui.impl.gen.view_models.views.lobby.widgets.quests_view_model import QuestsViewModel as QuestsViewModel
from last_stand.gui.shared.event_dispatcher import showRewardPathView as showRewardPathView
from last_stand_common.last_stand_constants import DailyMissionsSettings as DailyMissionsSettings
from last_stand.skeletons.ls_quests_ui_cache import ILSQuestsUICache as ILSQuestsUICache
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from last_stand.skeletons.ls_controller import ILSController as ILSController
from frameworks.wulf import View as View, ViewEvent as ViewEvent
from gui.server_events.parsers import BonusConditions as BonusConditions
_R_BACKPORT_TOOLTIP: Any

# base nao representavel no stub: ViewComponent[...]
class QuestsCardPresenter(UserMissionChildPresenter):
    __questsCache: Any
    __eventsCache: Any
    __lsCtrl: Any
    _MAX_BONUSES_IN_VIEW = 5
    __postBattleCondFormatter: Any
    __bonusCondFormatter: Any
    __statusChangeNotifier: Any
    __quest: Any
    __allDailyCompleted: Any
    __bonusCache: Any
    __idGen: Any
    def __init__(self):
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
    def _getCallbacks(self):
        ...
    def _init(self):
        ...
    def __onClick(self):
        ...
    def __onMarkAsViewed(self):
        ...
    def __onSyncQuestCompleted(self):
        ...
    def __onTokensUpdated(self, diff):
        ...
    def __onNotifyStatusChange(self):
        ...
    def __getTimeToStatusChange(self):
        ...
    def __getActiveQuest(self, checker):
        ...
    def __getFirstConditionIcon(self, quest, questConditions, formatter):
        ...
    def _getFirstConditionKeyName(self, questConditions):
        ...
    def __getFirstBonusConditionCumulativeProgress(self, quest):
        ...
    def __fillViewModel(self, quest):
        ...
    def __initQuest(self):
        ...
    @staticmethod
    def __isDailyQuest(questID):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __setWidgetState(self, isHidden, model=None):
        ...
