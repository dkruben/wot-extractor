# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/gift_system/wrappers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from functools import wraps as wraps
OpenedGiftData: Any
GiftsHistoryData: Any
GiftsWebState: Any
IncomeSysMessage: Any
SendGiftResponse: Any

def ifMessagesEnabled(method):
    ...
def ifMessagesAllowed(msgType, useQueue=True):
    ...
def hasGiftEventHub(method):
    ...
def skipNoHubsAction(method):
    ...
def filterGiftHubsAction(eventID):
    ...
