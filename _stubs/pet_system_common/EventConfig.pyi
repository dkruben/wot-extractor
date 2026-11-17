# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/pet_system_common/EventConfig.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from pet_system_common.pet_constants import PetEventsConsts as pc, PetEventTypeConsts as eventTypes
from typing import Dict as Dict

class EventConfig(object):
    _config: Any
    def __init__(self, config):
        ...
    def getEvents(self):
        ...
    def getEventById(self, eventID):
        ...
    def getEventType(self, eventID):
        ...
    def getEventRewardID(self, eventID):
        ...
