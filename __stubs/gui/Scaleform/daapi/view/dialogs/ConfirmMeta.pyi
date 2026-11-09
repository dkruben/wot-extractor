# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/dialogs/ConfirmMeta.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.dialogs import IDialogMeta as IDialogMeta
from gui.Scaleform.framework import ScopeTemplates as ScopeTemplates
from gui.shared import events as events
from helpers import i18n as i18n

class ConfirmMeta(IDialogMeta):
    __title: Any
    __description: Any
    __submitLabel: Any
    __cancelLabel: Any
    __checkBoxLabel: Any
    __checkBoxSelected: Any
    def __init__(self, title, description, submitBtn, cancelBtn, checkBox, selected=False):
        ...
    def destroy(self):
        ...
    def getEventType(self):
        ...
    def getTitle(self):
        ...
    def getDescription(self):
        ...
    def getSubmitButtonLabel(self):
        ...
    def getCancelButtonLabel(self):
        ...
    def getCheckBoxButtonLabel(self):
        ...
    def getCheckBoxSelected(self):
        ...
    def getViewScopeType(self):
        ...
