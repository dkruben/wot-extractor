# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/login/LoginQueue.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.meta.LoginQueueWindowMeta import LoginQueueWindowMeta as LoginQueueWindowMeta
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import LoginEvent as LoginEvent, LoginEventEx as LoginEventEx, ArgsEvent as ArgsEvent
from helpers import dependency as dependency
from skeletons.connection_mgr import IConnectionManager as IConnectionManager

class LoginQueue(LoginQueueWindowMeta):
    connectionMgr: Any
    __title: Any
    __message: Any
    __cancelLabel: Any
    __showAutoLoginBtn: Any
    def __init__(self, title, message, cancelLabel, showAutoLoginBtn, **kwargs):
        ...
    def __updateData(self, title, message, cancelLabel, showAutoLoginBtn):
        ...
    def __updateTexts(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def onWindowClose(self):
        ...
    def onCancelClick(self):
        ...
    def onAutoLoginClick(self):
        ...
    def __windowClosing(self):
        ...
    def __onCancelLoginQueue(self, event):
        ...
    def __onUpdateArgs(self, event):
        ...
