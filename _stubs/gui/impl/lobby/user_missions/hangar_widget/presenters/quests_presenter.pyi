# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/user_missions/hangar_widget/presenters/quests_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.user_missions.widget.quests_list_model import QuestsListModel as QuestsListModel
from gui.impl.gen.view_models.views.lobby.user_missions.widget.widget_quest_model import WidgetQuestModel as WidgetQuestModel
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.common.tooltips.extended_text_tooltip import ExtendedTextTooltip as ExtendedTextTooltip
from gui.impl.lobby.user_missions.hangar_widget.overlap_ctrl import OverlapCtrlMixin as OverlapCtrlMixin
from gui.impl.lobby.user_missions.hangar_widget.presenters.constants import UserMissionGroups as UserMissionGroups
from gui.impl.lobby.user_missions.hangar_widget.providers.user_mission_item import MissionItem as MissionItem
from gui.impl.lobby.user_missions.hangar_widget.presenters.base_child_presenter import UserMissionChildPresenter as UserMissionChildPresenter
from gui.impl.lobby.user_missions.hangar_widget.services import IMissionsService as IMissionsService
from gui.impl.lobby.user_missions.hangar_widget.tooltip_positioner import TooltipPositionerMixin as TooltipPositionerMixin
from gui.impl.lobby.user_missions.hangar_widget.user_misson_controller import MissionController as MissionController
from gui.impl.lobby.user_missions.hangar_widget.utils import getCountdown as getCountdown
from gui.impl.lobby.user_missions.tooltips.all_quests_done_tooltip import AllQuestsDoneTooltip as AllQuestsDoneTooltip
from gui.impl.lobby.user_missions.tooltips.quest_tooltip import DailyQuestTooltip as DailyQuestTooltip, WeeklyQuestTooltip as WeeklyQuestTooltip
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.server_events.events_dispatcher import showDailyQuests as showDailyQuests
from gui.shared.missions.packers.events import packQuestBonusModel as packQuestBonusModel
from helpers import dependency as dependency
from shared_utils import findFirst as findFirst
from skeletons.gui.server_events import IEventsCache as IEventsCache

# base nao representavel no stub: ViewComponent[...]
class QuestsPresenter(UserMissionChildPresenter, TooltipPositionerMixin, OverlapCtrlMixin, IGlobalListener):
    GROUP = UserMissionGroups.MISSIONS
    eventsCache: Any
    missionsService: Any
    _missionController: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def isVisible(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _getQuestFromEvent(self, event):
        ...
    def onPrbEntitySwitched(self):
        ...
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    def _onMissionsChanged(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _onChanged(self):
        ...
    def _updateCurrentMissionCountDown(self, missionItem):
        ...
    def _rawUpdate(self):
        ...
    def _updateViewModel(self):
        ...
    def _getModel(self, data):
        ...
    def _packBonuses(self, model, data, bonusPacker, sortKey):
        ...
    # decorador original: @args2params(...)
    def __onMissionClick(self, questId):
        ...
    def __onMarkAsViewed(self):
        ...
