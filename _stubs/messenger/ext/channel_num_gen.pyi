# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/ext/channel_num_gen.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from constants import PREBATTLE_TYPE as PREBATTLE_TYPE, QUEUE_TYPE as QUEUE_TYPE
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from messenger.m_constants import LAZY_CHANNEL as LAZY_CHANNEL, BATTLE_CHANNEL as BATTLE_CHANNEL, PRIMARY_CHANNEL_ORDER as PRIMARY_CHANNEL_ORDER
_CHANNEL_LAZY_ORDER: dict
_idGen: Any
_PRB_CLIENT_IDS: dict
PRB_CLIENT_COMBINED_IDS: dict
_LAZY_CLIENT_IDS: Any
_QUEUE_CLIENT_IDS: Any
_BATTLE_CLIENT_IDS: Any
_SPECIAL_CLIENT_IDS: Any

class SPECIAL_CLIENT_WINDOWS(CONST_CONTAINER):
    TRAINING_LIST = 1
    TRAINING_ROOM = 2
    EPIC_TRAINING_LIST = 5
    EPIC_TRAINING_ROOM = 6

def initPrbTypeToClientID():
    ...
def genOrder4Channel(channel):
    ...
def getOrder4Prebattle():
    ...
def getOrder4LazyChannel(name):
    ...
def genClientID4Channel(channel):
    ...
def getClientID4Prebattle(prbType):
    ...
def getClientID4PreQueue(queueType):
    ...
def getClientID4LazyChannel(name):
    ...
def getClientID4SpecialWindow(name):
    ...
def getClientID4BattleChannel(name):
    ...
def isClientIDValid(clientID):
    ...
