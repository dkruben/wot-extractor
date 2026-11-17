# wot-extractor: STUB (.pyi) gerado a partir de sources/res/open_bundle/scripts/client/open_bundle/gui/impl/lobby/main_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from builtins import round as round
from enum import Enum as Enum
from future.utils import viewvalues as viewvalues
from adisp import adisp_process as adisp_process
from functools import partial as partial
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from frameworks.wulf.gui_constants import ViewStatus as ViewStatus
from gui.Scaleform.daapi.view.lobby.storage.storage_helpers import getVehicleCDForStyle as getVehicleCDForStyle
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.customization.attachments_preview.attachments_preview_model import AttachmentsPreviewFeature as AttachmentsPreviewFeature
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.shared.event_dispatcher import selectVehicleInHangar as selectVehicleInHangar, showAttachmentsSetPreview as showAttachmentsSetPreview, showHangar as showHangar, showStylePreview as showStylePreview, showVehicleHubOverview as showVehicleHubOverview
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.money import Currency as Currency, Money as Money
from gui.shop import showBuyGoldForBundle as showBuyGoldForBundle
from helpers import dependency as dependency, time_utils as time_utils
from messenger.proto.events import g_messengerEvents as g_messengerEvents
from open_bundle.gui.impl.gen.view_models.views.lobby.cell_model import CellModel as CellModel
from open_bundle.gui.impl.gen.view_models.views.lobby.main_view_model import MainViewModel as MainViewModel
from open_bundle.gui.impl.lobby.decorators import createTooltipContentDecorator as createTooltipContentDecorator
from open_bundle.gui.impl.lobby.sounds import OPEN_BUNDLE_SOUND_SPACE as OPEN_BUNDLE_SOUND_SPACE
from open_bundle.gui.impl.lobby.tooltips.fixed_rewards_tooltip import FixedRewardsTooltip as FixedRewardsTooltip
from open_bundle.gui.shared.gui_items.processors.processors import ProcessNextStepProcessor as ProcessNextStepProcessor
from open_bundle.helpers.account_settings import setEntryPointShown as setEntryPointShown
from open_bundle.helpers.bonuses.bonus_packers import composeBonuses as composeBonuses, hideInvisible as hideInvisible, packBonusModelAndTooltipData as packBonusModelAndTooltipData, sortBonuses as sortBonuses
from open_bundle.skeletons.open_bundle_controller import IOpenBundleController as IOpenBundleController
from shared_utils import first as first
from skeletons.gui.game_control import IAchievements20EarningController as IAchievements20EarningController, ISoundEventChecker as ISoundEventChecker
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.shared import IItemsCache as IItemsCache

class _CellState(str, Enum):
    AVAILABLE = 'available'
    NEWLY_RECEIVED = 'newlyReceived'
    RECEIVED = 'received'

class MainView(ViewImpl):
    _COMMON_SOUND_SPACE = OPEN_BUNDLE_SOUND_SPACE
    __achievements: Any
    __customization: Any
    __itemsCache: Any
    __openBundle: Any
    __soundEventChecker: Any
    __bundle: Any
    __receivedCells: Any
    __newlyReceivedCells: Any
    __tooltipItems: Any
    def __init__(self, layoutID=..., *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    # decorador original: @createTooltipContentDecorator(...)
    def createToolTipContent(self, event, contentID):
        ...
    def getTooltipData(self, event):
        ...
    def _onLoading(self, bundleID):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def _getCallbacks(self):
        ...
    def __onSettingsChanged(self, *_):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateModel(self, model=None):
        ...
    def __fillMainInfo(self, model):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __fillPrice(self, value=None, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __fillCells(self, model=None):
        ...
    def __fillCellCoordinates(self, cellModel, cell):
        ...
    def __fillCellBonusInfo(self, cellModel, cellName):
        ...
    def __fillBonuses(self, cellModel, cellBonusInfo):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __fillFixedReward(self, model=None):
        ...
    def __calculateProbability(self, cellName, defaultProbability):
        ...
    # decorador original: @adisp_process
    def __processNextStep(self):
        ...
    def __unlockSpoilers(self):
        ...
    def __getNextStepNumber(self):
        ...
    def __getCurrentStep(self):
        ...
    # decorador original: @args2params(...)
    def __onItemShown(self, cellName):
        ...
    # decorador original: @args2params(...)
    def __showPreview(self, bonusType, bonusId, styleID, attachmentsToken):
        ...
    def __selectVehicle(self, vehicleCD):
        ...
    def __getCellState(self, cellName):
        ...
    def __setInterruption(self, isInterruption=False):
        ...
    def __isEnoughMoney(self, stepPrice):
        ...
    def __makeNotificationLockKey(self):
        ...
    def __lockSpoilerMessages(self):
        ...
    def __unlockMessages(self):
        ...
