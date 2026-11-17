# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/game_control/ls_chat_by_difficulty_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems, viewvalues as viewvalues
import gui.shared
from constants import Configs as Configs
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.app_loader import sf_lobby as sf_lobby
from gui.shared.utils.functions import getViewName as getViewName
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import ChannelCarouselEvent as ChannelCarouselEvent, GUICommonEvent as GUICommonEvent
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from last_stand.gui import ls_account_settings as ls_account_settings
from last_stand.gui.ls_account_settings import AccountSettingsKeys as AccountSettingsKeys
from last_stand.gui.ls_gui_constants import DifficultyLevel as DifficultyLevel, LAZY_CHANNEL as LAZY_CHANNEL
from last_stand.skeletons.difficulty_level_controller import IDifficultyLevelController as IDifficultyLevelController
from last_stand.skeletons.ls_controller import ILSController as ILSController
from last_stand.skeletons.ls_global_chat_controller import ILSDifficultyChatController as ILSDifficultyChatController
from helpers import dependency as dependency
from messenger.ext.channel_num_gen import getClientID4LazyChannel as getClientID4LazyChannel, getOrder4LazyChannel as getOrder4LazyChannel
from gui.prb_control.events_dispatcher import _defCarouselItemCtx as _defCarouselItemCtx
from gui.Scaleform.framework.managers.containers import VIEW_SEARCH_CRITERIA as VIEW_SEARCH_CRITERIA
from messenger.gui.Scaleform.data.ChannelsCarouselHandler import ChannelFindCriteria as ChannelFindCriteria
from messenger.gui.events_dispatcher import showLazyChannelWindow as showLazyChannelWindow
from messenger.gui.Scaleform.view.lobby import MESSENGER_VIEW_ALIAS as MESSENGER_VIEW_ALIAS
from messenger.inject import channelsCtrlProperty as channelsCtrlProperty
from frameworks.wulf import WindowLayer as WindowLayer
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext

class LSDifficultyChatController(ILSDifficultyChatController, IGlobalListener):
    lsCtrl: Any
    lsDifficultyCtrl: Any
    lobbyContext: Any
    SYS_CHANNELS_PARAM_KEY = Configs.SYSTEM_CHANNELS.value
    __clientIDs: Any
    __handlers: Any
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
    def removeChannels(self):
        ...
    def removeChannel(self, difficulty):
        ...
    def addChannel(self, difficulty):
        ...
    def _update(self, *args, **kwargs):
        ...
    def _onServerSettingChanged(self, diff):
        ...
    def __clear(self):
        ...
    def __handlerMinimizeAll(self, _):
        ...
