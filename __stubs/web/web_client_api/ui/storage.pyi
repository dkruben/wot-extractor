# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/ui/storage.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from past.builtins import basestring as basestring
from gui.Scaleform.daapi.view.lobby.storage import getSectionsList as getSectionsList, STORAGE_CONSTANTS as STORAGE_CONSTANTS
from gui.shared import event_dispatcher as shared_events
from helpers import dependency as dependency
from skeletons.gui.offers import IOffersDataProvider as IOffersDataProvider
from web.web_client_api import w2c as w2c, W2CSchema as W2CSchema, Field as Field, WebCommandException as WebCommandException

class _OpenStorageSchema(W2CSchema):
    section_id: Any

class _OpenOfferSchema(W2CSchema):
    offer_id: Any

class StorageWebApiMixin(object):
    _offersProvider: Any
    # decorador original: @w2c(...)
    def openStorage(self, cmd):
        ...
    # decorador original: @w2c(...)
    def openOffer(self, cmd):
        ...

def _validateSection(value, _):
    ...
