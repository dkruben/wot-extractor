# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/pve_base/fullmap.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import GUI as GUI
from gui.Scaleform.daapi.view.battle.classic.minimap import GlobalSettingsPlugin as GlobalSettingsPlugin
from gui.Scaleform.daapi.view.battle.pve_base.minimap import PveMinimapComponent as PveMinimapComponent
from gui.Scaleform.daapi.view.battle.shared.minimap.plugins import PersonalEntriesPlugin as PersonalEntriesPlugin
from gui.Scaleform.genConsts.LAYER_NAMES import LAYER_NAMES as LAYER_NAMES
from gui.battle_control import minimap_utils as minimap_utils
_FLASH_NAME = 'pveFullMap'
_MINIMAP_COMPONENT_PATH: Any
_MINIMAP_SIZE: tuple

class PveFullMapGlobalSettingsPlugin(GlobalSettingsPlugin):
    def _toogleVisible(self):
        ...

class PveFullMapPersonalEntriesPlugin(PersonalEntriesPlugin):
    __slots__: tuple
    def __init__(self, parentObj):
        ...

class PveFullMapComponent(PveMinimapComponent):
    def setMinimapCenterEntry(self, entityID):
        ...
    def setVisibleRect(self, bl, tr):
        ...
    def setZoom(self, zoom):
        ...
    def _setupPlugins(self, arenaVisitor):
        ...
    def _getFlashName(self):
        ...
    def _createFlashComponent(self):
        ...
    def _getMinimapSize(self):
        ...
