# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/pve_base/component_marker/markers_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import ResMgr as ResMgr
from chat_commands_consts import MarkerType as MarkerType
from gui.Scaleform.daapi.view.battle.shared.component_marker.markers_components import BaseMinimapMarkerComponent as BaseMinimapMarkerComponent, World2DActionMarkerComponent as World2DActionMarkerComponent, ComponentBitMask as ComponentBitMask, World2DLocationMarkerComponent as World2DLocationMarkerComponent
from gui.impl.backport import getIntegralFormat as getIntegralFormat

class PveAttackDirectionComponent(BaseMinimapMarkerComponent):
    @classmethod
    def configReader(cls, section):
        ...
    def _setupMarker(self, gui, **kwargs):
        ...

class PveAttackDirectionMinimapComponent(PveAttackDirectionComponent):
    @property
    def maskType(self):
        ...

class PveAttackDirectionFullscreenMapComponent(PveAttackDirectionComponent):
    @property
    def maskType(self):
        ...

class PveFlagMinimapComponent(BaseMinimapMarkerComponent):
    def _setupMarker(self, gui, **kwargs):
        ...
    @property
    def maskType(self):
        ...

class PveFlagFullscreenMapComponent(BaseMinimapMarkerComponent):
    def _setupMarker(self, gui, **kwargs):
        ...
    @property
    def maskType(self):
        ...

class PveTargetFlagMinimapComponent(BaseMinimapMarkerComponent):
    @property
    def maskType(self):
        ...

class PveTargetFlagFullscreenMapComponent(BaseMinimapMarkerComponent):
    @property
    def maskType(self):
        ...

class PveFlagLocationMarkerComponent(World2DLocationMarkerComponent):
    def _setupMarker(self, gui, **kwargs):
        ...
    @property
    def bcMarkerType(self):
        ...

class PveFlagVehicleMarkerComponent(World2DActionMarkerComponent):
    _vehicleMarkerGUI: Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def configReader(cls, section):
        ...
    def attachGUI(self, guiProvider, **kwargs):
        ...
    def update(self, distance, *args, **kwargs):
        ...
    def clear(self):
        ...
    def _setupMarker(self, gui, **kwargs):
        ...
    def _deleteMarker(self):
        ...
    def _getVehicleMarker(self):
        ...
    def _insertSymbol(self):
        ...
    def _removeSymbol(self):
        ...
    def _updateDistance(self, distance):
        ...

class PveAnimatedFlagMarkerComponent(World2DLocationMarkerComponent):
    @property
    def bcMarkerType(self):
        ...
