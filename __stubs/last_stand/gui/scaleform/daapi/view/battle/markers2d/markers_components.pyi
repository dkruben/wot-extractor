# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/battle/markers2d/markers_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from chat_commands_consts import DefaultMarkerSubType as DefaultMarkerSubType
from gui.Scaleform.daapi.view.battle.shared.component_marker.markers_components import World2DActionMarkerComponent as World2DActionMarkerComponent

class Camp2DActionMarkerComponent(World2DActionMarkerComponent):
    def _setupMarker(self, gui, **kwargs):
        ...
    def _deleteMarker(self):
        ...
    def _updateSticky(self, componentID, isSticky):
        ...

class Magnus2DActionMarkerComponent(World2DActionMarkerComponent):
    @classmethod
    def configReader(cls, section):
        ...
    def _setupMarker(self, gui, **kwargs):
        ...
    def _deleteMarker(self):
        ...
