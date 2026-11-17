# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/scaleform/daapi/view/battle/markers2d/manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from fort_rush.gui.fort_rush_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.Scaleform.daapi.view.battle.shared.markers2d import MarkersManager as MarkersManager
from gui.Scaleform.daapi.view.battle.shared.markers2d.vehicle_plugins import RespawnableVehicleMarkerPlugin as RespawnableVehicleMarkerPlugin
from gui.Scaleform.framework import getSwfExtensionUrl as getSwfExtensionUrl
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_FORT_RUSH_VEHICLE_MARKER = 'FortRushVehicleMarkerUI'

class FortRushVehicleMarkerPlugin(RespawnableVehicleMarkerPlugin):
    _sessionProvider: Any
    def start(self):
        ...
    def stop(self):
        ...
    def _getMarkerSymbol(self, vehicleID):
        ...
    def __onVehicleInvulnerabilityChanged(self, vehicleID, isActive):
        ...
    def _setMarkerInitialState(self, marker, vInfo):
        ...
    def __setInvulnerableIconVisible(self, vehicleID, isVisible):
        ...

class FortRushMarkersManager(MarkersManager):
    MARKERS_MANAGER_SWF: Any
    def _setupPlugins(self, arenaVisitor):
        ...
