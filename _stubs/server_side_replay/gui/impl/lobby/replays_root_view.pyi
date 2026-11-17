# wot-extractor: STUB (.pyi) gerado a partir de sources/res/server_side_replay/scripts/client/server_side_replay/gui/impl/lobby/replays_root_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from server_side_replay.gui.impl.gen.view_models.views.lobby.root_view_model import RootViewModel as RootViewModel
from server_side_replay.gui.impl.gen.view_models.views.lobby.tab_model import TabModel as TabModel
from server_side_replay.gui.impl.gen.view_models.views.lobby.enums import ReplaysViews as ReplaysViews
from gui.impl.gui_decorators import args2params as args2params
from server_side_replay.gui.impl.lobby.replays_lobby_sounds import REPLAYS_SOUND_SPACE as REPLAYS_SOUND_SPACE
from server_side_replay.gui.impl.lobby.pages.best_replays_page import BestReplaysPage as BestReplaysPage
from server_side_replay.gui.impl.lobby.pages.my_replays_page import MyReplaysPage as MyReplaysPage
from server_side_replay.gui.impl.lobby.pages.find_replay_page import FindReplayPage as FindReplayPage
from gui.impl.pub import ViewImpl as ViewImpl
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from gui.shared.event_dispatcher import showHangar as showHangar
from server_side_replay.gui.impl.lobby.pages import PageSubModelPresenter as PageSubModelPresenter
_logger: Any

class ReplaysRootView(ViewImpl, IGlobalListener):
    __slots__: tuple
    _COMMON_SOUND_SPACE = REPLAYS_SOUND_SPACE
    __pages: Any
    __tabId: Any
    def __init__(self, layoutID, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def tabId(self):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def createContextMenu(self, event):
        ...
    def createPopOver(self, event):
        ...
    def switchPage(self, tabId, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    @property
    def __currentPage(self):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    def __initPages(self):
        ...
    def __clearPages(self):
        ...
    def __updateTabs(self):
        ...
    def __onClose(self):
        ...
    # decorador original: @args2params(...)
    def __onSideBarTabChanged(self, tabId):
        ...
