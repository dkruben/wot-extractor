# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/epic_maps_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import Math as Math
import CommandMapping as CommandMapping
import Event as Event
from chat_commands_consts import INVALID_VEHICLE_POSITION as INVALID_VEHICLE_POSITION
from gui.battle_control import event_dispatcher as gui_event_dispatcher
from gui.battle_control.controllers.default_maps_ctrl import DefaultMapsController as DefaultMapsController

class EpicMapsController(DefaultMapsController):
    __overviewMapUi: Any
    __isOverlayActive: Any
    __overviewMapScreenVisible: Any
    __savedToggleState: Any
    onOverlayTriggered: Any
    onVisibilityChanged: Any
    _miniMapUi: Any
    _eManager: Any
    def __init__(self, setup):
        ...
    def setViewComponents(self, *components):
        ...
    def stopControl(self):
        ...
    def clearViewComponents(self):
        ...
    def getMinimapZoomMode(self):
        ...
    def getMinimapCenterPosition(self):
        ...
    def getVehiclePosition(self, vID):
        ...
    def overlayTriggered(self, isActive):
        ...
    @property
    def overlayActive(self):
        ...
    @property
    def overviewMapScreenVisible(self):
        ...
    def setOverviewMapScreenVisibility(self, isVisible):
        ...
    def overviewMapTriggered(self):
        ...
