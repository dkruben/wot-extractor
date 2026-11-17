# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/frontline_plugins.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.battle.shared.markers2d.vehicle_plugins import VehicleMarkerPlugin as VehicleMarkerPlugin
from gui.Scaleform.genConsts.BATTLE_MARKER_STATES import BATTLE_MARKER_STATES as BATTLE_MARKER_STATES
_FRONTLINE_STATUS_EFFECTS_PRIORITY: tuple

class FrontlineVehicleMarkerPlugin(VehicleMarkerPlugin):
    def _getMarkerStatusPriority(self, markerState):
        ...

class FrontlineRespawnableVehicleMarkerPlugin(FrontlineVehicleMarkerPlugin):
    _isSquadIndicatorEnabled: Any
    def start(self):
        ...
    def _hideVehicleMarker(self, vehicleID):
        ...
