# wot-extractor: STUB (.pyi) gerado a partir de sources/res/server_side_replay/scripts/client/server_side_replay/gui/impl/gen/view_models/views/lobby/root_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from server_side_replay.gui.impl.gen.view_models.views.lobby.enums import ReplaysViews as ReplaysViews
from frameworks.wulf import ViewModel as ViewModel
from server_side_replay.gui.impl.gen.view_models.views.lobby.pages.best_replays_model import BestReplaysModel as BestReplaysModel
from server_side_replay.gui.impl.gen.view_models.views.lobby.pages.find_replay_model import FindReplayModel as FindReplayModel
from server_side_replay.gui.impl.gen.view_models.views.lobby.pages.my_replays_model import MyReplaysModel as MyReplaysModel
from server_side_replay.gui.impl.gen.view_models.views.lobby.sidebar_model import SidebarModel as SidebarModel

class RootViewModel(ViewModel):
    __slots__: tuple
    onClose: Any
    def __init__(self, properties=5, commands=1):
        ...
    @property
    def sidebar(self):
        ...
    @staticmethod
    def getSidebarType():
        ...
    @property
    def bestReplays(self):
        ...
    @staticmethod
    def getBestReplaysType():
        ...
    @property
    def myReplays(self):
        ...
    @staticmethod
    def getMyReplaysType():
        ...
    @property
    def findReplay(self):
        ...
    @staticmethod
    def getFindReplayType():
        ...
    def getPageViewId(self):
        ...
    def setPageViewId(self, value):
        ...
    def _initialize(self):
        ...
