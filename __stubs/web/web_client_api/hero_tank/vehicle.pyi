# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/hero_tank/vehicle.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.shared import event_dispatcher as event_dispatcher
from helpers import dependency as dependency
from skeletons.gui.game_control import IHeroTankController as IHeroTankController
from web.web_client_api import w2c as w2c, W2CSchema as W2CSchema

class HeroTankWebApiMixin(object):
    __heroControl: Any
    # decorador original: @w2c(...)
    def getName(self, _):
        ...
    # decorador original: @w2c(...)
    def showPreview(self, _):
        ...
