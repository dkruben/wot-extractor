# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/exchange/ConfirmExchangeDialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from adisp import adisp_process as adisp_process
from gui import SystemMessages as SystemMessages
from gui.Scaleform.daapi.view.meta.ConfirmExchangeDialogMeta import ConfirmExchangeDialogMeta as ConfirmExchangeDialogMeta
from gui.impl.lobby.exchange.exchange_rates_helper import handleUserValuesInput as handleUserValuesInput, showAllPersonalDiscountsWindow as showAllPersonalDiscountsWindow, handleAndRoundStepperInput as handleAndRoundStepperInput
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, g_eventBus as g_eventBus

class ConfirmExchangeDialog(ConfirmExchangeDialogMeta):
    handler: Any
    __selectedGold: Any
    __selectedResource: Any
    __exchangeMutex: Any
    meta: Any
    def __init__(self, meta, handler, **kwargs):
        ...
    def updateDialog(self, meta, handler):
        ...
    def onSelectedAmountChanged(self, goldValue, needItemsValue):
        ...
    def openDiscountInfoPage(self):
        ...
    def onWindowClose(self):
        ...
    # decorador original: @adisp_process
    def exchange(self, goldValue):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _callHandler(self, success, *kwargs):
        ...
    def __removeMeta(self):
        ...
    def __setMeta(self, meta):
        ...
    def __prepareAndSendData(self, *args):
        ...
