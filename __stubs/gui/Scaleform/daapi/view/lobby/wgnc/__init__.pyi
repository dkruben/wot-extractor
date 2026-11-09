# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/wgnc/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from debug_utils import LOG_WARNING as LOG_WARNING
from frameworks.wulf import WindowLayer as WindowLayer
from gui.Scaleform.framework import ScopeTemplates as ScopeTemplates, ViewSettings as ViewSettings, GroupedViewSettings as GroupedViewSettings
from gui.Scaleform.framework.package_layout import PackageBusinessHandler as PackageBusinessHandler
from gui.app_loader import settings as app_settings
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events
from gui.wgnc import g_wgncProvider as g_wgncProvider

class WGNC_ALIASES(object):
    MODAL_BASIC_WINDOW = 'wgnc/modalBasicWindow'
    NOT_MODAL_BASIC_WINDOW = 'wgnc/notModalBasicWindow'
    POLL_WINDOW = 'wgnc/pollWindow'
    SWF_DIALOG = 'WGNCDialog.swf'
    SWF_POLL_WINDOW = 'WGNCPollWindow.swf'
    UI_DIALOG = 'WGNCDialog'
    UI_POLL_WINDOW = 'WGNCPollWindowUI'

class _WGNCPackageBusinessHandler(PackageBusinessHandler):
    def __init__(self):
        ...
    def __showBasicWindow(self, event):
        ...
    def __showPollWindow(self, event):
        ...

def getContextMenuHandlers():
    ...
def getViewSettings():
    ...
def getBusinessHandlers():
    ...
