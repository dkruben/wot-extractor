# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/MinimapGrid.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
from gui.Scaleform.daapi.view.meta.MinimapGridMeta import MinimapGridMeta as MinimapGridMeta
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore

class MinimapGrid(MinimapGridMeta):
    settingsCore: Any
    _channel: Any
    _controller: Any
    __mapId: Any
    def __init__(self):
        ...
    def setController(self, controller):
        ...
    def removeController(self):
        ...
    def setActive(self, isActive):
        ...
    def setClick(self, x, y):
        ...
    def setMapId(self, mapId):
        ...
    def addCommand(self, cmd):
        ...
    def as_addMessageS(self, message):
        ...
    def as_setJoinedS(self, flag):
        ...
