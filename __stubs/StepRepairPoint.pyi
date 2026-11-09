# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/StepRepairPoint.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import AnimationSequence as AnimationSequence
from Math import Vector2 as Vector2
from Math import Matrix as Matrix
import ResMgr as ResMgr
import SoundGroups as SoundGroups
ENVIRONMENT_EFFECTS_CONFIG_FILE = 'scripts/dynamic_objects.xml'
_g_stepRepairPointSettings = None

class _StepRepairPointSettingsCache(object):
    flagModel: Any
    radiusModel: Any
    flagAnim: Any
    attachedSoundEventName: Any
    def __init__(self, settings):
        ...
    def initSettings(self, settings):
        ...

class StepRepairPoint(BigWorld.Entity):
    _COLOR = 4294967295
    _OVER_TERRAIN_HEIGHT = 0.5
    __stepRepairPointSoundObject: Any
    __terrainSelectedArea: Any
    __animator: Any
    model: Any
    def __init__(self):
        ...
    def prerequisites(self):
        ...
    def onEnterWorld(self, prereqs):
        ...
    def onLeaveWorld(self):
        ...
    def isActiveForPlayerTeam(self):
        ...
    def set_team(self, oldValue):
        ...
