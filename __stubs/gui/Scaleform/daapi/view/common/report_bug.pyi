# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/common/report_bug.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from adisp import adisp_process as adisp_process
from gui import GUI_SETTINGS as GUI_SETTINGS, DialogsInterface as DialogsInterface, makeHtmlString as makeHtmlString
from gui.Scaleform.daapi.view.dialogs import DIALOG_BUTTON_ID as DIALOG_BUTTON_ID
from gui.Scaleform.daapi.view.meta.ReportBugPanelMeta import ReportBugPanelMeta as ReportBugPanelMeta
from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers import dependency as dependency
from skeletons.gui.game_control import IExternalLinksController as IExternalLinksController

class ReportBugPanel(ReportBugPanelMeta):
    def reportBug(self):
        ...
    def _populate(self):
        ...
    @staticmethod
    def makeHyperLink(linkType, text):
        ...
    @staticmethod
    # decorador original: @adisp_process
    def reportBugOpenConfirm():
        ...
