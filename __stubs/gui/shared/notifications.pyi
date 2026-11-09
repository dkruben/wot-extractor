# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/notifications.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from constants import IS_DEVELOPMENT as IS_DEVELOPMENT, NC_MESSAGE_PRIORITY as NC_MESSAGE_PRIORITY
_logger: Any

class NotificationPriorityLevel(object):
    HIGH = 'high'
    MEDIUM = 'medium'
    LOW = 'low'
    RANGE: tuple
    NC_MAPPING: dict
    @classmethod
    def convertFromNC(cls, priority):
        ...

class NotificationGroup(object):
    INFO = 'info'
    INVITE = 'invite'
    OFFER = 'offer'
    ALL: tuple

class NotificationGuiSettings(object):
    __slots__: tuple
    isNotify: Any
    priorityLevel: Any
    isAlert: Any
    auxData: Any
    showAt: Any
    groupID: Any
    messageType: Any
    messageSubtype: Any
    decorator: Any
    lifeTime: Any
    __customEvent: Any
    def __init__(self, isNotify=False, priorityLevel=..., isAlert=False, auxData=None, showAt=0, groupID=..., messageType=None, messageSubtype=None, decorator=None, lifeTime=0):
        ...
    def setCustomEvent(self, eType, ctx=None):
        ...
    def getCustomEvent(self):
        ...
    def __validate(self):
        ...
