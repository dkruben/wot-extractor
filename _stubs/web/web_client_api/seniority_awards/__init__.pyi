# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/seniority_awards/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from helpers import dependency as dependency
from skeletons.gui.game_control import ISeniorityAwardsController as ISeniorityAwardsController
from gui.shared.event_dispatcher import showSeniorityRewardVehiclesWindow as showSeniorityRewardVehiclesWindow
from web.web_client_api import w2capi as w2capi, w2c as w2c, W2CSchema as W2CSchema

# decorador original: @w2capi(...)
class SeniorityAwardsWebApi(object):
    __seniorityAwardsCtrl: Any
    # decorador original: @w2c(...)
    def isVehicleSelectionAvailable(self, _):
        ...

class OpenSeniorityAwardsWebApi(object):
    # decorador original: @w2c(...)
    def showSeniorityVehicleSelectionWindow(self, _):
        ...
