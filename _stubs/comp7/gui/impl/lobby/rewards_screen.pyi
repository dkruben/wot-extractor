# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/rewards_screen.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from collections import namedtuple as namedtuple
from copy import copy as copy
import Windowing as Windowing
from shared_utils import first as first, findFirst as findFirst
import SoundGroups as SoundGroups
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import COMP7_LAST_SEASON_WITH_SEEN_REWARD as COMP7_LAST_SEASON_WITH_SEEN_REWARD, COMP7_LAST_MASKOT_WITH_SEEN_REWARD as COMP7_LAST_MASKOT_WITH_SEEN_REWARD
from comp7.gui.game_control.comp7_shop_controller import ShopControllerStatus as ShopControllerStatus
from comp7.gui.impl.gen.view_models.views.lobby.enums import MetaRootViews as MetaRootViews, SeasonName as SeasonName
from comp7.gui.impl.gen.view_models.views.lobby.rewards_screen_model import Type as Type, RewardsScreenModel as RewardsScreenModel, ShopInfoType as ShopInfoType, VideoState as VideoState
from comp7.gui.impl.gen.view_models.views.lobby.season_result import SeasonResult as SeasonResult
from comp7.gui.impl.lobby.comp7_helpers import comp7_shared as comp7_shared, comp7_qualification_helpers as comp7_qualification_helpers
from comp7.gui.impl.lobby.comp7_helpers.comp7_bonus_packer import packRanksRewardsQuestBonuses as packRanksRewardsQuestBonuses, packTokensRewardsQuestBonuses as packTokensRewardsQuestBonuses, packQualificationRewardsQuestBonuses as packQualificationRewardsQuestBonuses, packYearlyRewardsBonuses as packYearlyRewardsBonuses, packYearlyRewardVehicleBonuses as packYearlyRewardVehicleBonuses, packSelectedRewardsBonuses as packSelectedRewardsBonuses
from comp7.gui.impl.lobby.comp7_helpers.comp7_lobby_sounds import VehicleVideoSounds as VehicleVideoSounds
from comp7.gui.impl.lobby.comp7_helpers.comp7_model_helpers import getYearlyRewardsRank as getYearlyRewardsRank
from comp7.gui.impl.lobby.comp7_helpers.comp7_quest_helpers import parseComp7RanksQuestID as parseComp7RanksQuestID, getPeriodicQuestsByDivision as getPeriodicQuestsByDivision
from comp7.gui.prb_control.entities import comp7_prb_helpers as comp7_prb_helpers
from comp7.gui.selectable_reward.common import Comp7SelectableRewardManager as Comp7SelectableRewardManager
from comp7.gui.shared import event_dispatcher as event_dispatcher
from comp7.skeletons.gui.game_control import IComp7ShopController as IComp7ShopController
from comp7_common_const import seasonPointsCodeBySeasonNumber as seasonPointsCodeBySeasonNumber, COMP7_MASKOT_ID as COMP7_MASKOT_ID
from comp7_core.gui.impl.lobby.comp7_core_helpers.comp7_core_model_helpers import getSeasonNameEnum as getSeasonNameEnum
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags, WindowLayer as WindowLayer
from frameworks.wulf.view.array import fillIntsArray as fillIntsArray, fillViewModelsArray as fillViewModelsArray
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow
from gui.impl.backport.backport_tooltip import TooltipData as TooltipData
from gui.impl.gen import R as R
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.common.vehicle_model_helpers import fillVehicleModel as fillVehicleModel
from gui.impl.lobby.tooltips.additional_rewards_tooltip import AdditionalRewardsTooltip as AdditionalRewardsTooltip
from gui.impl.lobby.tooltips.vehicle_role_descr_view import VehicleRolesTooltipView as VehicleRolesTooltipView
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.selectable_reward.constants import SELECTABLE_BONUS_NAME as SELECTABLE_BONUS_NAME
from gui.server_events.bonuses import VehiclesBonus as VehiclesBonus
from gui.shared import event_dispatcher as shared_events
from gui.sounds.filters import switchVideoOverlaySoundFilter as switchVideoOverlaySoundFilter
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7Controller as IComp7Controller, IHangarSpaceSwitchController as IHangarSpaceSwitchController
from skeletons.gui.offers import IOffersDataProvider as IOffersDataProvider
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Tuple as Tuple, Callable as Callable
from comp7_ranks_common import Comp7Division as Comp7Division
from frameworks.wulf import Command as Command
from frameworks.wulf.view.view_event import ViewEvent as ViewEvent
from gui.server_events.event_items import TokenQuest as TokenQuest
_logger: Any
_MAX_MAIN_REWARDS_COUNT = 4
_MAIN_REWARDS: tuple
_BonusData: Any

class _BaseRewardsView(ViewImpl):
    __slots__: tuple
    _bonusData: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _finalize(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def _packBonuses(self, *args, **kwargs):
        ...
    def _getMainRewardsCount(self):
        ...
    def _onClose(self):
        ...
    def _setRewards(self):
        ...
    def _packBonusData(self, *args, **kwargs):
        ...

class _QuestRewardsView(_BaseRewardsView):
    _comp7Controller: Any
    _comp7ShopController: Any
    _spaceSwitchController: Any
    def _onLoading(self, *args, **kwargs):
        ...
    def _setProductsData(self):
        ...
    def _getEvents(self):
        ...
    def __onShopStatusUpdated(self, status):
        ...
    def __onOpenShop(self):
        ...
    def __onSpaceUpdated(self):
        ...
    def __goToShop(self):
        ...

class RanksRewardsView(_QuestRewardsView):
    __slots__: tuple
    __comp7Controller: Any
    __division: Any
    def __init__(self, *args, **kwargs):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _packBonuses(self, *args, **kwargs):
        ...
    def _setProductsData(self):
        ...
    def _onClose(self):
        ...
    def _getType(self):
        ...

class TokensRewardsView(_QuestRewardsView):
    __willOpenRewardsSelection: Any
    def __init__(self, *args, **kwargs):
        ...
    def willOpenRewardsSelection(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _packBonuses(self, *args, **kwargs):
        ...
    def _setProductsData(self):
        ...
    def _getMainRewardsCount(self):
        ...
    def _getEvents(self):
        ...
    def _onClose(self):
        ...
    def __onOpenNextScreen(self):
        ...
    def __isSelectableReward(self, quest):
        ...

class QualificationRewardsView(_QuestRewardsView):
    __slots__: tuple
    __divisions: Any
    def __init__(self, *args, **kwargs):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _packBonuses(self, *args, **kwargs):
        ...
    def _setProductsData(self):
        ...
    def _onClose(self):
        ...
    def __getRanks(self, divisions):
        ...
    def __getDivisions(self, quests):
        ...
    def __hasShopProduct(self):
        ...

class YearlyRewardsView(_BaseRewardsView):
    __slots__: tuple
    __comp7Controller: Any
    __offersDataProvider: Any
    __itemsCache: Any
    _onClose: Any
    __bonuses: Any
    __hasOfferReward: Any
    __hasYearlyVehicle: Any
    __willOpenRewardsSelection: Any
    def __init__(self, *args, **kwargs):
        ...
    def willOpenRewardsSelection(self):
        ...
    def createToolTip(self, event):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def _packBonuses(self, *args, **kwargs):
        ...
    def _getMainRewardsCount(self):
        ...
    def __updateSeasonsResults(self, model):
        ...
    def __onWindowAccessibilityChanged(self, _):
        ...
    def __updateYearlyVehicle(self, model, bonuses):
        ...
    def __onOffersUpdated(self):
        ...
    def __onOpenNextScreen(self):
        ...
    # decorador original: @args2params(...)
    def __onChangeType(self, newType):
        ...
    # decorador original: @args2params(...)
    def __onVideoStateChange(self, state):
        ...

class SelectedRewardsView(_BaseRewardsView):
    def _onLoading(self, *args, **kwargs):
        ...
    def _packBonuses(self, *args, **kwargs):
        ...
    def _getMainRewardsCount(self):
        ...

class RanksRewardsWindow(LobbyNotificationWindow):
    __slots__: tuple
    def __init__(self, quest, parent=None):
        ...

class TokensRewardsWindow(LobbyNotificationWindow):
    __slots__: tuple
    def __init__(self, quest, parent=None):
        ...

class QualificationRewardsWindow(LobbyNotificationWindow):
    __slots__: tuple
    def __init__(self, quests, parent=None):
        ...

class YearlyRewardsWindow(LobbyNotificationWindow):
    __slots__: tuple
    def __init__(self, bonuses, showSeasonResults, parent=None):
        ...

class SelectedRewardsWindow(LobbyNotificationWindow):
    __slots__: tuple
    def __init__(self, bonuses, parent=None):
        ...
