# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/request/settings.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import helpers as helpers
from gui.limited_ui.lui_rules_storage import LUI_RULES as LUI_RULES
from helpers import dependency as dependency
from skeletons.gui.game_control import ILimitedUIController as ILimitedUIController
from web.web_client_api import W2CSchema as W2CSchema, w2c as w2c

class SettingsWebApiMixin(object):
    __limitedUIController: Any
    _MODE_HIDE_COUNTERS = 'hide_counters'
    # decorador original: @w2c(...)
    def getSettings(self, _):
        ...
