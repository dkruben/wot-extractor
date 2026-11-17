# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/awards/multiple_awards_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from adisp import adisp_process as adisp_process
from constants import RentType as RentType
from frameworks.wulf import ViewSettings as ViewSettings, ViewStatus as ViewStatus, ViewFlags as ViewFlags
from gui.Scaleform.genConsts.STORAGE_CONSTANTS import STORAGE_CONSTANTS as STORAGE_CONSTANTS
from gui.battle_pass.battle_pass_decorators import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.impl import backport as backport
from gui.impl.auxiliary.tooltips.compensation_tooltip import VehicleCompensationTooltipContent as VehicleCompensationTooltipContent
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.awards.multiple_awards_view_model import MultipleAwardsViewModel as MultipleAwardsViewModel
from gui.impl.gen.view_models.views.lobby.awards.tooltips.awards_vehicle_for_choose_tooltip_view_model import AwardsVehicleForChooseTooltipViewModel as AwardsVehicleForChooseTooltipViewModel
from gui.impl.gen.view_models.views.loot_box_compensation_tooltip_types import LootBoxCompensationTooltipTypes as LootBoxCompensationTooltipTypes
from gui.impl.gen.view_models.views.loot_box_vehicle_compensation_tooltip_model import LootBoxVehicleCompensationTooltipModel as LootBoxVehicleCompensationTooltipModel
from gui.impl.lobby.awards import SupportedTokenTypes as SupportedTokenTypes
from gui.impl.lobby.awards.tooltip import VEH_FOR_CHOOSE_ID as VEH_FOR_CHOOSE_ID
from gui.impl.lobby.awards.tooltip.vehicle_for_choose import VehicleForChooseTooltipContent as VehicleForChooseTooltipContent
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.shared import event_dispatcher as event_dispatcher
from gui.shared.view_helpers.blur_manager import CachedBlur as CachedBlur
from gui.sounds.filters import switchHangarOverlaySoundFilter as switchHangarOverlaySoundFilter
from helpers import dependency as dependency
from skeletons.gui.offers import IOffersDataProvider as IOffersDataProvider
from skeletons.gui.platform.catalog_service_controller import IPurchaseCache as IPurchaseCache
from gui.impl.gen.view_models.views.lobby.awards.reward_model import RewardModel as RewardModel, RentTypeEnum as RentTypeEnum
from gui.platform.catalog_service.controller import _PurchaseDescriptor as _PurchaseDescriptor
_logger: Any

class MultipleAwardsView(ViewImpl):
    __purchaseCache: Any
    __offersProvider: Any
    __slots__: tuple
    __tooltipItems: Any
    __vehicleIntCD: Any
    __offer: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def getTooltipData(self, event):
        ...
    # decorador original: @adisp_process
    def _onLoading(self, rewards, tooltips, productCode, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __isDestroyed(self):
        ...
    def __extendSortedBonusList(self, sortedBList, extraData):
        ...
    def __setProductTypeData(self, rewards):
        ...
    def __onClose(self):
        ...
    def __handleShowHangar(self):
        ...
    def __handleMakeChoice(self):
        ...

class MultipleAwardsViewWindow(LobbyNotificationWindow):
    __slots__: tuple
    __blur: Any
    def __init__(self, rewards, tooltips, productCode):
        ...
    def load(self):
        ...
    @classmethod
    def _getContentView(cls, rewards, tooltips, productCode):
        ...
    def _finalize(self):
        ...
