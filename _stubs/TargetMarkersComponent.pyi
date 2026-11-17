# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/TargetMarkersComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import listvalues as listvalues, viewitems as viewitems
import BigWorld as BigWorld
import Math as Math
import TriggersManager as TriggersManager
from gui.battle_control.controllers.area_marker_ctrl import AreaMarkersController as AreaMarkersController
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class TargetMarkersComponent(DynamicScriptComponent, TriggersManager.ITriggerListener):
    sessionProvider: Any
    _isReconnect: Any
    _markers: Any
    def __init__(self):
        ...
    def onDestroy(self):
        ...
    def addMarker(self, markerSetting):
        ...
    def removeMarkers(self, markerSettings):
        ...
    def onTriggerActivated(self, args):
        ...
    def _onAvatarReady(self):
        ...
    def _createVisibleMarker(self, vehicleId, settings, vehicle):
        ...
    def _createInvisibleMarker(self, vehicleId, settings, position):
        ...
    def _createMarker(self, vehicleId, settingId, markerType, matrix, vehicle=None):
        ...
    def _deleteMarker(self, targetId, marker):
        ...
    def _deleteMarkerBySettingId(self, targetId, settingId):
        ...
    def _getSettingId(self, targetId, marker):
        ...
    def _removeMarker(self, markerID):
        ...
