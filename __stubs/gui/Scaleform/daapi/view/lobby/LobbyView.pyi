# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/LobbyView.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import constants as constants
import gui as gui
from frameworks.wulf import WindowLayer as WindowLayer
from gui import SystemMessages as SystemMessages
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.header import battle_selector_items as battle_selector_items
from gui.Scaleform.daapi.view.lobby.vehicle_preview.vehicle_preview import VEHICLE_PREVIEW_ALIASES as VEHICLE_PREVIEW_ALIASES
from gui.Scaleform.daapi.view.meta.LobbyPageMeta import LobbyPageMeta as LobbyPageMeta
from gui.Scaleform.framework.entities.View import View as View, ViewKey as ViewKey, ViewKeyDynamic as ViewKeyDynamic
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor as InjectComponentAdaptor
from gui.Scaleform.framework.managers.view_lifecycle_watcher import IViewLifecycleHandler as IViewLifecycleHandler, ViewLifecycleWatcher as ViewLifecycleWatcher
from gui.Scaleform.genConsts.PERSONAL_MISSIONS_ALIASES import PERSONAL_MISSIONS_ALIASES as PERSONAL_MISSIONS_ALIASES
from gui.Scaleform.genConsts.PREBATTLE_ALIASES import PREBATTLE_ALIASES as PREBATTLE_ALIASES
from gui.Scaleform.genConsts.RANKEDBATTLES_ALIASES import RANKEDBATTLES_ALIASES as RANKEDBATTLES_ALIASES
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES as SYSTEM_MESSAGES
from gui.hangar_cameras.hangar_camera_common import CameraRelatedEvents as CameraRelatedEvents
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.prb_control.dispatcher import g_prbLoader as g_prbLoader
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events
from gui.shared.system_factory import registerLifecycleHandledSubViews as registerLifecycleHandledSubViews, collectLifecycleHandledSubViews as collectLifecycleHandledSubViews, collectViewsForMonitoring as collectViewsForMonitoring, collectDynamicViewsForMonitoring as collectDynamicViewsForMonitoring
from helpers import dependency as dependency, i18n as i18n, uniprof as uniprof
from messenger.m_constants import PROTO_TYPE as PROTO_TYPE
from messenger.proto import proto_getter as proto_getter
from skeletons.gui.app_loader import IWaitingWidget as IWaitingWidget
from skeletons.gui.game_control import IIGRController as IIGRController, IMapsTrainingController as IMapsTrainingController, IWalletController as IWalletController, IHangarGuiController as IHangarGuiController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.impl.pub.view_component import ViewComponent as ViewComponent
_logger: Any

class _LobbySubViewsLifecycleHandler(IViewLifecycleHandler):
    __WAITING_LBL = 'loadPage'
    __DYNAMIC_VIEWS: tuple
    __loadingSubViews: Any
    __isWaitingVisible: Any
    def __init__(self):
        ...
    def onViewLoading(self, view):
        ...
    def onViewCreated(self, view):
        ...
    def onViewDestroyed(self, view):
        ...
    def __invalidateWaitingStatus(self):
        ...

class LobbyPanelInjector(InjectComponentAdaptor, IGlobalListener):
    _viewType: Any
    def __init__(self):
        ...
    def onPrbEntitySwitched(self):
        ...
    def destroy(self):
        ...
    def _populate(self):
        ...
    def _makeInjectView(self):
        ...
    def _getViewType(self):
        ...

class LobbyHeaderInject(LobbyPanelInjector):
    _hangarGuiCtrl: Any
    def _getViewType(self):
        ...

class LobbyFooterInject(LobbyPanelInjector):
    _hangarGuiCtrl: Any
    def _getViewType(self):
        ...

class LobbyView(LobbyPageMeta, IWaitingWidget, IGlobalListener):
    itemsCache: Any
    igrCtrl: Any
    lobbyContext: Any
    wallet: Any
    mapsTrainingController: Any
    __currIgrType: Any
    __viewLifecycleWatcher: Any
    __oldStyleViewMode: Any
    def __init__(self, ctx=None):
        ...
    def create(self):
        ...
    # decorador original: @proto_getter(...)
    def bwProto(self):
        ...
    def showWaiting(self, messageID, softStart=False, showBg=True):
        ...
    def hideWaiting(self):
        ...
    def moveSpace(self, dx, dy, dz):
        ...
    def notifyCursorOver3dScene(self, isOver3dScene):
        ...
    def notifyCursorDragging(self, isDragging):
        ...
    def setRequiresOldStyle(self, value):
        ...
    def _updateRequiresOldStyle(self, alias):
        ...
    # decorador original: @uniprof.regionDecorator(...)
    def _populate(self):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    # decorador original: @uniprof.regionDecorator(...)
    def _dispose(self):
        ...
    def onPrbEntitySwitched(self):
        ...
    def __onServerSettingsChange(self, _):
        ...
    def __updateBattleSelector(self):
        ...
    def __showHelpLayout(self, _):
        ...
    def __closeHelpLayout(self, _):
        ...
    def __handleScreenShotMade(self, event):
        ...
    def __hideSubContainerItems(self, _):
        ...
    def __revealSubContainerItems(self, _):
        ...
    def __onIgrTypeChanged(self, roomType, xpFactor):
        ...
    def __onWalletChanged(self, _):
        ...
