# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/skeletons/gui/impl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from skeletons.gui.game_control import IGameController as IGameController
from Event import Event as Event
from frameworks.wulf.resource_manager import ResourceManager as ResourceManager
from frameworks.wulf.system_locale import SystemLocale as SystemLocale
from frameworks.wulf.formatters import Formatters as Formatters
from frameworks.wulf.tutorial import Tutorial as Tutorial
from frameworks.wulf.ui_logger import UILogger as UILogger
from frameworks.wulf.windows_system.windows_manager import WindowsManager as WindowsManager
from frameworks.wulf.view.layout_manager import LayoutManager as LayoutManager
from gui.impl.gui_factories import GuiEntitiesFactories as GuiEntitiesFactories

class IGuiLoader(object):
    __slots__: tuple
    @property
    def resourceManager(self):
        ...
    @property
    def windowsManager(self):
        ...
    @property
    def layoutManager(self):
        ...
    @property
    def systemLocale(self):
        ...
    @property
    def formatters(self):
        ...
    @property
    def tutorial(self):
        ...
    @property
    def uiLogger(self):
        ...
    @property
    def scale(self):
        ...
    @property
    def entitiesFactory(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...

class INotificationWindowController(IGameController):
    onPostponedQueueUpdated = None
    def append(self, command):
        ...
    def hasWindow(self, window):
        ...
    def isEnabled(self):
        ...
    def isExecuting(self):
        ...
    def postponeActive(self):
        ...
    def releasePostponed(self):
        ...
    def lock(self, key):
        ...
    def unlock(self, key):
        ...
    def hasLock(self, key):
        ...
    @property
    def activeQueueLength(self):
        ...
    def clear(self):
        ...
    @property
    def postponedCount(self):
        ...

class IFullscreenManager(object):
    __slots__: tuple
    def setEnabled(self, value):
        ...
    def init(self):
        ...
    def fini(self):
        ...

class IWindowLoaderController(IGameController):
    __slots__: tuple
