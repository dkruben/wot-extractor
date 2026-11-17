# wot-extractor: STUB (.pyi) gerado a partir de sources/res/resource_well/scripts/client/resource_well/gui/impl/lobby/feature/progression_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from builtins import round as round
from adisp import adisp_process as adisp_process
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.Scaleform.daapi.view.lobby.vehicle_preview.info.top_panel_tabs import PERSONAL_NUMBER_STYLE_TABS as PERSONAL_NUMBER_STYLE_TABS
from gui.Scaleform.genConsts.VEHPREVIEW_CONSTANTS import VEHPREVIEW_CONSTANTS as VEHPREVIEW_CONSTANTS
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.impl.auxiliary.vehicle_helper import fillVehicleInfo as fillVehicleInfo
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.vehicle_preview.top_panel.top_panel_tabs_model import TabID as TabID
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.shared.event_dispatcher import showHangar as showHangar
from gui.shared.utils.scheduled_notifications import SimpleNotifier as SimpleNotifier
from helpers import dependency as dependency, time_utils as time_utils
from resource_well.gui.feature.constants import PurchaseMode as PurchaseMode
from resource_well.gui.feature.processors import ResourceWellTakeBackProcessor as ResourceWellTakeBackProcessor
from resource_well.gui.feature.resource_well_helpers import isEventEndingsSoon as isEventEndingsSoon, getRewardStyle as getRewardStyle, getSerialNumber as getSerialNumber
from resource_well.gui.impl.gen.view_models.views.lobby.progression_view_model import ProgressionViewModel as ProgressionViewModel, ProgressionState as ProgressionState
from resource_well.gui.impl.gen.view_models.views.lobby.reward_model import RewardModel as RewardModel, RewardState as RewardState
from resource_well.gui.impl.lobby.feature.sounds import RESOURCE_WELL_SOUND_SPACE as RESOURCE_WELL_SOUND_SPACE
from resource_well.gui.impl.lobby.feature.tooltips.progress_tooltip import ProgressTooltip as ProgressTooltip
from resource_well.gui.impl.lobby.feature.tooltips.serial_number_tooltip import SerialNumberTooltip as SerialNumberTooltip
from resource_well.gui.shared.event_dispatcher import showResourceWellVehiclePreview as showResourceWellVehiclePreview, showMainWindow as showMainWindow, showResourcesLoadingWindow as showResourcesLoadingWindow
from skeletons.gui.resource_well import IResourceWellController as IResourceWellController
from resource_well.helpers.server_settings import RewardConfig as RewardConfig
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
_FULL_PROGRESS = 100

class ProgressionView(ViewImpl):
    _COMMON_SOUND_SPACE = RESOURCE_WELL_SOUND_SPACE
    __resourceWell: Any
    __notifier: Any
    __selectedRewardId: Any
    def __init__(self, layoutID=...):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def __updateModel(self):
        ...
    def __getCurrentRewardID(self):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateEventTime(self, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __fillEventInfo(self, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __fillProgression(self, model=None):
        ...
    def __fillRewards(self, rewards):
        ...
    def __fillSelectReward(self, rewardID=None):
        ...
    def __getRewardModel(self, rewardID, reward):
        ...
    def __getRewardState(self, rewardID, rewardVehicle):
        ...
    def __getProgressionState(self):
        ...
    def __showHangar(self):
        ...
    # decorador original: @args2params(...)
    def __showPreview(self, rewardId):
        ...
    # decorador original: @args2params(...)
    def __contributeResources(self, rewardId):
        ...
    # decorador original: @args2params(...)
    def __selectReward(self, rewardId):
        ...
    # decorador original: @args2params(...)
    def __onResourcesReturn(self, rewardId):
        ...
    def __previewCallback(self):
        ...
    # decorador original: @adisp_process
    def __extractResources(self, rewardID):
        ...
    def __onEventUpdated(self):
        ...
    def __onSettingsChanged(self):
        ...
    def __goBack(self):
        ...
    def __getReminderTimeLeft(self):
        ...
    def __onNumberRequesterUpdated(self):
        ...

class ProgressionWindow(WindowImpl):
    def __init__(self, layer, *args, **kwargs):
        ...
