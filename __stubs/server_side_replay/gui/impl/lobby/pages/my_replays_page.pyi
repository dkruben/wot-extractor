# wot-extractor: STUB (.pyi) gerado a partir de sources/res/server_side_replay/scripts/client/server_side_replay/gui/impl/lobby/pages/my_replays_page.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from past.builtins import unicode as unicode
from typing import TYPE_CHECKING as TYPE_CHECKING, Optional as Optional, List as List, Dict as Dict
import BigWorld as BigWorld
from BattleReplay import BattleReplay as BattleReplay
from adisp import adisp_process as adisp_process
from dossiers2.custom.records import DB_ID_TO_RECORD as DB_ID_TO_RECORD
from dossiers2.ui import layouts as layouts
from frameworks.wulf import WindowLayer as WindowLayer
from gui.impl.gen import R as R
from server_side_replay.gui.impl.gen.view_models.views.lobby.filter_toggle_group_model import ToggleGroupType as ToggleGroupType
from server_side_replay.gui.impl.gen.view_models.views.lobby.pages.best_replays_model import BestReplaysModel as BestReplaysModel
from server_side_replay.gui.impl.gen.view_models.views.lobby.replay_model import ReplayModel as ReplayModel, MarksOfMastery as MarksOfMastery
from server_side_replay.gui.impl.gen.view_models.views.lobby.enums import ReplaysViews as ReplaysViews
from server_side_replay.gui.impl.gen.view_models.views.lobby.table_base_model import State as State
from server_side_replay.gui.impl.gen.view_models.views.lobby.top_replay_model import StatParams as StatParams
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.common.vehicle_model_helpers import fillVehicleModel as fillVehicleModel
from server_side_replay.gui.impl.lobby.filter import getVehicleTypeSettings as getVehicleTypeSettings, getNationSettings as getNationSettings, getVehicleTierSettings as getVehicleTierSettings
from server_side_replay.gui.impl.lobby.filter.state import FilterState as FilterState
from server_side_replay.gui.impl.lobby.pages import PageSubModelPresenter as PageSubModelPresenter
from server_side_replay.gui.impl.lobby.popovers.replays_filter_popover_view import ReplaysFilterPopoverView as ReplaysFilterPopoverView
from server_side_replay.gui.impl.lobby.utils import WebReplaysHelper as WebReplaysHelper
from gui.impl.pub import PopOverWindow as PopOverWindow
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.shared.gui_items.dossier import getAchievementFactory as getAchievementFactory
from gui.shared.gui_items.dossier.achievements import MarkOfMasteryAchievement as MarkOfMasteryAchievement
from server_side_replay.gui.wgcg.data_wrappers.server_replays import DataNames as DataNames, StatParams as DataStatParams
from server_side_replay.gui.wgcg.providers.server_replays_provider import ServerReplaysProvider as ServerReplaysProvider
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from server_side_replay.gui.wgcg.data_wrappers import server_replays as server_replays
_logger: Any
_DataToModelStatParam: dict
_ModelToDataStatParam: dict
_DataToModelMarkOfMastery: dict

class MyReplaysPage(PageSubModelPresenter):
    __itemsCache: Any
    __tooltips: Any
    __selectedSortBy: Any
    __callback: Any
    __selectedVehID: Any
    __cachedBestReplaysData: Any
    __filterState: Any
    __loadingData: Any
    __serverReplayProvider: Any
    def __init__(self, viewModel, parentView):
        ...
    @property
    def pageId(self):
        ...
    @property
    def viewModel(self):
        ...
    def initialize(self, *args, **kwargs):
        ...
    def hasAppliedFilters(self):
        ...
    def createPopOver(self, event):
        ...
    def _getEvents(self):
        ...
    def __onPopoverStateUpdated(self, clearCallback=False):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateState(self, loadedData=None, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateReplays(self, allReplaysData, model=None):
        ...
    def __makeReplayModel(self, replayInfo, model=None):
        ...
    def __updateFilter(self, model=None):
        ...
    def __onResetFilter(self, *args):
        ...
    # decorador original: @args2params(...)
    def __onWatch(self, index):
        ...
    # decorador original: @args2params(...)
    def __onLike(self, index):
        ...
    # decorador original: @adisp_process
    def __playReplay(self, replayLink):
        ...
    def __playReplay2(self, relativePath):
        ...
    # decorador original: @args2params(...)
    def __onSort(self, param):
        ...
    def __onRefresh(self):
        ...
    def __onDataReceived(self, dataName, data):
        ...
    def __onDataFailed(self, dataName):
        ...
