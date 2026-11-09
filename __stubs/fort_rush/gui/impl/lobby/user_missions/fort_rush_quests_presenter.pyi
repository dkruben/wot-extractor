# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/user_missions/fort_rush_quests_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from fort_rush.gui.impl.lobby.bonus_packers import getFortRushMissionBonusPacker as getFortRushMissionBonusPacker
from fort_rush.gui.impl.lobby.quest_packers import FortRushDailyQuestUIDataPacker as FortRushDailyQuestUIDataPacker
from fort_rush.gui.impl.lobby.tooltips.fort_rush_daily_quest_tooltip import FortRushProgressionQuestTooltip as FortRushProgressionQuestTooltip
from fort_rush.gui.shared.event_dispatcher import showProgressionView as showProgressionView
from fort_rush.gui.impl.lobby.user_missions.fort_rush_overlap_ctrl import FortRushOverlapCtrlMixin as FortRushOverlapCtrlMixin
from fort_rush.skeletons.battle_controller import IFortRushBattleController as IFortRushBattleController
from fort_rush_common.fort_rush_constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from gui.Scaleform.genConsts.MISSIONS_STATES import MISSIONS_STATES as MISSIONS_STATES
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.user_missions.widget.quests_list_model import QuestsListModel as QuestsListModel
from gui.impl.gen.view_models.views.lobby.user_missions.widget.widget_quest_model import WidgetQuestModel as WidgetQuestModel
from gui.impl.lobby.missions.missions_helpers import needToUpdateQuestsInModel as needToUpdateQuestsInModel
from gui.impl.lobby.user_missions.hangar_widget.presenters.base_child_presenter import UserMissionChildPresenter as UserMissionChildPresenter
from gui.impl.lobby.user_missions.hangar_widget.presenters.constants import UserMissionGroups as UserMissionGroups
from gui.impl.lobby.user_missions.hangar_widget.tooltip_positioner import TooltipPositionerMixin as TooltipPositionerMixin
from gui.impl.lobby.user_missions.tooltips.all_quests_done_tooltip import AllQuestsDoneTooltip as AllQuestsDoneTooltip
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.shared.missions.packers.events import findFirstConditionModel as findFirstConditionModel, packQuestBonusModelAndTooltipData as packQuestBonusModelAndTooltipData
from helpers import dependency as dependency
from helpers.time_utils import getServerRegionalTime as getServerRegionalTime
from shared_utils import findFirst as findFirst
from skeletons.gui.battle_results import IBattleResultsService as IBattleResultsService
from skeletons.gui.game_control import IGameSessionController as IGameSessionController
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from frameworks.wulf import Array as Array, View as View, ViewEvent as ViewEvent
from gui.server_events.event_items import Quest as Quest

# base nao representavel no stub: ViewComponent[...]
class FortRushQuestsPresenter(UserMissionChildPresenter, TooltipPositionerMixin, FortRushOverlapCtrlMixin, IGlobalListener):
    GROUP = UserMissionGroups.MISSIONS
    __battleResults: Any
    __gameSession: Any
    __ctrl: Any
    __eventsCache: Any
    __itemsCache: Any
    __hangarSpace: Any
    __quests: Any
    __isModelInited: Any
    __battleResultsArenaUniqueID: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def isVisible(self):
        ...
    @property
    def hasDeferModelUpdate(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def _getCallbacks(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _rawUpdate(self):
        ...
    def _getModel(self, quest):
        ...
    def _getQuestFromEvent(self, event):
        ...
    def _updateCurrentMissionCountDown(self, missionItem):
        ...
    @staticmethod
    def __getFirstConditionModel(questModel):
        ...
    def __getAvailability(self):
        ...
    def __onTokensUpdate(self, diff):
        ...
    def __handleBattleResultsPosted(self, reusableInfo, _, __):
        ...
    def __onVehicleLoaded(self):
        ...
    def _onSpaceCreate(self):
        ...
    def __onSyncCompleted(self, *_):
        ...
    def __initModel(self):
        ...
    def __onMissionClick(self, *args):
        ...
    def __onMarkAsViewed(self):
        ...
    def __refresh(self):
        ...
    def __getTimeLeft(self):
        ...
