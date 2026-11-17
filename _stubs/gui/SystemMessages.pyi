# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/SystemMessages.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from enumerations import Enumeration as Enumeration
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency
from skeletons.gui.system_messages import ISystemMessages as ISystemMessages
ResultMsg: Any
SM_TYPE: Any
CURRENCY_TO_SM_TYPE: dict
CURRENCY_TO_SM_TYPE_DISMANTLING: dict

def _getSystemMessages():
    ...
def pushMessage(text, type=..., priority=None, messageData=None, savedData=None):
    ...
def pushMessagesFromResult(resultMsg):
    ...
def pushI18nMessage(key, *args, **kwargs):
    ...
