# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/client/comp7_core/gui/Scaleform/daapi/view/battle/markers_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from chat_commands_consts import INVALID_TARGET_ID as INVALID_TARGET_ID
from gui.Scaleform.daapi.view.battle.shared.component_marker.markers_components import MinimapMarkerComponent as MinimapMarkerComponent
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from items import vehicles as vehicles

class IlluminationFlareMinimapMarker(MinimapMarkerComponent):
    _callbackDelayer: Any
    _launchTime: Any
    def __init__(self, config, matrixProduct, entity=None, targetID=..., isVisible=True):
        ...
    @property
    def _equipment(self):
        ...
    def _createMarker(self, **kwargs):
        ...
    def _deleteMarker(self):
        ...
    def _updateRadius(self):
        ...
    def _setRadius(self, radius):
        ...
