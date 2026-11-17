# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/smoke_screen.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from helpers.EffectsList import effectsFromSection as effectsFromSection
from items import vehicles as vehicles
import BigWorld as BigWorld
import ResMgr as ResMgr
import Math as Math
from Flock import DebugGizmo as DebugGizmo
ENVIRONMENT_EFFECTS_CONFIG_FILE = 'scripts/dynamic_objects.xml'
_SHOW_DEBUG_SMOKE = False
_DEFAULT_SMOKE_INTENSITY = 0.08
_DEFAULT_SMOKE_COLOR: Any
_logger: Any

class _SmokeDebugVisualization(object):
    _startRadius: Any
    _startHeight: Any
    _expansionDuration: Any
    _expandedRadius: Any
    _expandedHeight: Any
    _heightUpFraction: Any
    _totalDuration: Any
    __position: Any
    __callbackID: Any
    __endTime: Any
    __debugGizmo: Any
    __startTime: Any
    __currentMatrix: Any
    def __init__(self, position, equipmentID, endTime):
        ...
    def stop(self):
        ...
    def __onUpdate(self):
        ...
    def __mkMatrix(self, radius, height):
        ...

class SmokeScreen(object):
    vignetteEnabled = False
    activeVignetteEquipmentID = -1
    renderSettings: Any
    __args: Any
    __effectID: Any
    __smokeID: Any
    __debugGizmo: Any
    def __init__(self, smokeId, args):
        ...
    def stop(self):
        ...
    def __loadSmokeScreen(self, equipmentID, position, team):
        ...
    def __stopSmokeScreen(self):
        ...
    @staticmethod
    def enableSmokePostEffect(enabled, smokeInfos=None):
        ...
