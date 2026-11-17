# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/notification/NotificationListView.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from adisp import adisp_process as adisp_process
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.Scaleform.daapi.view.meta.NotificationsListMeta import NotificationsListMeta as NotificationsListMeta
from gui.Scaleform.genConsts.NOTIFICATIONS_CONSTANTS import NOTIFICATIONS_CONSTANTS as NOTIFICATIONS_CONSTANTS
from gui.Scaleform.locale.MESSENGER import MESSENGER as MESSENGER
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.impl.gen import R as R
from gui.shared.formatters import icons as icons
from gui.shared.notifications import NotificationGroup as NotificationGroup
from helpers import dependency as dependency
from helpers.i18n import makeString as _ms
from messenger.formatters import TimeFormatter as TimeFormatter
from notification import NotificationMVC as NotificationMVC
from notification.BaseNotificationView import BaseNotificationView as BaseNotificationView
from notification.settings import LIST_SCROLL_STEP_FACTOR as LIST_SCROLL_STEP_FACTOR, NOTIFICATION_STATE as NOTIFICATION_STATE
from notification.utils import dynamicNotificationRegister as dynamicNotificationRegister
from skeletons.gui.game_control import IPromoController as IPromoController, IWinbackController as IWinbackController
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache

class NotificationListView(NotificationsListMeta, BaseNotificationView):
    _lobbyContext: Any
    __itemsCache: Any
    __winbackController: Any
    __promoController: Any
    __guiLoader: Any
    __currentGroup: Any
    __countersLabels: Any
    def __init__(self, **kwargs):
        ...
    def onClickAction(self, typeID, entityID, action):
        ...
    def onGroupChange(self, groupIdx):
        ...
    def getMessageActualTime(self, msTime):
        ...
    def onCheckNewsClick(self):
        ...
    def registerGFNotification(self, component, alias, gfViewName, isPopUp, linkageData):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __setInitData(self):
        ...
    def __updateWinbackPromo(self, *_):
        ...
    def __onServerSettingsChange(self, diff):
        ...
    def __updateCounters(self):
        ...
    def __setNotificationList(self):
        ...
    def __getMessagesList(self):
        ...
    def __getEmptyListMsg(self, hasMessages):
        ...
    def __onNotificationReceived(self, notification):
        ...
    def __onNotificationUpdated(self, notification, isStateChanged):
        ...
    def __onNotificationRemoved(self, typeID, entityID, groupID, countOnce):
        ...
    def __makeTabItemVO(self, tabId, label, tooltip):
        ...
    def __getListVO(self, notificaton):
        ...
    # decorador original: @adisp_process
    def __openPromoScreen(self):
        ...
