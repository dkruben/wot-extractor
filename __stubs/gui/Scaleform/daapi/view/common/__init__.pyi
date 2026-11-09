# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/common/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import WindowLayer as WindowLayer
from gui.Scaleform.daapi.view.dialogs.button_dialog import ButtonDialog as ButtonDialog
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework import ViewSettings as ViewSettings, GroupedViewSettings as GroupedViewSettings, ScopeTemplates as ScopeTemplates, ComponentSettings as ComponentSettings
from gui.Scaleform.framework.package_layout import PackageBusinessHandler as PackageBusinessHandler
from gui.shared.events import ShowDialogEvent as ShowDialogEvent

class CommonPackageBusinessHandler(PackageBusinessHandler):
    __slots__: tuple
    def __init__(self):
        ...

class CommonDialogsHandler(PackageBusinessHandler):
    __slots__: tuple
    def __init__(self):
        ...
    def __loadSimpleDialogView(self, alias, meta, handler):
        ...
    def __loadSimpleDialog(self, event):
        ...
    def __loadButtonDialog(self, event):
        ...

def getContextMenuHandlers():
    ...
def getViewSettings():
    ...
def getBusinessHandlers():
    ...
