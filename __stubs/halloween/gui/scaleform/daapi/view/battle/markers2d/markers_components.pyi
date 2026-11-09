# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/markers2d/markers_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from chat_commands_consts import DefaultMarkerSubType as DefaultMarkerSubType, MarkerType as MarkerType
from gui.Scaleform.daapi.view.battle.shared.component_marker.markers_components import World2DActionMarkerComponent as World2DActionMarkerComponent, World2DLocationMarkerComponent as World2DLocationMarkerComponent, BaseMinimapMarkerComponent as BaseMinimapMarkerComponent, ComponentBitMask as ComponentBitMask
from halloween.gui.halloween_gui_constants import SoulsCollectorMarkerStates as SoulsCollectorMarkerStates, BATTLE_CTRL_ID as BATTLE_CTRL_ID
from halloween.gui.battle_control.halloween_battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE
from gui.battle_control import avatar_getter as avatar_getter

class SoulsCollector2DActionMarkerComponent(World2DActionMarkerComponent):
    __sessionProvider: Any
    __UNHIDE_STATES_TRIGGERS: tuple
    _isMarkerHidden: Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def configReader(cls, section):
        ...
    @property
    def hwBattleGuiCtrl(self):
        ...
    def setVisible(self, isVisible):
        ...
    def _setupMarker(self, gui, **kwargs):
        ...
    def _deleteMarker(self):
        ...
    def _updateMarkerState(self, collected, capacity, isFull, isCampActivated):
        ...
    def _updateMarkerProgress(self, collected, capacity, isFull, isCampActivated):
        ...
    def __onVehicleStateUpdated(self, state, value):
        ...

class Camp2DActionMarkerComponent(World2DActionMarkerComponent):
    def _setupMarker(self, gui, **kwargs):
        ...
    def _deleteMarker(self):
        ...
    def _updateSticky(self, componentID, isSticky):
        ...

class HWLootMarkerComponent(World2DLocationMarkerComponent):
    _guiSessionProvider: Any
    @property
    def bcMarkerType(self):
        ...
    @property
    def _hwLootableComponent(self):
        ...
    def _setupMarker(self, gui, **kwargs):
        ...
    def _togglePlayerSn(self):
        ...
    def _onCapturingEntitiesChanged(self):
        ...
    def _onAvatarVehicleChanged(self):
        ...
    def clear(self):
        ...

class HWLootMinimapComponent(BaseMinimapMarkerComponent):
    @property
    def maskType(self):
        ...
    def _setupMarker(self, gui, **kwargs):
        ...

def getSoulsCollectorMarkerState(isFull):
    ...
