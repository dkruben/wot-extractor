# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/exchange/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import WindowLayer as WindowLayer
from gui.Scaleform.framework.package_layout import PackageBusinessHandler as PackageBusinessHandler
from gui.app_loader import settings as app_settings
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import ShowDialogEvent as ShowDialogEvent
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework import GroupedViewSettings as GroupedViewSettings, ScopeTemplates as ScopeTemplates

class ExchangeDialogBusinessHandler(PackageBusinessHandler):
    _ALIAS = VIEW_ALIAS.CONFIRM_EXCHANGE_DIALOG
    _EVENT = ShowDialogEvent.SHOW_EXCHANGE_DIALOG
    _LAYER = WindowLayer.WINDOW
    def __init__(self):
        ...
    def _exchangeDialogHandler(self, event):
        ...
    def __loadOrUpdateDialog(self, name, alias, meta, handler):
        ...

class _ExchangeDialogModalBusinessHandler(ExchangeDialogBusinessHandler):
    _ALIAS = VIEW_ALIAS.CONFIRM_EXCHANGE_DIALOG_MODAL
    _EVENT = ShowDialogEvent.SHOW_EXCHANGE_DIALOG_MODAL
    _LAYER = WindowLayer.TOP_WINDOW

def getContextMenuHandlers():
    ...
def getViewSettings():
    ...
def getBusinessHandlers():
    ...
