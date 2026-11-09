# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/platform/wgnp/general/statuses.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.platform.base.response import Codes as Codes
from gui.platform.base.statuses.constants import StatusTypes as StatusTypes
from gui.platform.base.statuses.status import Status as Status
from gui.platform.wgnp.general.request import AccountCountryParams as AccountCountryParams

class GeneralAccountCountryStatus(Status):
    __slots__: tuple
    @property
    def country(self):
        ...

def createAccountCountryStatusFromResponse(response):
    ...
