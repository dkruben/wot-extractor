# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/ui/battle_royale.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import QUEUE_TYPE as QUEUE_TYPE
from gui.prb_control.dispatcher import g_prbLoader as g_prbLoader
from gui.prb_control.entities.base.ctx import PrbAction as PrbAction
from gui.prb_control.settings import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from gui.shared.event_dispatcher import showHangar as showHangar
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController
from web.web_client_api import w2c as w2c, W2CSchema as W2CSchema

class OpenBattleRoyaleHangarMixin(object):
    battleRoyaleController: Any
    # decorador original: @w2c(...)
    def selectBRMode(self, _):
        ...
