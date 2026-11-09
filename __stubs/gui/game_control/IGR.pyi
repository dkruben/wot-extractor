# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/IGR.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import Event as Event
import constants as constants
from PlayerEvents import g_playerEvents as g_playerEvents
from skeletons.gui.game_control import IIGRController as IIGRController

class IGRController(IIGRController):
    __xpFactor: Any
    __roomType: Any
    onIgrTypeChanged: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def onLobbyStarted(self, ctx=None):
        ...
    def onDisconnected(self):
        ...
    def getXPFactor(self):
        ...
    def getRoomType(self):
        ...
    def __onIGRTypeChanged(self, roomType, xpFactor):
        ...
