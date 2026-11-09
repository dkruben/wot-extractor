# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/framework/package_layout.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import importlib as importlib
import logging as logging
from future.utils import viewvalues as viewvalues
from frameworks.wulf import WindowLayer as WindowLayer
from gui.Scaleform.framework import GroupedViewSettings as GroupedViewSettings
from gui.Scaleform.framework.managers import context_menu as context_menu
from gui.Scaleform.framework.managers.containers import POP_UP_CRITERIA as POP_UP_CRITERIA
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.override_scaleform_views_manager import g_overrideScaleFormViewsConfig as g_overrideScaleFormViewsConfig
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import ViewEventType as ViewEventType
from helpers import dependency as dependency
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from soft_exception import SoftException as SoftException
_logger: Any
_addListener = g_eventBus.addListener
_removeListener = g_eventBus.removeListener

class PackageBusinessHandler(object):
    __counter: Any
    __slots__: tuple
    _listeners: Any
    _scope: Any
    _app: Any
    _appNS: Any
    def __init__(self, listeners, appNS=None, scope=None):
        ...
    def getScope(self):
        ...
    def getAppNS(self):
        ...
    def setApp(self, app):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def loadViewWithDefName(self, alias, name=None, parent=None, *args, **kwargs):
        ...
    def loadViewWithGenName(self, alias, parent=None, *args, **kwargs):
        ...
    def loadViewBySharedEvent(self, event):
        ...
    def loadViewByCtxEvent(self, event):
        ...
    def loadView(self, event):
        ...
    def findViewByAlias(self, layer, alias):
        ...
    def findViewByName(self, layer, name):
        ...
    def bringViewToFront(self, name):
        ...
    def __getContainer(self, layer):
        ...
    def __loadViewHandler(self, event):
        ...

class PackageImporter(object):
    __slots__: tuple
    __guiLoader: Any
    _aliases: Any
    _handlers: Any
    _contextMenuTypes: Any
    _stateMachineConfigurators: Any
    def __init__(self):
        ...
    def isPackageLoaded(self, path):
        ...
    def getLoadedPackages(self):
        ...
    def getAliasesByPackage(self, path):
        ...
    def load(self, app, seq, arenaGuiType=None, isExtention=False):
        ...
    def unload(self, seq=None):
        ...
    def _loadPackage(self, path, arenaGuiType, isExtention):
        ...
    def _getHandlesWithoutExtensionOverride(self, handlers, arenaGuiType):
        ...
