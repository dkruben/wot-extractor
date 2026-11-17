# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gui_loader.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks.wulf import GuiApplication as GuiApplication
from gui.impl.gui_factories import GuiEntitiesFactories as GuiEntitiesFactories
from gui.impl.optimization_manager import GraphicsOptimizationManager as GraphicsOptimizationManager
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from frameworks.wulf.tutorial import Tutorial as Tutorial
from frameworks.wulf.ui_logger import UILogger as UILogger

class GuiLoader(IGuiLoader):
    __gui: Any
    __entitiesFactory: Any
    __graphicsOptimizationManager: Any
    def __init__(self):
        ...
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
