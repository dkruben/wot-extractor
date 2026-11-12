# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/vehicle_preview.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import itertools as itertools
from copy import deepcopy as deepcopy
import BigWorld as BigWorld
import SoundGroups as SoundGroups
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle, g_currentVehicle as g_currentVehicle
from HeroTank import HeroTank as HeroTank
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import PREVIEW_INFO_PANEL_IDX as PREVIEW_INFO_PANEL_IDX
from account_helpers.settings_core.ServerSettingsManager import UI_STORAGE_KEYS as UI_STORAGE_KEYS
from constants import QUEUE_TYPE as QUEUE_TYPE
from gui import makeHtmlString as makeHtmlString
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.LobbySelectableView import LobbySelectableView as LobbySelectableView
from gui.Scaleform.daapi.view.lobby.store.browser.sound_constants import SHOP_PREVIEW_SOUND_SPACE as SHOP_PREVIEW_SOUND_SPACE
from gui.Scaleform.daapi.view.lobby.vehicle_compare.formatters import resolveStateTooltip as resolveStateTooltip
from gui.Scaleform.daapi.view.lobby.vehicle_preview.hero_tank_preview_constants import getHeroTankPreviewParams as getHeroTankPreviewParams
from gui.Scaleform.daapi.view.lobby.vehicle_preview.info.crew_tab_view import DOG as DOG
from gui.Scaleform.daapi.view.lobby.vehicle_preview.items_kit_helper import OFFER_CHANGED_EVENT as OFFER_CHANGED_EVENT, addBuiltInEquipment as addBuiltInEquipment, getActiveOffer as getActiveOffer
from gui.Scaleform.daapi.view.lobby.vehicle_preview.preview_selectable_logic import PreviewSelectableLogic as PreviewSelectableLogic
from gui.Scaleform.daapi.view.lobby.vehicle_preview.sound_constants import RESEARCH_PREVIEW_SOUND_SPACE as RESEARCH_PREVIEW_SOUND_SPACE, VEHICLE_PREVIEW_SOUND_SPACE as VEHICLE_PREVIEW_SOUND_SPACE, COMMON_VEHICLE_PREVIEW_SOUND_SPACE as COMMON_VEHICLE_PREVIEW_SOUND_SPACE
from gui.Scaleform.daapi.view.meta.VehiclePreviewMeta import VehiclePreviewMeta as VehiclePreviewMeta
from gui.Scaleform.genConsts.PERSONAL_MISSIONS_ALIASES import PERSONAL_MISSIONS_ALIASES as PERSONAL_MISSIONS_ALIASES
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.Scaleform.genConsts.VEHPREVIEW_CONSTANTS import VEHPREVIEW_CONSTANTS as VEHPREVIEW_CONSTANTS
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.VEHICLE_PREVIEW import VEHICLE_PREVIEW as VEHICLE_PREVIEW
from gui.Scaleform.locale.VEH_COMPARE import VEH_COMPARE as VEH_COMPARE
from gui.hangar_cameras.hangar_camera_common import CameraMovementStates as CameraMovementStates, CameraRelatedEvents as CameraRelatedEvents
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.lobby.battle_results.states import PostBattleResultsEntryState as PostBattleResultsEntryState
from gui.impl.lobby.hangar.buy_vehicle_view import BuyVehicleWindow as BuyVehicleWindow
from gui.prb_control.dispatcher import g_prbLoader as g_prbLoader
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, event_dispatcher as event_dispatcher, events as events, g_eventBus as g_eventBus
from gui.shared.formatters import getRoleTextWithIcon as getRoleTextWithIcon, text_styles as text_styles
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.money import MONEY_UNDEFINED as MONEY_UNDEFINED
from gui.shared.tutorial_helper import getTutorialGlobalStorage as getTutorialGlobalStorage
from helpers import dependency as dependency
from helpers.i18n import makeString as _ms
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.game_control import IHeroTankController as IHeroTankController, IVehicleComparisonBasket as IVehicleComparisonBasket
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from tutorial.control.context import GLOBAL_FLAG as GLOBAL_FLAG
from uilogging.shop.loggers import getPreviewUILoggers as getPreviewUILoggers
from uilogging.shop.logging_constants import ShopCloseItemStates as ShopCloseItemStates
from web.web_client_api.common import ItemPackEntry as ItemPackEntry, ItemPackType as ItemPackType, ItemPackTypeGroup as ItemPackTypeGroup
from gui.shared.events import ViewEventType as ViewEventType
VEHICLE_PREVIEW_ALIASES: set
_BACK_BTN_LABELS: dict
_TABS_DATA: tuple

class VehiclePreview(LobbySelectableView, VehiclePreviewMeta):
    __background_alpha__ = 0.0
    _itemsCache: Any
    __comparisonBasket: Any
    __heroTanksControl: Any
    __settingsCore: Any
    __guiLoader: Any
    _hangarSpace: Any
    __crewTabInject: Any
    __ctx: Any
    _backAlias: Any
    _itemsPack: Any
    __currentOffer: Any
    _vehicleCD: Any
    __vehicleStrCD: Any
    _previousBackAlias: Any
    _previewBackCb: Any
    __isHeroTank: Any
    __customizationCD: Any
    __offers: Any
    _price: Any
    _oldPrice: Any
    _title: Any
    __description: Any
    __endTime: Any
    __buyParams: Any
    __topPanelData: Any
    __style: Any
    __outfit: Any
    __subscriptions: Any
    _heroInteractive: Any
    __haveCustomCrew: Any
    __obtainingMethod: Any
    __hangarVehicleCD: Any
    __previewAppearance: Any
    __uiMetricsLogger: Any
    __uiFlowLogger: Any
    _COMMON_SOUND_SPACE: Any
    __vehAppearanceChanged: Any
    def __init__(self, ctx=None):
        ...
    def setTopPanel(self):
        ...
    def setBottomPanel(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def closeView(self):
        ...
    def onBackClick(self):
        ...
    def onOpenInfoTab(self, index):
        ...
    def onGoToPostProgressionClick(self):
        ...
    def onCompareClick(self):
        ...
    def handleSelectedEntityUpdated(self, event):
        ...
    def _highlight3DEntityAndShowTT(self, entity):
        ...
    def _fade3DEntityAndHideTT(self, entity):
        ...
    def _createSelectableLogic(self):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def _getData(self):
        ...
    def __prepareItems(self):
        ...
    def __onViewLoaded(self, event):
        ...
    def __onVehicleLoading(self, ctxEvent):
        ...
    def __fullUpdate(self):
        ...
    def __updateTabsData(self):
        ...
    def __onVehicleChanged(self, *args):
        ...
    def __updateCrewTabLabel(self):
        ...
    def __onCompareBasketChanged(self, changedData):
        ...
    def __updateHeaderData(self):
        ...
    @staticmethod
    def __getInfoPanelListDescription(vehicle):
        ...
    def _getPrbEntityType(self):
        ...
    def __onHangarCreateOrRefresh(self):
        ...
    def __handleWindowClose(self, event=None):
        ...
    def _processBackClick(self, ctx=None):
        ...
    def _onInventoryChanged(self, *_):
        ...
    def __onOfferChanged(self, event):
        ...
    def __updateModuleBullet(self):
        ...
    def _resetPostProgressionBullet(self):
        ...

def _isCollectibleVehicleWithModules():
    ...
def _updateCollectorHintParameters():
    ...
def _updatePostProgressionParameters():
    ...
def _isPostProgressionBulletVisible(settingsCore):
    ...
def _getModulesTabIdx():
    ...
