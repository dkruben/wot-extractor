# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/component_marker/markers_gui_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES as BATTLE_VIEW_ALIASES
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events

class MarkerGUIProvider(object):
    __markers2DPlugin: Any
    __vehicleMarkerPlugin: Any
    __minimapPlugin: Any
    __fullscreenMapPlugin: Any
    __pluginID: Any
    def __init__(self, pluginID):
        ...
    def getMinimapPlugin(self):
        ...
    def getMarkers2DPlugin(self):
        ...
    def getFullscreenMapPlugin(self):
        ...
    def getVehicleMarkerPlugin(self):
        ...
    def clear(self):
        ...
    def __onComponentRegistered(self, event):
        ...
    def __onComponentUnregistered(self, event):
        ...
