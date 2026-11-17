# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/page/chats_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from constants import Configs as Configs
from frameworks.wulf import WindowLayer as WindowLayer
from gui.Scaleform.framework.managers.containers import POP_UP_CRITERIA as POP_UP_CRITERIA
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.impl.gen.view_models.views.lobby.page.footer.chat_model import ChatModel as ChatModel
from gui.impl.gen.view_models.views.lobby.page.footer.message_model import MessageModel as MessageModel
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events
from gui.shared.events import ChannelCarouselEvent as ChannelCarouselEvent, ChannelManagementEvent as ChannelManagementEvent
from helpers import dependency as dependency, i18n as i18n
from helpers.server_settings import serverSettingsChangeListener as serverSettingsChangeListener
from messenger import MessengerEntry as MessengerEntry
from messenger.gui.Scaleform.view.lobby import MESSENGER_VIEW_ALIAS as MESSENGER_VIEW_ALIAS
from messenger.m_constants import MESSENGER_SCOPE as MESSENGER_SCOPE, LAZY_CHANNEL as LAZY_CHANNEL
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
_logger: Any

# base nao representavel no stub: ViewComponent[...]
class ChatsPresenter:
    __appLoader: Any
    __lobbyContext: Any
    __carouselHandler: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _finalize(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def _getListeners(self):
        ...
    # decorador original: @serverSettingsChangeListener(...)
    def __onServerSettingChanged(self, diff):
        ...
    # decorador original: @args2params(...)
    def __onWindowAnchorPositionUpdated(self, x, y, width, height):
        ...
    def __onWindowPopulate(self, event):
        ...
    def __onWindowMinimize(self, event):
        ...
    def __requestChange(self, clientID, key, value):
        ...
    # decorador original: @args2params(...)
    def __onViewMessageAction(self, sessionID, x, y, width, height):
        ...
    # decorador original: @args2params(...)
    def __onDeleteMessageAction(self, sessionID):
        ...
    # decorador original: @args2params(...)
    def __onChatsAction(self, x, y, width, height):
        ...
    def __updateModel(self, *_):
        ...
    def __getChannelsList(self):
        ...

def _convertDPItemToModel(item):
    ...
