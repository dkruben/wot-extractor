# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/platform/products_fetcher/product_descriptor.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from helpers.events_handler import EventsHandler as EventsHandler
from typing import TYPE_CHECKING as TYPE_CHECKING
from typing import Dict as Dict

class ProductDescriptor(EventsHandler):
    STOREFRONT_NAMESPACE = 'wot_subscriptions'
    _params: Any
    _isFull: Any
    def __init__(self, params):
        ...
    @property
    def productCode(self):
        ...
    @property
    def productID(self):
        ...
    @property
    def productUrl(self):
        ...
    @property
    def metadata(self):
        ...
    @property
    def description(self):
        ...
    @property
    def largeImageURL(self):
        ...
    @property
    def smallImageURL(self):
        ...
    @property
    def mediumImageURL(self):
        ...
    @property
    def shortDescription(self):
        ...
    @property
    def name(self):
        ...
    @property
    def claimURL(self):
        ...
    @property
    def isDescriptorFull(self):
        ...
    def destroy(self):
        ...
    def extendData(self, data):
        ...
    def _getImageURL(self, size):
        ...
    def _getFromParams(self, name, default=None):
        ...
    def _getFromMetadata(self, valueName):
        ...
