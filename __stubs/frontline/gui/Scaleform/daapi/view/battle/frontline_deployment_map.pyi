# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/frontline_deployment_map.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import GUI as GUI
from frontline.gui.Scaleform.daapi.view.meta.FrontlineDeploymentMapMeta import FrontlineDeploymentMapMeta as FrontlineDeploymentMapMeta
from frontline.gui.Scaleform.daapi.view.battle.frontline_minimap import _FRONT_LINE_DEV_VISUALIZATION_SUPPORTED as _FRONT_LINE_DEV_VISUALIZATION_SUPPORTED, DevelopmentRespawnEntriesPlugin as DevelopmentRespawnEntriesPlugin, EpicGlobalSettingsPlugin as EpicGlobalSettingsPlugin, HeadquartersStatusEntriesPlugin as HeadquartersStatusEntriesPlugin, MINIMAP_SCALE_TYPES as MINIMAP_SCALE_TYPES, ProtectionZoneEntriesPlugin as ProtectionZoneEntriesPlugin, RespawningPersonalEntriesPlugin as RespawningPersonalEntriesPlugin, RecoveringVehiclesPlugin as RecoveringVehiclesPlugin, SectorBaseEntriesPlugin as SectorBaseEntriesPlugin, SectorOverlayEntriesPlugin as SectorOverlayEntriesPlugin, SectorStatusEntriesPlugin as SectorStatusEntriesPlugin, StepRepairPointEntriesPlugin as StepRepairPointEntriesPlugin, EpicMinimapPingPlugin as EpicMinimapPingPlugin
from gui.Scaleform.daapi.view.battle.shared.minimap import settings as settings
from gui.Scaleform.daapi.view.battle.shared.minimap.component import _IMAGE_PATH_FORMATTER as _IMAGE_PATH_FORMATTER
from gui.Scaleform.genConsts.LAYER_NAMES import LAYER_NAMES as LAYER_NAMES
from gui.battle_control import minimap_utils as minimap_utils
_S_NAME = settings.ENTRY_SYMBOL_NAME
_C_NAME = settings.CONTAINER_NAME
_DEPLOY_MAP_PATH: Any

class FrontlineDeploymentMapComponent(FrontlineDeploymentMapMeta):
    _size: Any
    _bounds: Any
    _hitAreaSize: Any
    def __init__(self):
        ...
    def getVisualBounds(self):
        ...
    def getRangeScale(self):
        ...
    def canChangeAlpha(self):
        ...
    def setMinimapCenterEntry(self, entryID):
        ...
    def changeMinimapZoom(self, mode):
        ...
    def setEntryParameters(self, id_, doClip=True, scaleType=...):
        ...
    def onZoomModeChanged(self, change):
        ...
    def updateSectorStates(self, states):
        ...
    def _getFlashName(self):
        ...
    def _setupPlugins(self, arenaVisitor):
        ...
    def _createFlashComponent(self):
        ...
    def _getMinimapSize(self):
        ...
    def _processMinimapSize(self, minSize, maxSize):
        ...
    def _getMinimapTexture(self, arenaVisitor):
        ...

class DeploymentSectorBaseEntriesPlugin(SectorBaseEntriesPlugin):
    def __init__(self, parentObj):
        ...

class DeploymentHeadquartersStatusEntriesPlugin(HeadquartersStatusEntriesPlugin):
    def __init__(self, parentObj):
        ...
