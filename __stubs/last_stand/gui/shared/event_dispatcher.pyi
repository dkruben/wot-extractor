# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/shared/event_dispatcher.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from CurrentVehicle import HeroTankPreviewAppearance as HeroTankPreviewAppearance
from frameworks.wulf import WindowLayer as WindowLayer
from BWUtil import AsyncReturn as AsyncReturn
from gui import GUI_SETTINGS as GUI_SETTINGS
from gui.lootbox_system.base.common import ViewID as ViewID, Views as Views
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.impl.common.fade_manager import UseFading as UseFading
from gui.impl.gen import R as R
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, g_eventBus as g_eventBus, events as events
from gui.shared.event_dispatcher import showShop as showShop, _getModuleInfoViewName as _getModuleInfoViewName, showBrowserOverlayView as showBrowserOverlayView, findAndLoadWindow as findAndLoadWindow, selectVehicleInHangar as selectVehicleInHangar
from last_stand.gui.ls_gui_constants import LS_INFO_PAGE_KEY as LS_INFO_PAGE_KEY, LS_INTRO_VIDEO_KEY as LS_INTRO_VIDEO_KEY
from last_stand.skeletons.ls_artefacts_controller import ILSArtefactsController as ILSArtefactsController
from last_stand.skeletons.ls_controller import ILSController as ILSController
from skeletons.gui.game_control import ILootBoxSystemController as ILootBoxSystemController
from skeletons.gui.impl import INotificationWindowController as INotificationWindowController
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from last_stand.gui.ls_account_settings import AccountSettingsKeys as AccountSettingsKeys, getSettings as getSettings
from last_stand.gui.impl.lobby.tank_setup.dialogs.confirm_dialog import LSTankSetupConfirmDialog as LSTankSetupConfirmDialog
from helpers import dependency as dependency
from gui.impl.pub.notification_commands import EventNotificationCommand as EventNotificationCommand, NotificationEvent as NotificationEvent, WindowNotificationCommand as WindowNotificationCommand
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from wg_async import wg_await as wg_await, wg_async as wg_async
from last_stand.gui.scaleform.genConsts.LAST_STAND_HANGAR_ALIASES import LAST_STAND_HANGAR_ALIASES as LAST_STAND_HANGAR_ALIASES

# decorador original: @dependency.replace_none_kwargs(...)
def _getUrl(urlName=None, url=None, lobbyContext=None):
    ...
def getLoadedViewByLayoutID(layoutID):
    ...
def isViewLoaded(layoutID):
    ...
def showHangar():
    ...
def isHangarLoaded():
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def showMetaIntroView(forceOpen=True, parent=None, lsController=None):
    ...
def showVehiclePreview(**kwargs):
    ...
def showHeroTankPreview(vehTypeCompDescr, previewAlias=..., previousBackAlias=None, previewBackCb=None, hangarVehicleCD=None, backOutfit=None, backBtnLabel='', isHiddenMenu=True, isKingReward=False):
    ...
def showRewardPathView(openFromQuestCard=False):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def showPromoWindowView(forceOpen=False, notificationsMgr=None):
    ...
def showDifficultyView(level, useQueue=False):
    ...
def showNarrationWindowView(useQueue=False):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def showIntroVideo(lsController=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def showInfoPage(lsController=None):
    ...
def showBattleResult(arenaUniqueID):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def showLootBoxMainView(eventName, lootBoxCtrl=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def showLootBoxMainViewInQueue(eventName, notificationsMgr=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def showLSShopAll(lsArtefactsController=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def showLSShopBundle(bundleUrl, lsArtefactsController=None):
    ...
# decorador original: @wg_async
def showTankSetupConfirmDialog(items, vehicle=None, startState=None, parent=None):
    ...
# decorador original: @wg_async
def showAbilitiesIncompleteConfirm(parent=None):
    ...
def showModuleInfo(itemCD, vehicleDescr):
    ...
def closeViewsByID(layoutIDs):
    ...
# decorador original: @UseFading(...)
def selectVehicleInHangarWithFade(itemCD, loadHangar=True):
    ...
def showAttachmentRewardWindow(element, isFirstEntry, useQueue=True):
    ...
def showStageRewardWindow(resourceID, isReward=False, useQueue=False):
    ...
