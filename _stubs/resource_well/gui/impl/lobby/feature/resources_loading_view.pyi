# wot-extractor: STUB (.pyi) gerado a partir de sources/res/resource_well/scripts/client/resource_well/gui/impl/lobby/feature/resources_loading_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from builtins import str as str
from future.utils import iteritems as iteritems
from adisp import adisp_process as adisp_process
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags, ViewStatus as ViewStatus
from gui.impl.auxiliary.vehicle_helper import fillVehicleInfo as fillVehicleInfo
from gui.impl.gen import R as R
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyWindow as LobbyWindow
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.event_dispatcher import showHangar as showHangar
from helpers import dependency as dependency
from resource_well.gui.feature.constants import ResourceType as ResourceType, UNAVAILABLE_REWARD_ERROR as UNAVAILABLE_REWARD_ERROR, PurchaseMode as PurchaseMode
from resource_well.gui.feature.processors import PutResourcesProcessor as PutResourcesProcessor, NextSerialVehicleProcessor as NextSerialVehicleProcessor
from resource_well.gui.feature.resource import processResourcesConfig as processResourcesConfig
from resource_well.gui.feature.resource_well_helpers import fillVehicleCounter as fillVehicleCounter, getNextSerialRewardID as getNextSerialRewardID
from resource_well.gui.impl.gen.view_models.views.lobby.resource_model import ResourceModel as ResourceModel
from resource_well.gui.impl.gen.view_models.views.lobby.resources_loading_view_model import ResourcesLoadingViewModel as ResourcesLoadingViewModel, ProgressionState as ProgressionState
from resource_well.gui.impl.gen.view_models.views.lobby.resources_tab_model import ResourcesTabModel as ResourcesTabModel
from resource_well.gui.impl.lobby.feature.sounds import RESOURCE_WELL_SOUND_SPACE as RESOURCE_WELL_SOUND_SPACE
from resource_well.gui.impl.lobby.feature.tooltips.max_progress_tooltip import MaxProgressTooltip as MaxProgressTooltip
from resource_well.gui.impl.lobby.feature.tooltips.progress_tooltip import ProgressTooltip as ProgressTooltip
from resource_well.gui.shared import events as events
from resource_well.gui.shared.event_dispatcher import showResourceWellNoVehiclesConfirm as showResourceWellNoVehiclesConfirm
from shared_utils import findFirst as findFirst
from skeletons.gui.resource_well import IResourceWellController as IResourceWellController
_logger: Any
_FULL_PROGRESS = 100

class ResourcesLoadingView(ViewImpl):
    _COMMON_SOUND_SPACE = RESOURCE_WELL_SOUND_SPACE
    __resourceWell: Any
    __rewardID: Any
    __stopRequesterInDestroy: Any
    __rewardConfig: Any
    __resources: Any
    __tooltips: Any
    def __init__(self, rewardID, stopRequesterInDestroy=True):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    def getTooltipData(self, event):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getCallbacks(self):
        ...
    def _getEvents(self):
        ...
    def __isDestroyed(self):
        ...
    def __updateModel(self):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __fillProgression(self, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __fillTabs(self, model=None):
        ...
    def __fillResources(self, resourceModels, resources):
        ...
    def __fillResource(self, resourceModel, resource, rateCof):
        ...
    def __updateCurrencies(self, *_):
        ...
    def __updateBlueprints(self, *_):
        ...
    def __updateResourceModels(self, resourceType):
        ...
    # decorador original: @adisp_process
    def __loadResources(self, args):
        ...
    # decorador original: @adisp_process
    def __showNextSerialRewardConfirm(self, rewardID, resources):
        ...
    def __onLoadResources(self, result, responseCtx, nextRewardID=None):
        ...
    def __showNoRewardsConfirm(self):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateLoadingError(self, isError, model=None):
        ...
    def __showHangar(self):
        ...
    def __close(self):
        ...
    def __onNumberRequesterUpdated(self):
        ...
    def __onEventStateUpdated(self):
        ...

class ResourcesLoadingWindow(LobbyWindow):
    __slots__: tuple
    def __init__(self, rewardID, stopRequesterInDestroy=True):
        ...
