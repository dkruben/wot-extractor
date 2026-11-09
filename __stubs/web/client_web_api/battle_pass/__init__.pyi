# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/client_web_api/battle_pass/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from helpers import dependency as dependency
from helpers.events_handler import EventsHandler as EventsHandler
from skeletons.gui.game_control import IBattlePassController as IBattlePassController
from web.client_web_api.api import C2WHandler as C2WHandler, c2w as c2w
from web.common import formatBattlePassInfo as formatBattlePassInfo

class BattlePassEventHandler(C2WHandler, EventsHandler):
    __battlePass: Any
    def init(self):
        ...
    def fini(self):
        ...
    def _getEvents(self):
        ...
    # decorador original: @c2w(...)
    def __sendInfo(self, *args, **kwargs):
        ...
