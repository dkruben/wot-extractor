# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/game_control/halloween_global_chat_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import gui.shared
from constants import Configs as Configs
from gui.app_loader import sf_lobby as sf_lobby
from gui.shared.utils.functions import getViewName as getViewName
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import ChannelCarouselEvent as ChannelCarouselEvent
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from halloween.gui import halloween_account_settings as halloween_account_settings
from halloween.gui.halloween_account_settings import AccountSettingsKeys as AccountSettingsKeys
from halloween.gui.halloween_gui_constants import LAZY_CHANNEL as LAZY_CHANNEL
from halloween.skeletons.halloween_controller import IHalloweenController as IHalloweenController
from halloween.skeletons.halloween_global_chat_controller import IHalloweenGlobalChatController as IHalloweenGlobalChatController
from halloween_common.halloween_constants import HALLOWEEN_CHAT_CHANNEL as HALLOWEEN_CHAT_CHANNEL
from helpers import dependency as dependency
from messenger.ext import channel_num_gen as channel_num_gen
from gui.prb_control.events_dispatcher import _defCarouselItemCtx as _defCarouselItemCtx
from gui.Scaleform.framework.managers.containers import VIEW_SEARCH_CRITERIA as VIEW_SEARCH_CRITERIA
from messenger.gui.Scaleform.data.ChannelsCarouselHandler import ChannelFindCriteria as ChannelFindCriteria
from messenger.gui.events_dispatcher import showLazyChannelWindow as showLazyChannelWindow
from messenger.gui.Scaleform.view.lobby import MESSENGER_VIEW_ALIAS as MESSENGER_VIEW_ALIAS
from messenger.inject import channelsCtrlProperty as channelsCtrlProperty
from soft_exception import SoftException as SoftException
from frameworks.wulf import WindowLayer as WindowLayer
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext

class HalloweenGlobalChatController(IHalloweenGlobalChatController, IGlobalListener):
    halloweenCtrl: Any
    lobbyContext: Any
    SYS_CHANNELS_PARAM_KEY = Configs.SYSTEM_CHANNELS.value
    __clientID: Any
    __handler: Any
    __isShown: Any
    def __init__(self):
        ...
    # decorador original: @sf_lobby
    def app(self):
        ...
    # decorador original: @channelsCtrlProperty
    def channelsCtrl(self):
        ...
    def fini(self):
        ...
    def onDisconnected(self):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def onLobbyInited(self, event):
        ...
    def onPrbEntitySwitched(self):
        ...
    def isEnabled(self):
        ...
    def isAllChatsDisabled(self):
        ...
    def isChatEnabled(self):
        ...
    def removeChannel(self):
        ...
    def addChannel(self):
        ...
    def _onServerSettingChanged(self, diff):
        ...
    def _update(self):
        ...
    def __clear(self):
        ...
    def __handlerMinimizeAll(self, _):
        ...
