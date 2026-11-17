# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/fortifications/ConfirmOrderDialogMeta.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui import makeHtmlString as makeHtmlString
from gui.Scaleform.daapi.view.dialogs import IDialogMeta as IDialogMeta, I18nConfirmDialogMeta as I18nConfirmDialogMeta, DIALOG_BUTTON_ID as DIALOG_BUTTON_ID
from gui.Scaleform.framework import ScopeTemplates as ScopeTemplates
from gui.Scaleform.locale.DIALOGS import DIALOGS as DIALOGS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared import events as events
from gui.shared.formatters import text_styles as text_styles, icons as icons
from web_stubs import i18n as i18n

class ConfirmOrderDialogMeta(IDialogMeta):
    __orderID: Any
    __title: Any
    __submitLabel: Any
    __cancelLabel: Any
    def __init__(self, orderID, title, submitBtn, cancelBtn):
        ...
    def submit(self, count):
        ...
    def getEventType(self):
        ...
    def getTitle(self):
        ...
    def getSubmitButtonLabel(self):
        ...
    def getCancelButtonLabel(self):
        ...
    def getOrderID(self):
        ...
    def getViewScopeType(self):
        ...
    def destroy(self):
        ...

class BuyOrderDialogMeta(ConfirmOrderDialogMeta):
    def __init__(self, orderID):
        ...

class UnfreezeVehicleDialogMeta(I18nConfirmDialogMeta):
    __playerName: Any
    __vehicleName: Any
    __price: Any
    __balance: Any
    def __init__(self, playerName, vehicleName, price, balance):
        ...
    def getMessage(self):
        ...
