# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/minimap/markers_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from chat_commands_consts import MarkerType as MarkerType
from gui.Scaleform.daapi.view.battle.shared.component_marker.markers_components import MinimapMarkerComponent as MinimapMarkerComponent, StaticDeathZoneMinimapMarkerComponent as StaticDeathZoneMinimapMarkerComponent
from halloween.gui.halloween_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
import SoundGroups as SoundGroups
from gui.Scaleform.daapi.view.battle.epic.minimap import MINIMAP_SCALE_TYPES as MINIMAP_SCALE_TYPES
from gui.Scaleform.daapi.view.battle.shared.minimap import settings as settings
from helpers import dependency as dependency
from halloween.gui.halloween_gui_constants import SoulsCollectorMarkerStates as SoulsCollectorMarkerStates
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from HWDeathZone import HWDeathZone as HWDeathZone

class CampMinimapMarkerComponent(MinimapMarkerComponent):
    _isMarkerExists: Any
    @property
    def bcMarkerType(self):
        ...
    @classmethod
    def configReader(cls, section):
        ...
    def _createMarker(self, **kwargs):
        ...
    def _setupMarker(self, gui, **kwargs):
        ...

class SoulsCollectorMinimapMarkerComponent(CampMinimapMarkerComponent):
    __sessionProvider: Any
    @property
    def hwBattleGuiCtrl(self):
        ...
    def _deleteMarker(self):
        ...
    def _setupMarker(self, gui, **kwargs):
        ...
    def _updateMarkerState(self, collected, capacity, isFull, isCampActivated):
        ...

class BotSpawnNotificationMarkerComponent(MinimapMarkerComponent):
    _ANIMATION_NAME = 'firstEnemy'
    _GUI_PROPS_NAME = 'enemy'
    def _setupMarker(self, gui, **kwargs):
        ...

class HWStaticDeathZoneMinimapMarkerComponent(StaticDeathZoneMinimapMarkerComponent):
    _MINIMAP_1M_IN_PX = 0.21
    def _setupMarker(self, gui, **kwargs):
        ...
    def _getSize(self):
        ...

class HWResizableDeathZoneMinimapMarkerComponent(HWStaticDeathZoneMinimapMarkerComponent):
    _maskingPolygons: Any
    _polygon: Any
    def _setupMarker(self, gui, **kwargs):
        ...
    def detachGUI(self):
        ...
    def _fillMaskingPolygons(self, mask, xc, yc):
        ...
    def getPolygon(self):
        ...
    def _resize(self, zone):
        ...
    def _updateMasks(self):
        ...

def getSoulsCollectorMinimapMarkerState(isFull, isCampActivated):
    ...
