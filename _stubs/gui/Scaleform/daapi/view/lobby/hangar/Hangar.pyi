# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/hangar/Hangar.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from functools import partial as partial
import BigWorld as BigWorld
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from helpers.i18n import makeString as _ms
from helpers.statistics import HANGAR_LOADING_STATE as HANGAR_LOADING_STATE
from ClientSelectableCameraObject import ClientSelectableCameraObject as ClientSelectableCameraObject
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle, g_currentVehicle as g_currentVehicle
from HeroTank import HeroTank as HeroTank
from PlayerEvents import g_playerEvents as g_playerEvents
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import NATION_CHANGE_VIEWED as NATION_CHANGE_VIEWED
from account_helpers.settings_core.ServerSettingsManager import SETTINGS_SECTIONS as SETTINGS_SECTIONS
from battle_pass_common import BATTLE_PASS_CONFIG_NAME as BATTLE_PASS_CONFIG_NAME
from constants import DOG_TAGS_CONFIG as DOG_TAGS_CONFIG, Configs as Configs
from frameworks.wulf import ViewStatus as ViewStatus, WindowFlags as WindowFlags, WindowLayer as WindowLayer, WindowStatus as WindowStatus
from gui import SystemMessages as SystemMessages
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.LobbySelectableView import LobbySelectableView as LobbySelectableView
from gui.Scaleform.daapi.view.lobby.hangar.carousel_event_entry_widget import isAnyEntryVisible as isAnyEntryVisible
from gui.Scaleform.daapi.view.meta.HangarMeta import HangarMeta as HangarMeta
from gui.Scaleform.framework.managers.containers import POP_UP_CRITERIA as POP_UP_CRITERIA
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.Scaleform.genConsts.HANGAR_ALIASES import HANGAR_ALIASES as HANGAR_ALIASES
from gui.Scaleform.genConsts.HANGAR_CONSTS import HANGAR_CONSTS as HANGAR_CONSTS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.easy_tank_equip.easy_tank_equip_helpers import isAvailableForVehicle as isAvailableForVehicle
from gui.game_control.links import URLMacros as URLMacros
from gui.game_loading.resources.consts import Milestones as Milestones
from gui.hangar_cameras.hangar_camera_common import CameraMovementStates as CameraMovementStates, CameraRelatedEvents as CameraRelatedEvents
from gui.hangar_presets.obsolete.hangar_gui_helpers import ifComponentAvailable as ifComponentAvailable
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.lobby.hangar.base.sound_constants import HangarSoundStates as HangarSoundStates
from gui.limited_ui.lui_rules_storage import LUI_RULES as LUI_RULES
from gui.prb_control import prb_getters as prb_getters
from gui.prb_control.ctrl_events import g_prbCtrlEvents as g_prbCtrlEvents
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.prestige.prestige_helpers import hasVehiclePrestige as hasVehiclePrestige
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared import event_dispatcher as shared_events
from gui.shared import events as events
from gui.shared.events import AmmunitionPanelViewEvent as AmmunitionPanelViewEvent, LobbySimpleEvent as LobbySimpleEvent
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.processors.tankman import TankmanAutoReturn as TankmanAutoReturn
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from gui.shared.notifications import NotificationPriorityLevel as NotificationPriorityLevel
from gui.shared.tutorial_helper import getTutorialGlobalStorage as getTutorialGlobalStorage
from gui.shared.utils import decorators as decorators
from gui.shared.utils.functions import makeTooltip as makeTooltip
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA as REQ_CRITERIA
from gui.sounds.filters import States as States, StatesGroup as StatesGroup
from helpers import dependency as dependency
from nation_change_helpers.client_nation_change_helper import getChangeNationTooltip as getChangeNationTooltip
from personal_missions import PM_SWITCHES as PM_SWITCHES
from renewable_subscription_common.schema import renewableSubscriptionsConfigSchema as renewableSubscriptionsConfigSchema
from shared_utils import nextTick as nextTick
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.game_control import IBattlePassController as IBattlePassController, IBattleRoyaleController as IBattleRoyaleController, IComp7Controller as IComp7Controller, IEpicBattleMetaGameController as IEpicBattleMetaGameController, IHangarGuiController as IHangarGuiController, IIGRController as IIGRController, ILimitedUIController as ILimitedUIController, ILootBoxSystemController as ILootBoxSystemController, IMapboxController as IMapboxController, IMarathonEventsController as IMarathonEventsController, IPromoController as IPromoController, IRankedBattlesController as IRankedBattlesController
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.offers import IOffersBannerController as IOffersBannerController
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from skeletons.helpers.statistics import IStatisticsCollector as IStatisticsCollector
from sound_gui_manager import CommonSoundSpaceSettings as CommonSoundSpaceSettings
from tutorial.control.context import GLOBAL_FLAG as GLOBAL_FLAG
from frameworks.wulf import Window as Window, View as View
from gui.marathon.marathon_event import MarathonEvent as MarathonEvent
_logger: Any
_HELP_LAYOUT_RESTRICTED_LAYERS: tuple

class Hangar(LobbySelectableView, HangarMeta, IGlobalListener):
    _COMMON_SOUND_SPACE: Any
    __background_alpha__ = 0.0
    itemsCache: Any
    igrCtrl: Any
    lobbyContext: Any
    statsCollector: Any
    gui: Any
    hangarSpace: Any
    rankedController: Any
    epicController: Any
    battlePassController: Any
    battleRoyaleController: Any
    _settingsCore: Any
    _promoController: Any
    _connectionMgr: Any
    _offersBannerController: Any
    __mapboxCtrl: Any
    __marathonCtrl: Any
    __comp7Controller: Any
    __hangarGuiCtrl: Any
    __lootBoxes: Any
    __limitedUIController: Any
    __currentCarouselAlias: Any
    __isSpaceReadyForC11n: Any
    __isVehicleReadyForC11n: Any
    __isVehicleCameraReadyForC11n: Any
    __isUnitJoiningInProgress: Any
    __urlMacros: Any
    __teaser: Any
    __timer: Any
    __comp7BanTimer: Any
    def __init__(self, **kwargs):
        ...
    @property
    def ammoPanel(self):
        ...
    @property
    def paramsPanel(self):
        ...
    @property
    def crewWidget(self):
        ...
    @property
    def researchPanel(self):
        ...
    @property
    def headerComponent(self):
        ...
    @property
    def alertMessage(self):
        ...
    @property
    def carouselComponent(self):
        ...
    def onCacheResync(self, reason, diff):
        ...
    def onPlayerStateChanged(self, entity, roster, accountInfo):
        ...
    def onUnitPlayerStateChanged(self, pInfo):
        ...
    def onUnitPlayersListChanged(self):
        ...
    def onPrbEntitySwitched(self):
        ...
    def onEnqueued(self, queueType, *args):
        ...
    def onDequeued(self, queueType, *args):
        ...
    def onRankedUpdate(self):
        ...
    def onEscape(self):
        ...
    def hideTeaser(self):
        ...
    def onTeaserClick(self):
        ...
    def showHelpLayout(self):
        ...
    def closeHelpLayout(self):
        ...
    def animateHangarSubItems(self, isShow):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __updateDogTagsState(self):
        ...
    def __onWindowLoaded(self, uniqueID, newStatus):
        ...
    def __switchCarousels(self, force=False):
        ...
    def __updateAmmoPanel(self):
        ...
    def __updateParams(self):
        ...
    def __updateVehicleInResearchPanel(self):
        ...
    def __updateNavigationInResearchPanel(self):
        ...
    def __updateHeaderComponent(self):
        ...
    # decorador original: @decorators.adisp_process(...)
    def __returnCrew(self):
        ...
    def __updateCrew(self):
        ...
    def __updateEasyTankEquipState(self, *_):
        ...
    def __onWaitingShown(self, _):
        ...
    def __handleFightButtonUpdated(self, _):
        ...
    def __handleSelectedEntityUpdated(self, event):
        ...
    def _highlight3DEntityAndShowTT(self, entity):
        ...
    def _fade3DEntityAndHideTT(self, entity):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def _onUnregisterFlashComponent(self, viewPy, alias):
        ...
    def __onEpicBattleUpdated(self, *_):
        ...
    def __updateAll(self):
        ...
    def __onCurrentVehicleChanged(self):
        ...
    def __onSpaceRefresh(self):
        ...
    def __onSpaceCreate(self):
        ...
    def __onVehicleLoading(self):
        ...
    def __onVehicleLoaded(self):
        ...
    def __onIgrTypeChanged(self, *args):
        ...
    def __updateState(self, force=False):
        ...
    def _packBtn(self, visible=False, enabled=False, tooltip='', isNew=False):
        ...
    def __onEntityChanged(self):
        ...
    def __onEntityUpdated(self, *_):
        ...
    def __onVehicleClientStateChanged(self, modifiedCDs):
        ...
    def __onServerSettingChanged(self, diff):
        ...
    def _onConfigModelUpdated(self, gpKey):
        ...
    def __onSettingsChanged(self, diff):
        ...
    def __checkVehicleCameraState(self):
        ...
    def __onOptDeviceClick(self, event):
        ...
    def __oAmmunitionPanelViewClose(self, _):
        ...
    def __onUnitJoined(self, _, __):
        ...
    def __onPrebattleInvitationAccepted(self, _, __):
        ...
    def __onResetUnitJoiningProgress(self):
        ...
    def __updateCarouselEventEntryState(self):
        ...
    # decorador original: @ifComponentAvailable(...)
    def __updatePrestigeProgressWidget(self):
        ...
    # decorador original: @ifComponentAvailable(...)
    def __updateAlertMessage(self, *_):
        ...
    def __updateAlertBlock(self, visible, data, callbacks):
        ...
    def __onInventoryUpdate(self, invDiff):
        ...
    def __updateCustomizationHint(self):
        ...

def _predicateHelpLayoutRestrictedWindow(window):
    ...
def _predicateHelpLayoutRestrictedView(view):
    ...
