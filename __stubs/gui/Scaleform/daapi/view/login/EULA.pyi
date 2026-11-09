# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/login/EULA.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.meta.EULAMeta import EULAMeta as EULAMeta
from gui.shared.events import CloseWindowEvent as CloseWindowEvent, OpenLinkEvent as OpenLinkEvent
from helpers import dependency as dependency
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gameplay import IGameplayLogic as IGameplayLogic

class EULADlg(EULAMeta):
    connectionMgr: Any
    gameplay: Any
    __applied: Any
    __eulaString: Any
    def __init__(self, ctx=None):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def onWindowClose(self):
        ...
    def requestEULAText(self):
        ...
    def onApply(self):
        ...
    def onLinkClick(self, url):
        ...
    def __fireEulaClose(self):
        ...
    def __onDisconnected(self):
        ...
