# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/page/footer/server_info_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum, IntEnum as IntEnum
from frameworks.wulf import ViewModel as ViewModel

class PingStatus(IntEnum):
    REQUESTED = 0
    HIGH = 1
    NORM = 2
    LOW = 3

class ColorBlindMode(Enum):
    DISABLED = 'disabled'
    PROTANOPIA = 'protanopia'

class ServerInfoModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=3, commands=0):
        ...
    def getServerName(self):
        ...
    def setServerName(self, value):
        ...
    def getStatus(self):
        ...
    def setStatus(self, value):
        ...
    def getColorBlind(self):
        ...
    def setColorBlind(self, value):
        ...
    def _initialize(self):
        ...
