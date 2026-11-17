# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/dialogs/SimpleDialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from gui.Scaleform.daapi.view.dialogs import DIALOG_BUTTON_ID as DIALOG_BUTTON_ID
from gui.Scaleform.daapi.view.meta.SimpleDialogMeta import SimpleDialogMeta as SimpleDialogMeta
from gui.Scaleform.framework import ScopeTemplates as ScopeTemplates

class SimpleDialog(SimpleDialogMeta):
    __message: Any
    __title: Any
    __buttons: Any
    __timer: Any
    __timerCallbackID: Any
    _handler: Any
    __dialogScope: Any
    _isProcessed: Any
    def __init__(self, message, title, buttons, handler, dialogScope=..., timer=0, **kwargs):
        ...
    def _callHandler(self, buttonID):
        ...
    def getCurrentScope(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def onButtonClick(self, buttonId):
        ...
    def onWindowClose(self):
        ...
    def __setMessage(self):
        ...
    def _timerCallback(self):
        ...
