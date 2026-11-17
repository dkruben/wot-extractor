# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/skeletons/helpers/platform.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from Event import Event as Event

class IPublishPlatform(object):
    onPayment = None
    onOverlay = None
    def init(self):
        ...
    def fini(self):
        ...
    def isInited(self):
        ...
    def isConnected(self):
        ...
