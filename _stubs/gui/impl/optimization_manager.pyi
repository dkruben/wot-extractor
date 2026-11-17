# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/optimization_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from future.utils import itervalues as itervalues, iteritems as iteritems
from frameworks.wulf import WindowStatus as WindowStatus
from frameworks.wulf.gui_constants import ShowingStatus as ShowingStatus
from gui.graphics_optimization_controller.utils import rescaleRectBounds as rescaleRectBounds
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import GameEvent as GameEvent
from helpers import dependency as dependency
from skeletons.gui.game_control import IGraphicsOptimizationController as IGraphicsOptimizationController
_logger: Any
DEFAULT_APPLICATION_SCALE = 1.0

class GraphicsOptimizationManager(object):
    __optimizationController: Any
    __gfWindowsOptimizationIDs: Any
    __windowsManager: Any
    __scale: Any
    def __init__(self):
        ...
    def init(self, windowsManager, scale):
        ...
    def fini(self):
        ...
    def switchOptimizationEnabled(self, value):
        ...
    def __isOptimizationAvailable(self, alias):
        ...
    def __isOptimizationEnabled(self, alias):
        ...
    def __onAppResolutionChanged(self, event):
        ...
    def __onWindowSizeChanged(self, uniqueID, width, height):
        ...
    def __onWindowPositionChanged(self, uniqueID, x, y):
        ...
    def __onWindowShowingStatusChanged(self, uniqueID, status):
        ...
    def __addWindowListeners(self, window):
        ...
    def __removeWindowListeners(self, window):
        ...
    def __invalidateRectangles(self):
        ...
    def __handleGuiVisibility(self):
        ...
    def __onSettingsChanged(self):
        ...
