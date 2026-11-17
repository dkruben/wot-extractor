# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/hangar_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from CurrentVehicle import g_currentVehicle as g_currentVehicle, g_currentPreviewVehicle as g_currentPreviewVehicle
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.lobby_state_machine.routable_view import IRoutableView as IRoutableView
from gui.lobby_state_machine.router import SubstateRouter as SubstateRouter
from gui.shared.event_dispatcher import showVehicleHubOverview as showVehicleHubOverview, showLobbyMenu as showLobbyMenu
from gui.impl.lobby.hangar.presenters.main_menu_presenter import MainMenuPresenter as MainMenuPresenter
from gui.impl.pub import WindowImpl as WindowImpl
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from halloween.gui.impl.lobby.hw_helpers.anomalies_helpers import hasNewAnomalies as hasNewAnomalies, isAnomaliesSystemAvailable as isAnomaliesSystemAvailable
from halloween.gui.impl.lobby.hw_helpers.bestiary_helper import getEnemyRole as getEnemyRole, isEnemyUnlocked as isEnemyUnlocked
from halloween.gui.impl.lobby.widgets.gsw_view import GswPresenter as GswPresenter
from frameworks.wulf import WindowStatus as WindowStatus, WindowFlags as WindowFlags
from halloween.gui.impl.lobby.widgets.hw_loadout import HalloweenLoadoutPresenter as HalloweenLoadoutPresenter
from halloween.gui.impl.lobby.widgets.vehicle_title_view import VehicleTitlePresenter as VehicleTitlePresenter
from halloween.gui.shared.events import HWHangarEvent as HWHangarEvent
from halloween.uilogging.loggers import HWMetricsLogger as HWMetricsLogger
from halloween.uilogging.logging_constants import HWLogKeys as HWLogKeys
from items.vehicles import getVehicleType as getVehicleType
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.app_loader import sf_lobby as sf_lobby
from gui.impl.gen import R as R
from gui.impl.lobby.common.tooltips.extended_text_tooltip import ExtendedTextTooltip as ExtendedTextTooltip
from gui.impl.lobby.hangar.presenters.utils import getSharedMenuItems as getSharedMenuItems
from gui.prb_control import prbEntityProperty as prbEntityProperty
from gui.shared import g_eventBus as g_eventBus, events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from halloween.gui.impl.gen.view_models.views.lobby.hangar_view_model import HangarViewModel as HangarViewModel
from halloween.gui.impl.gen.view_models.views.lobby.widgets.hangar_carousel_vehicle_view_model import VehicleStates as VehicleStates
from halloween.gui.impl.lobby.hw_helpers import getVehicleState as getVehicleState, fillGiftVehicleModel as fillGiftVehicleModel, getEnemyByArtefactID as getEnemyByArtefactID
from halloween.gui.impl.lobby.widgets.carousel_view import CarouselView as CarouselView
from halloween.gui.impl.lobby.widgets.difficulty_view import DifficultyView as DifficultyView
from halloween.gui.impl.lobby.widgets.meta_view import MetaWidgetView as MetaWidgetView
from halloween.gui.halloween_account_settings import AccountSettingsKeys as AccountSettingsKeys, getSettings as getSettings, setSettings as setSettings
from halloween.gui.shared.event_dispatcher import showHalloweenShopVehicle as showHalloweenShopVehicle, showIntroVideo as showIntroVideo, showInfoPage as showInfoPage, showComparisonWindow as showComparisonWindow, showBestiaryWindow as showBestiaryWindow, showAnomaliesWindow as showAnomaliesWindow
from halloween.skeletons.halloween_anomalies_controller import IHalloweenAnomaliesController as IHalloweenAnomaliesController
from halloween.skeletons.halloween_artefacts_controller import IHalloweenArtefactsController as IHalloweenArtefactsController
from halloween.skeletons.halloween_bestiary_controller import IHalloweenBestiaryController as IHalloweenBestiaryController
from halloween.skeletons.halloween_controller import IHalloweenController as IHalloweenController
from halloween.gui.sounds.sound_constants import HANGAR_SOUND_SETTINGS as HANGAR_SOUND_SETTINGS
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.impl import IGuiLoader as IGuiLoader, INotificationWindowController as INotificationWindowController
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from halloween.gui.impl.lobby.base_view import SwitcherPresenter as SwitcherPresenter
from gui.shared.events import GUICommonEvent as GUICommonEvent
from halloween.gui.game_control.halloween_bestiary_controller import EnemyData as EnemyData
_BACKGROUND_ALPHA = 0.0
_logger: Any

# base nao representavel no stub: ViewComponent[...]
class HangarView(IRoutableView):
    _appLoader: Any
    _guiLoader: Any
    _hwController: Any
    _hwAnomaliesCtrl: Any
    _hwArtefactsCtrl: Any
    _hwBestiaryCtrl: Any
    _hangarSpace: Any
    _notificationMgr: Any
    _COMMON_SOUND_SPACE = HANGAR_SOUND_SETTINGS
    __metaWidget: Any
    _router: Any
    __inputManager: Any
    __uiLogger: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def getRouterModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def selectSlideByArtefact(self, artefactID):
        ...
    def updateSlide(self):
        ...
    # decorador original: @prbEntityProperty
    def prbEntity(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _onShown(self):
        ...
    def _finalize(self):
        ...
    def _initializeRouter(self):
        ...
    def _getEvents(self):
        ...
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    def _getListeners(self):
        ...
    def _getChildComponents(self):
        ...
    def __refresh(self, event):
        ...
    def __selectNextSlide(self):
        ...
    @property
    def __selectedArtefactID(self):
        ...
    @property
    def __selectedMissionIndex(self):
        ...
    def __onVehicleLockUpdated(self, *args):
        ...
    def __onArtefactStatusUpdated(self, _):
        ...
    def __onArtefactSettingsUpdated(self):
        ...
    def __onSlide(self, args):
        ...
    def __onWidgetsUpdate(self, args):
        ...
    # decorador original: @sf_lobby
    def __app(self):
        ...
    def __fillGiftVehicle(self):
        ...
    def __fillCore(self):
        ...
    def __updateVehicleLocked(self):
        ...
    def __updateAnomaliesInfo(self):
        ...
    def __updateBestiaryInfo(self):
        ...
    def __onAboutClick(self):
        ...
    def __onEnemyClick(self):
        ...
    def __onBestiaryClick(self):
        ...
    def __onComparisonClick(self):
        ...
    def __onAnomaliesClick(self):
        ...
    def __onPreview(self):
        ...
    def __onTasksClick(self):
        ...
    def __onPacksClick(self):
        ...
    def __onCurrentVehicleChanged(self):
        ...
    def __escapeHandler(self):
        ...
    def __windowStatusChanged(self, uniqueID, newStatus):
        ...
    def __onViewLoaded(self):
        ...

class HangarWindow(WindowImpl):
    def __init__(self, layer, **kwargs):
        ...
