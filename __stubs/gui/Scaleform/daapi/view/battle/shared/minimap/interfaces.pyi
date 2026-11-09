# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/minimap/interfaces.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from abc import abstractmethod as abstractmethod
from account_helpers.settings_core.settings_constants import GAME as GAME
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME

class IMinimapPlugin(typing.Protocol):
    @abstractmethod
    def applyNewSize(self, sizeIndex):
        ...
    @abstractmethod
    def updateControlMode(self, mode, vehicleID):
        ...
    @abstractmethod
    def initControlMode(self, mode, available):
        ...
    @abstractmethod
    def updateSettings(self, diff):
        ...
    @abstractmethod
    def setSettings(self):
        ...
