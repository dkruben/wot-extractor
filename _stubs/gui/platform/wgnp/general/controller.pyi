# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/platform/wgnp/general/controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from BWUtil import AsyncReturn as AsyncReturn
import wg_async as wg_async
from gui.platform.base.statuses.controller_mixin import StatusesMixin as StatusesMixin
from gui.platform.wgnp.base.controller import WGNPRequestController as WGNPRequestController
from gui.platform.wgnp.general.request import AccountCountryParams as AccountCountryParams
from gui.platform.wgnp.general.statuses import GeneralAccountCountryStatus as GeneralAccountCountryStatus, createAccountCountryStatusFromResponse as createAccountCountryStatusFromResponse
from skeletons.gui.platform.wgnp_controllers import IWGNPGeneralRequestController as IWGNPGeneralRequestController
ACCOUNT_COUNTRY_CONTEXT = '<country>'

class WGNPGeneralRequestController(StatusesMixin, WGNPRequestController, IWGNPGeneralRequestController):
    # decorador original: @wg_async.wg_async
    def getAccountCountry(self, waitingID=None):
        ...
