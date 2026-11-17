# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/graphics_optimization_controller/optimization_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import GUI as GUI
import Event as Event
from gui.graphics_optimization_controller.settings import OPTIMIZED_VIEWS_SETTINGS as OPTIMIZED_VIEWS_SETTINGS
from gui.graphics_optimization_controller.utils import getRectBounds as getRectBounds, PERMANENT_SETTING_ID as PERMANENT_SETTING_ID, getSettingsNames as getSettingsNames
from gui.shared import g_eventBus as g_eventBus, events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.system_factory import collectOptimizedViews as collectOptimizedViews, registerOptimizedViews as registerOptimizedViews
from helpers import dependency as dependency
from ids_generators import Int32IDGenerator as Int32IDGenerator
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.game_control import IGraphicsOptimizationController as IGraphicsOptimizationController
_logger: Any

class GraphicsOptimizationController(IGraphicsOptimizationController):
    __settingsCore: Any
    __idsGenerator: Any
    __optimizer: Any
    __cache: Any
    __config: Any
    __isUiVisible: Any
    __settingsNames: Any
    __em: Any
    onUiVisibilityToggled: Any
    onSettingsChanged: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def getConfig(self):
        ...
    def updateConfig(self, config):
        ...
    def registerOptimizationArea(self, x, y, width, height):
        ...
    def unregisterOptimizationArea(self, optimizationID):
        ...
    def updateOptimizationArea(self, optimizationID, x, y, width, height):
        ...
    def switchOptimizationEnabled(self, value):
        ...
    def getEnable(self):
        ...
    def isOptimizationAvailable(self, alias):
        ...
    def isOptimizationEnabled(self, alias):
        ...
    def __handleGuiVisibility(self, event):
        ...
    def __onSettingsChanged(self, diff):
        ...
