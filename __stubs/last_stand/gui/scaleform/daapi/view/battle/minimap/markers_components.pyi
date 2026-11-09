# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/battle/minimap/markers_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from chat_commands_consts import MarkerType as MarkerType
from gui.Scaleform.daapi.view.battle.shared.component_marker.markers_components import MinimapMarkerComponent as MinimapMarkerComponent, StaticDeathZoneMinimapMarkerComponent as StaticDeathZoneMinimapMarkerComponent
import SoundGroups as SoundGroups
from gui.Scaleform.daapi.view.battle.epic.minimap import MINIMAP_SCALE_TYPES as MINIMAP_SCALE_TYPES
from gui.Scaleform.daapi.view.battle.shared.minimap import settings as settings

class CampMinimapMarkerComponent(MinimapMarkerComponent):
    _isMarkerExists: Any
    @property
    def bcMarkerType(self):
        ...
    def _createMarker(self, **kwargs):
        ...
    def _setupMarker(self, gui, **kwargs):
        ...

class MagnusMinimapMarkerComponent(CampMinimapMarkerComponent):
    def _setupMarker(self, gui, **kwargs):
        ...

class BotSpawnNotificationMarkerComponent(MinimapMarkerComponent):
    _ANIMATION_NAME = 'firstEnemy'
    _GUI_PROPS_NAME = 'enemy'
    def _setupMarker(self, gui, **kwargs):
        ...

class LSStaticDeathZoneMinimapMarkerComponent(StaticDeathZoneMinimapMarkerComponent):
    _MINIMAP_1M_IN_PX = 0.21
    def _setupMarker(self, gui, **kwargs):
        ...
    def _getSize(self):
        ...
