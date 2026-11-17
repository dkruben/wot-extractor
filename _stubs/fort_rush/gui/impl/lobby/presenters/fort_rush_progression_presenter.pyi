# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/presenters/fort_rush_progression_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewvalues as viewvalues
import logging as logging
from typing import TYPE_CHECKING as TYPE_CHECKING
from fort_rush.account_helpers.account_settings import getLastSeenProgressionPoints as getLastSeenProgressionPoints, setLastSeenProgressionPoints as setLastSeenProgressionPoints
from fort_rush.gui.impl.gen.view_models.views.progression.milestone_model import MilestoneModel as MilestoneModel
from frameworks.wulf.view.submodel_presenter import SubModelPresenter as SubModelPresenter
from gui.impl.gen import R as R
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow, TooltipData as TooltipData
from gui.impl.lobby.common.tooltips.extended_text_tooltip import ExtendedTextTooltip as ExtendedTextTooltip
from fort_rush.gui.impl.gen.view_models.views.progression.progression_view_model import ProgressionViewModel as ProgressionViewModel
from fort_rush.gui.impl.gen.view_models.views.progression.mission_model import MissionModel as MissionModel
from gui.shared.missions.packers.bonus import getDefaultBonusPacker as getDefaultBonusPacker
from gui.shared.missions.packers.events import packQuestBonusModelAndTooltipData as packQuestBonusModelAndTooltipData
from helpers import dependency as dependency
from fort_rush.skeletons.battle_controller import IFortRushBattleController as IFortRushBattleController
from helpers.time_utils import getTimestampFromUTC as getTimestampFromUTC, utcToLocalDatetime as utcToLocalDatetime
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.game_control import IGameSessionController as IGameSessionController
from skeletons.gui.shared import IItemsCache as IItemsCache
from fort_rush.gui.impl.lobby.quest_packers import FortRushDailyQuestUIDataPacker as FortRushDailyQuestUIDataPacker
from fort_rush_common.configs.fort_rush_battles_config import fortRushBattlesConfigGameParamsSchema as fortRushBattlesConfigGameParamsSchema
from gui.impl.lobby.missions.missions_helpers import markQuestProgressAsViewed as markQuestProgressAsViewed
from PlayerEvents import g_playerEvents as g_playerEvents
from frameworks.wulf import Array as Array, ViewEvent as ViewEvent
from fort_rush_common.configs.fort_rush_battles_config import FortRushBattlesConfigModel as FortRushBattlesConfigModel
_logger: Any

class _MissionDecoration(object):
    WIN = 1
    KILL_VEHICLES = 2
    DAMAGE = 3
    BASE_CAPTURE = 4
    RAM = 5
    TOP3 = 6

class FortRushProgressionPresenter(SubModelPresenter):
    __gameSession: Any
    __ctrl: Any
    __eventsCache: Any
    __itemsCache: Any
    __tooltipData: Any
    def __init__(self, viewModel, parentView):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def tokens(self):
        ...
    @property
    def config(self):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def packModel(self):
        ...
    def saveSeenProgress(self):
        ...
    def _getEvents(self):
        ...
    def _getCallbacks(self):
        ...
    def finalize(self):
        ...
    def _updateModel(self):
        ...
    def _fillTimers(self):
        ...
    def _fillDailyMissions(self):
        ...
    def _fillMissions(self, missionModelArray, questPrefix):
        ...
    @staticmethod
    def filterQuestsByTokenRequirement(quests, token):
        ...
    def _fillProgressionPoints(self):
        ...
    def _fillMilestones(self):
        ...
    def __onConfigModelUpdated(self, gpKey):
        ...
    def __onSyncCompleted(self, reason, diff):
        ...
    def __onTokensUpdate(self, diff):
        ...
    def __getTooltipData(self, event):
        ...
