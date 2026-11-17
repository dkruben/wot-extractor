# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/gifts/gifts_common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import IS_DEVELOPMENT as IS_DEVELOPMENT
from soft_exception import SoftException as SoftException
UNKNOWN_SENDER_ID = 0
UNPROCESSED_GIFT_DB_ID = -1

class ClientReqStrategy(object):
    AUTO = 'auto'
    DEMAND = 'demand'
    ALL: tuple

class GiftEventID(object):
    UNKNOWN = 0
    DEV_TEST = 1
    ALL: Any

class GiftEventState(object):
    ENABLED = 'enabled'
    SUSPENDED = 'suspended'
    DISABLED = 'disabled'
    ALL: tuple

class GiftStatus(object):
    TYPE: Any
    NEW = 1
    AVAILABLE = 2
    OPENED = 3
    ACTIVE: tuple
    ALL: tuple

class Gift(object):
    __slots__: tuple
    _giftID: Any
    _senderID: Any
    _giftItemID: Any
    _status: Any
    _meta: Any
    def __init__(self, giftID, senderID, giftItemID, status, meta):
        ...
    @property
    def giftID(self):
        ...
    @property
    def giftItemID(self):
        ...
    @property
    def status(self):
        ...
    @status.setter
    def status(self, value):
        ...
    def toOpenExtra(self):
        ...
    def __str__(self):
        ...
