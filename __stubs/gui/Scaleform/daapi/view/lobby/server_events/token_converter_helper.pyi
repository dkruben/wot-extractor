# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/server_events/token_converter_helper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from copy import deepcopy as deepcopy
from future.utils import viewkeys as viewkeys, viewvalues as viewvalues
from typing import TYPE_CHECKING as TYPE_CHECKING, NamedTuple as NamedTuple
from optional_bonuses import TrackVisitor as TrackVisitor
from math_common import round_py2_style_int as round_py2_style_int
from typing import Dict as Dict
from gui.server_events.event_items import Quest as Quest

# base nao representavel no stub: NamedTuple(...)
class TokenConvertionData:
    def __new__(cls, **kwargs):
        ...

def convertTokens(token, bonusTokens, convertionData):
    ...
def convertTokensInBonusData(event, bonusData, questTokensConvertion, questTokensCount):
    ...
def getBonusDataFromOneOfBonuses(event, pCur=None):
    ...
