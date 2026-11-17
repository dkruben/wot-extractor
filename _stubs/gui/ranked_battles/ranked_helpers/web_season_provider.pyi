# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/ranked_battles/ranked_helpers/web_season_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
import logging as logging
import time as time
import BigWorld as BigWorld
import Event as Event
import constants as constants
from adisp import adisp_process as adisp_process
from helpers import dependency as dependency
from helpers.time_utils import ONE_MINUTE as ONE_MINUTE
from skeletons.gui.web import IWebController as IWebController
from gui.wgcg.rank.contexts import RankedPositionCtx as RankedPositionCtx
_logger: Any
_WEB_AVAILABLE_SYNC_TIME = 2
_LEAGUE_SYNC_TIME: Any
WebSeasonInfo: Any
UNDEFINED_LEAGUE_ID = 0
UNDEFINED_WEB_INFO: Any
TOP_LEAGUE_ID = 1

class RankedWebSeasonProvider(object):
    __webController: Any
    __slots__: tuple
    onInfoUpdated: Any
    __isStarted: Any
    __callbackID: Any
    __lastUpdateTime: Any
    __webSeasonInfo: Any
    __fakeInfo: Any
    def __init__(self):
        ...
    @property
    def isStarted(self):
        ...
    @property
    def lastUpdateTime(self):
        ...
    @property
    def seasonInfo(self):
        ...
    def clear(self):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def _setFakeSeasonInfo(self, league=0, position=None, isSprinter=False, isTop=False):
        ...
    # decorador original: @adisp_process
    def __invoke(self):
        ...
    def __getInvokeDelay(self):
        ...
