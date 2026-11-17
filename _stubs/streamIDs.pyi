# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/streamIDs.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from past.builtins import xrange as xrange
STREAM_ID_CHAT_MIN = 1
STREAM_ID_CHAT_MAX = 99
CHAT_INITIALIZATION_ID = 50
STREAM_ID_AVATAR_BATTLE_RESULTS = 100
STREAM_ID_AVATAR_EMPTY_BATTLE_RESULTS = 101
STREAM_ID_ACCOUNT_CMDS_MIN = 200
STREAM_ID_ACCOUNT_CMDS_MAX = 30000
rangeCBs: Any

class RangeStreamIDCallbacks(object):
    __callbacks: Any
    __rangeFactor: Any
    def __init__(self, rangeFactor=100):
        ...
    def addRangeCallback(self, range, callback):
        ...
    def delRangeCallback(self, range):
        ...
    def clear(self):
        ...
    def getCallbackForStreamID(self, streamID):
        ...
    def __getKeySequence(self, range):
        ...

def outStreamIdCB(streamID):
    ...
