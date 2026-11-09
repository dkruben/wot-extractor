# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/helpers/platform/base.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from Event import EventManager as EventManager, Event as Event
from skeletons.helpers.platform import IPublishPlatform as IPublishPlatform

class BasePublishPlatform(IPublishPlatform):
    __slots__: tuple
    __eventMgr: Any
    onPayment: Any
    onOverlay: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def isInited(self):
        ...
    def isConnected(self):
        ...
