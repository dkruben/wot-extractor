# wot-extractor: STUB (.pyi) gerado a partir de sources/res/server_side_replay/scripts/client/server_side_replay/gui/wgcg/providers/server_replays_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
from copy import deepcopy as deepcopy
import typing as typing
from server_side_replay.gui.wgcg.providers.base_provider import BaseProvider as BaseProvider, RequestSettings as RequestSettings, UpdatePeriodType as UpdatePeriodType
from server_side_replay.gui.wgcg.data_wrappers.server_replays import DataNames as DataNames
from server_side_replay.gui.wgcg.providers.example_responses.server_replays import EXAMPLE_DATA as EXAMPLE_DATA
from server_side_replay.gui.wgcg.server_replays import contexts as contexts
from helpers import dependency as dependency
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from typing import Optional as Optional, Dict as Dict, Any as Any
from data_structures import DictObj as DictObj

class ServerReplaysProvider(BaseProvider):
    __connectionMgr: _Any
    __lastShownReplay: _Any
    def getBestReplays(self, useFake=False, **kwargs):
        ...
    def getTopReplays(self, useFake=False):
        ...
    def getMyReplays(self, useFake=False, **kwargs):
        ...
    def getReplayLink(self, replayID, useFake=False):
        ...
    def findReplay(self, replayName, useFake=False):
        ...
    def saveLastShownReplay(self, value):
        ...
    @property
    def _dataNameContainer(self):
        ...
    @property
    def _isEnabled(self):
        ...
    @property
    def _fakeDataStorage(self):
        ...
    def _getSettings(self):
        ...
