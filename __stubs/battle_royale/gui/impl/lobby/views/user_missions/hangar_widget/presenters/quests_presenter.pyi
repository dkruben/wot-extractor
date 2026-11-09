# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/user_missions/hangar_widget/presenters/quests_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from battle_royale.gui.impl.lobby.br_helpers.account_settings import setLastSeenQuestData as setLastSeenQuestData, getLastSeenQuestData as getLastSeenQuestData
from battle_royale.gui.impl.lobby.tooltips.progression_quest_tooltip import BattleRoyaleProgressionQuestTooltip as BattleRoyaleProgressionQuestTooltip
from battle_royale.gui.impl.lobby.views.bonus_packer import getBonusPacker as getBonusPacker, packQuestBonuses as packQuestBonuses, packMissionItem as packMissionItem
from battle_royale.gui.impl.lobby.views.quests_packer import BRDailyQuestUIDataPacker as BRDailyQuestUIDataPacker
from battle_royale.gui.impl.lobby.views.user_missions.hangar_widget.overlap_ctrl import BattleRoyaleOverlapCtrlMixin as BattleRoyaleOverlapCtrlMixin
from battle_royale.gui.shared.event_dispatcher import showProgressionView as showProgressionView
from battle_royale.skeletons.game_controller import IBRProgressionOnTokensController as IBRProgressionOnTokensController
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from frameworks.wulf.view.array import fillViewModelsArray as fillViewModelsArray
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.user_missions.widget.quests_list_model import QuestsListModel as QuestsListModel
from gui.impl.gen.view_models.views.lobby.user_missions.widget.widget_quest_model import WidgetQuestModel as WidgetQuestModel
from gui.impl.lobby.missions.missions_helpers import needToUpdateQuestsInModel as needToUpdateQuestsInModel
from gui.impl.lobby.user_missions.hangar_widget.presenters.constants import UserMissionGroups as UserMissionGroups
from gui.impl.lobby.user_missions.hangar_widget.presenters.base_child_presenter import UserMissionChildPresenter as UserMissionChildPresenter
from gui.impl.lobby.user_missions.hangar_widget.tooltip_positioner import TooltipPositionerMixin as TooltipPositionerMixin
from gui.impl.lobby.user_missions.tooltips.all_quests_done_tooltip import AllQuestsDoneTooltip as AllQuestsDoneTooltip
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.server_events.events_helpers import EventInfoModel as EventInfoModel
from helpers import dependency as dependency, time_utils as time_utils
from helpers.time_utils import ONE_DAY as ONE_DAY
from skeletons.gui.battle_results import IBattleResultsService as IBattleResultsService
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from shared_utils import findFirst as findFirst
from frameworks.wulf import Array as Array, ViewEvent as ViewEvent
from gui.server_events.event_items import Quest as Quest

# base nao representavel no stub: ViewComponent[...]
class BattleRoayaleQuestsPresenter(UserMissionChildPresenter, TooltipPositionerMixin, BattleRoyaleOverlapCtrlMixin):
    GROUP = UserMissionGroups.MISSIONS
    __battleRoyale: Any
    __brProgression: Any
    __eventsCache: Any
    __hangarSpace: Any
    __battleResults: Any
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
    def _onLoading(self, *args, **kwargs):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def prepare(self):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def __getAvailability(self):
        ...
    def _rawUpdate(self):
        ...
    def _getModel(self, quest):
        ...
    def _getQuestFromEvent(self, event):
        ...
    def __handleBattleResultsPosted(self, reusableInfo, _, __):
        ...
    def __onVehicleLoaded(self):
        ...
    def __onSpaceCreate(self):
        ...
    def __onProgressSettingsChanged(self):
        ...
    def __onSyncCompleted(self, *_):
        ...
    def __initModel(self):
        ...
    def __refresh(self):
        ...
    def __getQuests(self):
        ...
    def __onMissionClick(self, *args):
        ...
    def __onMarkAsViewed(self):
        ...
    def __getTimeLeft(self):
        ...
