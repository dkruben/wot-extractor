# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import WindowLayer as WindowLayer
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.dialogs.missions_dialogs import UseAwardSheetWindow as UseAwardSheetWindow
from gui.Scaleform.daapi.view.lobby.BoosterInfoWindow import BoosterInfoWindow as BoosterInfoWindow
from gui.Scaleform.daapi.view.lobby.goodie_info_window import GoodieInfoWindow as GoodieInfoWindow
from gui.Scaleform.daapi.view.lobby.hangar.BrowserView import BrowserView as BrowserView
from gui.Scaleform.daapi.view.lobby.image_view.image_view import ImageView as ImageView
from gui.Scaleform.daapi.view.lobby.wot_plus.wot_plus_browser_pages import WotPlusInfoView as WotPlusInfoView
from gui.Scaleform.daapi.view.login.LegalInfoWindow import LegalInfoWindow as LegalInfoWindow
from gui.Scaleform.framework import ComponentSettings as ComponentSettings, ContainerSettings as ContainerSettings, GroupedViewSettings as GroupedViewSettings, ScopeTemplates as ScopeTemplates, ViewSettings as ViewSettings
from gui.Scaleform.framework.managers import containers as containers
from gui.Scaleform.framework.package_layout import PackageBusinessHandler as PackageBusinessHandler
from gui.Scaleform.genConsts.CONTEXT_MENU_HANDLER_TYPE import CONTEXT_MENU_HANDLER_TYPE as CONTEXT_MENU_HANDLER_TYPE
from gui.app_loader import settings as app_settings
from gui.impl.lobby.clan_supply.info_view import InfoView as ClanSupplyInfoView
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import ShowDialogEvent as ShowDialogEvent

class LobbyPackageBusinessHandler(PackageBusinessHandler):
    def __init__(self):
        ...
    def __moduleWindowHandler(self, event):
        ...

class LobbyDialogsHandler(PackageBusinessHandler):
    def __init__(self):
        ...
    def __checkBoxDialogHandler(self, event):
        ...
    def __confirmModuleHandler(self, event):
        ...
    def __pmConfirmationDialogHandler(self, event):
        ...
    def __iconDialogHandler(self, event):
        ...
    def __iconPriceDialogHandler(self, event):
        ...
    def __useAwardSheetDialogHandler(self, event):
        ...
    def __showFreeXPInfoWindow(self, event):
        ...
    def __systemMsgDialogHandler(self, event):
        ...

def getContextMenuHandlers():
    ...
def getViewSettings():
    ...
def getBusinessHandlers():
    ...
