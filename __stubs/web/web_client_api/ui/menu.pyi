# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/ui/menu.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from past.builtins import long as long, basestring as basestring
from gui.Scaleform.daapi.view.lobby.user_cm_handlers import CustomUserCMHandler as CustomUserCMHandler
from gui.Scaleform.genConsts.CONTEXT_MENU_HANDLER_TYPE import CONTEXT_MENU_HANDLER_TYPE as CONTEXT_MENU_HANDLER_TYPE
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.game_control import IBrowserController as IBrowserController
from web.web_client_api import WebCommandException as WebCommandException, w2c as w2c, W2CSchema as W2CSchema, Field as Field

class _UserMenuSchema(W2CSchema):
    spa_id: Any
    user_name: Any
    clan_abbrev: Any
    custom_items: Any
    excluded_items: Any
    custom_items_after_end: Any

class UserMenuWebApiMixin(object):
    browserController: Any
    # decorador original: @w2c(...)
    def userMenu(self, cmd, ctx):
        ...
