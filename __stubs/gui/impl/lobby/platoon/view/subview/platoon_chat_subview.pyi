# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/platoon/view/subview/platoon_chat_subview.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.platoon.chat_message_model import ChatMessageModel as ChatMessageModel
from gui.impl.pub.view_impl import ViewImpl as ViewImpl
from helpers import dependency as dependency
from messenger import g_settings as g_settings
from messenger.formatters import TimeFormatter as TimeFormatter
from messenger.formatters.chat_message import LobbyMessageBuilder as LobbyMessageBuilder
from messenger.gui.gameface.view.gf_channel_view_interface import GFChannelViewInterface as GFChannelViewInterface
from skeletons.gui.game_control import IPlatoonController as IPlatoonController, IAnonymizerController as IAnonymizerController
from gui.impl.gen.view_models.views.lobby.platoon.chat_model import ChatModel as ChatModel
from messenger.proto.bw_chat2.wrappers import UnitMessageVO as UnitMessageVO
from messenger.gui.gameface.channels import GFChannelController as GFChannelController
_logger: Any
_R_SQUAD = R.strings.messenger.dialogs.squadChannel

class ChatSubview(ViewImpl, GFChannelViewInterface):
    __platoonCtrl: Any
    __anonymizerController: Any
    __messageCount: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def onChannelControllerInited(self, channelCtrl):
        ...
    def addMessageToView(self, message, isHistoryMessage=False):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __clearMessages(self):
        ...
    def __addMessage(self, message):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    def __onChannelControllerChanged(self, channelController):
        ...
    def __onSend(self, *args, **kwargs):
        ...
    def __onInputCleared(self):
        ...
    def __updateHeaderText(self):
        ...
    def __onAnonymizerStateChanged(self, **_):
        ...
