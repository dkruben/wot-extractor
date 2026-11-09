# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/framework/managers/event_logging.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import time as time
import itertools as itertools
from constants import REQUEST_COOLDOWN as REQUEST_COOLDOWN
from debug_utils import LOG_DEBUG as LOG_DEBUG, LOG_WARNING as LOG_WARNING
from gui.Scaleform.framework.entities.abstract.EventLogManagerMeta import EventLogManagerMeta as EventLogManagerMeta
from gui.Scaleform.genConsts.EVENT_LOG_CONSTANTS import EVENT_LOG_CONSTANTS as EVENT_LOG_CONSTANTS
import BigWorld as BigWorld
LOG_LIMIT = 70
PACKAGE_LIMIT = 70

class EventLogManager(EventLogManagerMeta):
    __currentPackage: Any
    __sendList: Any
    __lastSentTime: Any
    __onAutoSending: Any
    __cbckIdx: Any
    __packageIdx: Any
    _isEnabled: Any
    def __init__(self, isEnabled=False):
        ...
    def _populate(self):
        ...
    def __sendPackageToServer(self, package):
        ...
    def __sendSavedPackageToServer(self):
        ...
    def __addPackageToSendList(self, package):
        ...
    def __encodeEvent(self, subSystemType, eventType, uiid, arg):
        ...
    def logEvent(self, subSystemType, eventType, uiid, arg):
        ...
    def destroy(self):
        ...
