# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/notification/BaseNotificationView.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from debug_utils import LOG_ERROR as LOG_ERROR
_NOT_ID_TUPLE_INDEX = 2

class BaseNotificationView(object):
    _model: Any
    __flashIDCounter: Any
    __flashIdToEntityIdMap: Any
    __entityIdToFlashIdMap: Any
    def __init__(self, model=None):
        ...
    def setModel(self, value):
        ...
    def cleanUp(self):
        ...
    def _getFlashID(self, notificationInfo):
        ...
    def _getNotificationID(self, flashId):
        ...
