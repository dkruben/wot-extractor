# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/ranked_battles/ranked_helpers/year_position_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import RANKED_YEAR_POSITION as RANKED_YEAR_POSITION
from adisp import adisp_process as adisp_process
import constants as constants
from gui.wgcg.rank.contexts import RankedYearPositionCtx as RankedYearPositionCtx
from gui.ranked_battles.constants import YEAR_STRIPE_CLIENT_TOKEN as YEAR_STRIPE_CLIENT_TOKEN, YEAR_STRIPE_SERVER_TOKEN as YEAR_STRIPE_SERVER_TOKEN
from helpers import dependency as dependency, isPlayerAccount as isPlayerAccount
from helpers.time_utils import ONE_MINUTE as ONE_MINUTE
from skeletons.gui.web import IWebController as IWebController
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any
_WEB_AVAILABLE_SYNC_TIME = 2
_POSITION_SYNC_TIME: Any

class RankedYearPositionProvider(object):
    __itemsCache: Any
    __webController: Any
    __isStarted: Any
    __callbackID: Any
    __yearPosition: Any
    __fakePosition: Any
    def __init__(self):
        ...
    @property
    def isStarted(self):
        ...
    @property
    def yearPosition(self):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def _setFakePosition(self, position):
        ...
    # decorador original: @adisp_process
    def __invoke(self):
        ...
    def __getInvokeDelay(self):
        ...
    def __hasServerFinalToken(self):
        ...
