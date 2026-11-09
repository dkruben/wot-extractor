# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/SectorBase.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import ResMgr as ResMgr
import SoundGroups as SoundGroups
from helpers import dependency as dependency
from FlagModel import FlagSettings as FlagSettings, FlagModel as FlagModel
from Math import Vector4 as Vector4, Vector3 as Vector3, Vector2 as Vector2, Matrix as Matrix
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from account_helpers.settings_core.settings_constants import GRAPHICS as GRAPHICS
import AnimationSequence as AnimationSequence
ENVIRONMENT_EFFECTS_CONFIG_FILE = 'scripts/dynamic_objects.xml'
_g_sectorBaseSettings = None

class _SectorBaseSettingsCache(object):
    flagModelName: Any
    flagStaffModelName: Any
    radiusModel: Any
    flagAnim: Any
    flagStaffFlagHP: Any
    baseAttachedSoundEventName: Any
    flagBackgroundTex: Any
    flagEmblemTex: Any
    flagEmblemTexCoords: Any
    flagScale: Any
    flagNodeAliasName: Any
    def __init__(self, settings):
        ...
    def initSettings(self, settings):
        ...

class SectorBase(BigWorld.Entity):
    _OVER_TERRAIN_HEIGHT = 0.5
    _PLAYER_TEAM_PARAMS: dict
    __settingsCore: Any
    __flagModel: Any
    __terrainSelectedArea: Any
    capturePercentage: Any
    __isCapturedOnStart: Any
    __baseCaptureSoundObject: Any
    _baseCaptureSirenSoundIsPlaying: Any
    model: Any
    __prereqs: Any
    expectedCaptureTime: Any
    def __init__(self):
        ...
    def prerequisites(self):
        ...
    def onEnterWorld(self, prereqs):
        ...
    def onLeaveWorld(self):
        ...
    def isPlayerTeam(self):
        ...
    def active(self):
        ...
    def set_invadersCount(self, oldValue):
        ...
    def set_pointsPercentage(self, oldValue):
        ...
    def set_capturingStopped(self, oldValue):
        ...
    def set_isActive(self, oldValue):
        ...
    def set_isCaptured(self, oldValue):
        ...
    def set_expectedCaptureTime(self, oldValue):
        ...
    def __getTeamParams(self):
        ...
