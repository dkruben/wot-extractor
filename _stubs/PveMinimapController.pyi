# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/PveMinimapController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from constants import PVE_MINIMAP_DEFAULT_ZOOM as PVE_MINIMAP_DEFAULT_ZOOM, PVE_MINIMAP_DEFAULT_BORDERS as PVE_MINIMAP_DEFAULT_BORDERS
from gui.shared import g_eventBus as g_eventBus, events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent

class PveMinimapController(DynamicScriptComponent):
    def set_minimapData(self, prev):
        ...
    def _onAvatarReady(self):
        ...
    def _sendZoomUpdated(self):
        ...
    def _sendMinimapBorders(self):
        ...
