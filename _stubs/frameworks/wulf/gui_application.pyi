# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/frameworks/wulf/gui_application.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from helpers import time_utils as time_utils
from .formatters import Formatters as Formatters
from .py_object_wrappers import PyGuiApplication as PyGuiApplication
from .resource_manager import ResourceManager as ResourceManager
from .tutorial import Tutorial as Tutorial
from .ui_logger import UILogger as UILogger
from .view.layout_manager import LayoutManager as LayoutManager
from .windows_system.windows_manager import WindowsManager as WindowsManager
from typing import Callable as Callable

class GuiApplication(object):
    __instance = None
    __impl: Any
    __windowsManager: Any
    __layoutManager: Any
    __resourceManager: Any
    __formatters: Any
    __tutorial: Any
    __uiLogger: Any
    def __init__(self):
        ...
    @classmethod
    def getInstance(cls):
        ...
    @property
    def windowsManager(self):
        ...
    @property
    def layoutManager(self):
        ...
    @property
    def resourceManager(self):
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
    def init(self):
        ...
    def destroy(self):
        ...
    def _setServerTimeCallback(self, callback):
        ...
