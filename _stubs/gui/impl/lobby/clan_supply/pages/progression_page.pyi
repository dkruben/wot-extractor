# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/clan_supply/pages/progression_page.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from adisp import adisp_process as adisp_process
from frameworks.wulf.view.submodel_presenter import SubModelPresenter as SubModelPresenter
from gui.clans.clan_cache import g_clanCache as g_clanCache
from gui.clans.data_wrapper.clan_supply import PointStatus as PointStatus, DataNames as DataNames
from gui.impl.gen.view_models.views.lobby.clan_supply.pages.progression_model import ScreenStatus as ProgressionScreenStatus
from gui.impl.gen.view_models.views.lobby.clan_supply.pages.stage_model import StageModel as StageModel, StageStatus as StageStatus
from gui.impl.gen.view_models.views.lobby.clan_supply.stage_info_model import ScreenStatus as StageScreenStatus, StageInfoStatus as StageInfoStatus
from gui.impl.lobby.clan_supply.bonus_packers import composeBonuses as composeBonuses, findVehicle as findVehicle, getClanSupplyBonusPacker as getClanSupplyBonusPacker, BONUSES_ORDER as BONUSES_ORDER
from gui.impl.lobby.common.vehicle_model_helpers import fillVehicleModel as fillVehicleModel
from gui.impl.lobby.common.view_helpers import packBonusModelAndTooltipData as packBonusModelAndTooltipData
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.shared.event_dispatcher import showVehicleHubOverview as showVehicleHubOverview
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.money import Currency as Currency
from gui.wgcg.clan_supply.contexts import PurchaseProgressionStageCtx as PurchaseProgressionStageCtx
from helpers import dependency as dependency
from shared_utils import findFirst as findFirst
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.web import IWebController as IWebController
from typing import Optional as Optional
from gui.clans.data_wrapper import clan_supply as clan_supply
from gui.impl.backport import TooltipData as TooltipData
from gui.impl.gen.view_models.views.lobby.clan_supply.pages.progression_model import ProgressionModel as ProgressionModel
from gui.impl.gen.view_models.views.lobby.clan_supply.clan_supply_vehicle_model import ClanSupplyVehicleModel as ClanSupplyVehicleModel
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
_logger: Any
DEFAULT_STAGE_ID = 1

class ProgressionPage(SubModelPresenter):
    __slots__: tuple
    __itemsCache: Any
    __webController: Any
    __c11nService: Any
    __tooltips: Any
    __rewardVehicleIntCD: Any
    __rewardStyleID: Any
    __selectedStageID: Any
    __cachedProgressData: Any
    __cachedSettingsData: Any
    __isFindSelectedStageNeeded: Any
    def __init__(self, viewModel, parentView):
        ...
    @property
    def viewModel(self):
        ...
    def initialize(self, *args, **kwargs):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    def getTooltipData(self, event):
        ...
    def _getEvents(self):
        ...
    def _getCallbacks(self):
        ...
    def __updateState(self):
        ...
    def __updateProgression(self, settingsData, progressData):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateStageInfo(self, stageID, settingsData, progressData, model=None):
        ...
    def __onDataReceived(self, dataName, data):
        ...
    def __onDataFailed(self, dataName):
        ...
    def __onSelectStage(self, kwargs):
        ...
    def __onPreviewClick(self):
        ...
    def __onRefresh(self):
        ...
    def __onStageInfoRefresh(self):
        ...
    # decorador original: @adisp_process
    def __onBuyStage(self, kwargs):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateBalance(self, value=None, model=None):
        ...
    @staticmethod
    def __fillStageModel(stageID, stageSettings, stageProgress):
        ...
    @staticmethod
    def __fillVehicleModel(vehicleModel, vehicle):
        ...
    @staticmethod
    def __findInitialSelectedStage(progressData):
        ...
    @staticmethod
    def __checkProgressionIsCompleted(progressData):
        ...
    @staticmethod
    def __isMainRewardAvailable(settingsData, progressData):
        ...
    @staticmethod
    def __findVehicleRewardIntCD(pointSettings):
        ...
    @staticmethod
    def __findStyleRewardID(pointSettings):
        ...
    def __validateRewards(self, rewards):
        ...
