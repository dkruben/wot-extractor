# wot-extractor: STUB (.pyi) gerado a partir de sources/res/server_side_replay/scripts/client/server_side_replay/gui/impl/lobby/pages/find_replay_page.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from past.builtins import unicode as unicode
from typing import TYPE_CHECKING as TYPE_CHECKING
import BigWorld as BigWorld
from BattleReplay import BattleReplay as BattleReplay
from adisp import adisp_process as adisp_process
from server_side_replay.gui.impl.gen.view_models.views.lobby.pages.find_replay_model import FindReplayModel as FindReplayModel
from server_side_replay.gui.impl.gen.view_models.views.lobby.enums import ReplaysViews as ReplaysViews
from server_side_replay.gui.impl.gen.view_models.views.lobby.table_base_model import State as State
from gui.impl.gui_decorators import args2params as args2params
from server_side_replay.gui.impl.lobby.pages import PageSubModelPresenter as PageSubModelPresenter
from server_side_replay.gui.impl.lobby.utils import WebReplaysHelper as WebReplaysHelper
from server_side_replay.gui.wgcg.data_wrappers.server_replays import DataNames as DataNames
from server_side_replay.gui.wgcg.providers.server_replays_provider import ServerReplaysProvider as ServerReplaysProvider
from typing import Optional as Optional
from server_side_replay.gui.wgcg.data_wrappers import server_replays as server_replays
_logger: Any

class FindReplayPage(PageSubModelPresenter):
    __foundReplay: Any
    __serverReplayProvider: Any
    def __init__(self, viewModel, parentView):
        ...
    @property
    def pageId(self):
        ...
    @property
    def viewModel(self):
        ...
    def initialize(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def __updateState(self):
        ...
    def __onRefresh(self):
        ...
    # decorador original: @args2params(...)
    def __onFind(self, searchText):
        ...
    # decorador original: @adisp_process
    def __onWatch(self):
        ...
    def __onDataReceived(self, dataName, data):
        ...
    def __onDataFailed(self, dataName):
        ...
