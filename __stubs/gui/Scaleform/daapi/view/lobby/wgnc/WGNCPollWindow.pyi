# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/wgnc/WGNCPollWindow.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from adisp import adisp_process as adisp_process
from gui import DialogsInterface as DialogsInterface
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.wgnc import g_wgncProvider as g_wgncProvider
from gui.Scaleform.daapi.view.dialogs import DIALOG_BUTTON_ID as DIALOG_BUTTON_ID
from gui.Scaleform.daapi.view.meta.WGNCPollWindowMeta import WGNCPollWindowMeta as WGNCPollWindowMeta

class WGNCPollWindow(WGNCPollWindowMeta):
    __notID: Any
    __target: Any
    def __init__(self, ctx=None):
        ...
    # decorador original: @adisp_process
    def onWindowClose(self):
        ...
    def onBtnClick(self):
        ...
    def onLinkClick(self, actions):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __populateData(self):
        ...
    def __handlePollWindowClose(self, event):
        ...
