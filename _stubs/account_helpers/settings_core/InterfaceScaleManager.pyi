# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/account_helpers/settings_core/InterfaceScaleManager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
import BigWorld as BigWorld
import Event as Event
from gui.shared.utils import graphics as graphics
from gui import g_guiResetters as g_guiResetters
from account_helpers.settings_core import settings_constants as settings_constants
from helpers import dependency as dependency
from skeletons.connection_mgr import IConnectionManager as IConnectionManager

class InterfaceScaleManager(object):
    connectionMgr: Any
    onScaleChanged: Any
    onScaleExactlyChanged: Any
    proxy: Any
    __index: Any
    __scaleValue: Any
    def __init__(self, settingsCore):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def get(self):
        ...
    def getIndex(self):
        ...
    def onSettingsChanged(self, diff):
        ...
    def scaleChanged(self):
        ...
    def changeScale(self, index):
        ...
    @staticmethod
    def getScaleOptions():
        ...
    def getScaleByIndex(self, ind, powerOfTwo=True):
        ...
