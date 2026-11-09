# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/wotlda/response.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from http import client as httplib
from typing import Dict as Dict, Optional as Optional, TYPE_CHECKING as TYPE_CHECKING
from gui.game_control.wotlda.constants import LAST_UPDATE_TIMESTAMP as LAST_UPDATE_TIMESTAMP, SupportedWotldaLoadoutType as SupportedWotldaLoadoutType
from gui.shared.utils.requesters.abstract import Response as Response

class WotldaResponse(object):
    _response: Any
    _exception: Any
    def __init__(self, response):
        ...
    def getData(self):
        ...
    def setException(self, exception):
        ...
    def isSuccess(self):
        ...
    def isNotModified(self):
        ...
    def isServiceUnavailable(self):
        ...
    def hasRequestFailed(self):
        ...
    def getLoadoutsByType(self, loadoutType):
        ...
    def getTimestamp(self):
        ...
