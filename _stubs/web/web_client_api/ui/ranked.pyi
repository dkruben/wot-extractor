# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/ui/ranked.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from past.builtins import basestring as basestring
from gui.Scaleform.genConsts.RANKEDBATTLES_CONSTS import RANKEDBATTLES_CONSTS as RANKEDBATTLES_CONSTS
from gui.Scaleform.genConsts.RANKEDBATTLES_ALIASES import RANKEDBATTLES_ALIASES as RANKEDBATTLES_ALIASES
from gui.shared.event_dispatcher import showBrowserOverlayView as showBrowserOverlayView
from helpers import dependency as dependency
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController
from web.web_client_api import w2c as w2c, W2CSchema as W2CSchema, Field as Field
VALID_RANKED_PAGES: tuple

class _OpenRankedBattlesScheme(W2CSchema):
    pageId: Any
    pageParams: Any

class _OpenBrowserOverlaySchema(W2CSchema):
    url: Any

class OpenRankedPagesMixin(object):
    __rankedController: Any
    # decorador original: @w2c(...)
    def openRankedPage(self, cmd):
        ...
    # decorador original: @w2c(...)
    def openRankedOverlay(self, cmd):
        ...
