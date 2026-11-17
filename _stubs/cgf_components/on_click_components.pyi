# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/on_click_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import CGF as CGF
from GenericComponents import VSEComponent as VSEComponent
from adisp import adisp_process as adisp_process
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
from constants import MarathonConfig as MarathonConfig, IS_CLIENT as IS_CLIENT
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from cgf_components.hover_component import IsHoveredComponent as IsHoveredComponent, SelectionComponent as SelectionComponent
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.game_control.links import URLMacros as URLMacros
from gui.shared.event_dispatcher import showBrowserOverlayView as showBrowserOverlayView
_logger: Any
URL_PROVIDERS: dict

# decorador original: @registerComponent
class OpenBrowserOnClickComponent(object):
    domain = CGF.Domain.Client
    editorTitle = 'Open Browser On Click'
    urlProvider: Any
    __urlParser: Any
    def __init__(self):
        ...
    def doAction(self):
        ...
    # decorador original: @adisp_process
    def __openBrowser(self):
        ...

class ClientSelectableComponentsSystem(CGF.System):
    BrowserActivated: Any
    BrowserDeactivated: Any
    Reactions: Any
    def update(self):
        ...
    def handleOpenBrowserOnClickAdded(self, openBrowserOnClickComponent, selectionComponent):
        ...
    def handleOpenBrowserOnClickRemoved(self, openBrowserOnClickComponent, selectionComponent):
        ...

class ClickVSEComponentsSystem(CGF.System):
    ComponentActivated: Any
    ComponentDeactivated: Any
    Reactions: Any
    def update(self):
        ...
    def handleComponentAdded(self, selectionComponent, vseComponent):
        ...
    def handleComponentRemoved(self, selectionComponent, vseComponent):
        ...

class ClickSystem(CGF.System):
    _hangarSpace: Any
    ClickIterate: Any
    Reactions: Any
    _selectedGO: Any
    def __init__(self, *args):
        ...
    def onMappingLoaded(self):
        ...
    def onMappingUnloaded(self):
        ...
    def _onMouseDown(self):
        ...
    def _onMouseUp(self):
        ...

def getMarathonVideoUrl():
    ...
