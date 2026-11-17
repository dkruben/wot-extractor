# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/customization/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import WindowLayer as WindowLayer
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework import GroupedViewSettings as GroupedViewSettings, ScopeTemplates as ScopeTemplates, ViewSettings as ViewSettings, ComponentSettings as ComponentSettings
from gui.Scaleform.framework.package_layout import PackageBusinessHandler as PackageBusinessHandler
from gui.Scaleform.genConsts.CONTEXT_MENU_HANDLER_TYPE import CONTEXT_MENU_HANDLER_TYPE as CONTEXT_MENU_HANDLER_TYPE
from gui.Scaleform.genConsts.CUSTOMIZATION_ALIASES import CUSTOMIZATION_ALIASES as CUSTOMIZATION_ALIASES
from gui.Scaleform.locale.VEHICLE_CUSTOMIZATION import VEHICLE_CUSTOMIZATION as VEHICLE_CUSTOMIZATION
from gui.app_loader import settings as app_settings
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import ShowDialogEvent as ShowDialogEvent
CAMOUFLAGES_KIND_TEXTS: list
CAMOUFLAGES_NATIONS_TEXTS: list

class CustomizationPackageBusinessHandler(PackageBusinessHandler):
    def __init__(self):
        ...

class CustomizationDialogPackageBusinessHandler(PackageBusinessHandler):
    def __init__(self):
        ...
    def __confirmCustomizationItemHandler(self, event):
        ...

def getContextMenuHandlers():
    ...
def getViewSettings():
    ...
def getStateMachineRegistrators():
    ...
def getBusinessHandlers():
    ...
