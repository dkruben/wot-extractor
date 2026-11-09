# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/impl/lobby/newbie_advertising_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from PlayerEvents import g_playerEvents as g_playerEvents
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from story_mode.account_settings import setNewbieAdvertisingScreenSeen as setNewbieAdvertisingScreenSeen
from story_mode.gui.impl.gen.view_models.views.lobby.advertising_view_model import AdvertisingViewModel as AdvertisingViewModel
from story_mode.uilogging.story_mode.consts import LogButtons as LogButtons
from story_mode.uilogging.story_mode.loggers import NewbieAdvertisingViewLogger as NewbieAdvertisingViewLogger

class NewbieAdvertisingView(ViewImpl):
    __slots__: tuple
    layoutID: Any
    _uiLogger: Any
    def __init__(self, layoutID=None):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def __onClose(self):
        ...
    def __onCloseClicked(self):
        ...
    def __onSubmitClicked(self):
        ...
    def __onDisconnected(self):
        ...

class NewbieAdvertisingWindow(LobbyNotificationWindow):
    def __init__(self, layoutID):
        ...
