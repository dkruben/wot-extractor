# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/stronghold/plugins.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.battle.shared.markers2d.vehicle_plugins import VehicleMarkerPlugin as VehicleMarkerPlugin
from gui.Scaleform.genConsts.BATTLE_MARKER_STATES import BATTLE_MARKER_STATES as _STATES

class _StrongholdInspireMarker(object):
    __slots__: tuple
    isSourceVehicle: Any
    isInactivation: Any
    def __init__(self, isSourceVehicle, isInactivation):
        ...
    def needInspireCounter(self):
        ...
    def getHideStatusID(self):
        ...
    def getStatusID(self):
        ...

class StrongholdVehicleMarkerPlugin(VehicleMarkerPlugin):
    def _updateInspireMarker(self, vehicleID, handle, isSourceVehicle, isInactivation, endTime, duration, primary=True, animated=True, equipmentID=None):
        ...
