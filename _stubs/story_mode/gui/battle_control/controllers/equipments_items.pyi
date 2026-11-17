# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/battle_control/controllers/equipments_items.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
import typing as typing
from functools import partial as partial
import BigWorld as BigWorld
import CGF as CGF
import Math as Math
import SoundGroups as SoundGroups
from typing import List as List
from AvatarInputHandler import MapCaseMode as MapCaseMode
from SMReconAbilityEntityComponent import SMReconAbilityEntityComponent as SMReconAbilityEntityComponent
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.Scaleform.genConsts.ANIMATION_TYPES import ANIMATION_TYPES as ANIMATION_TYPES
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control.controllers.consumables import equipment_ctrl as equipment_ctrl
from gui.shared.system_factory import registerEquipmentItem as registerEquipmentItem
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from story_mode.avatar_input_handler.control_modes import StoryModeArcadeMinefieldControlMode as StoryModeArcadeMinefieldControlMode, SMStrategicMapCaseControlMode as SMStrategicMapCaseControlMode
from story_mode.gui.story_mode_gui_constants import ABILITY_ON_COOLDOWN_ACTIVATION_ERROR_KEY as ABILITY_ON_COOLDOWN_ACTIVATION_ERROR_KEY
from story_mode.gui.sound_constants import SMN_ARCADE_ARTILLERY_ACTIVATE_SOUND as SMN_ARCADE_ARTILLERY_ACTIVATE_SOUND, SMN_ARCADE_ARTILLERY_DEACTIVATE_SOUND as SMN_ARCADE_ARTILLERY_DEACTIVATE_SOUND, SMN_ARCADE_ARTILLERY_SET_SOUND as SMN_ARCADE_ARTILLERY_SET_SOUND, SMN_ARCADE_ARTILLERY_STATE_GROUP as SMN_ARCADE_ARTILLERY_STATE_GROUP, SMN_ARCADE_ARTILLERY_STATE_IN as SMN_ARCADE_ARTILLERY_STATE_IN, SMN_ARCADE_ARTILLERY_STATE_OUT as SMN_ARCADE_ARTILLERY_STATE_OUT, SMN_ARCADE_ARTILLERY_DESTROYER_SOUND as SMN_ARCADE_ARTILLERY_DESTROYER_SOUND, DISTRACTION_ABILITY_ACTIVATE_SOUND as DISTRACTION_ABILITY_ACTIVATE_SOUND, DISTRACTION_ABILITY_CANCEL_SOUND as DISTRACTION_ABILITY_CANCEL_SOUND, DISTRACTION_ABILITY_SET_SOUND as DISTRACTION_ABILITY_SET_SOUND, RECON_ABILITY_ACTIVATE_SOUND as RECON_ABILITY_ACTIVATE_SOUND, RECON_ABILITY_DEACTIVATE_SOUND as RECON_ABILITY_DEACTIVATE_SOUND, RECON_ABILITY_CANCEL_SOUND as RECON_ABILITY_CANCEL_SOUND, RECON_ABILITY_SET_SOUND as RECON_ABILITY_SET_SOUND, RECON_ABILITY_ENGINE_STOP_SOUND as RECON_ABILITY_ENGINE_STOP_SOUND, RECON_ABILITY_ENGINE_START_SOUND as RECON_ABILITY_ENGINE_START_SOUND
from story_mode_common.story_mode_constants import RECON_ABILITY as RECON_ABILITY, EQUIPMENT_STAGES as STAGES, DISTRACTION_ABILITY as DISTRACTION_ABILITY, SCC_AIRSTRIKE_ABILITY as SCC_AIRSTRIKE_ABILITY, SCC_AIRSTRIKE_ABILITY_HARD as SCC_AIRSTRIKE_ABILITY_HARD
from Avatar import Avatar as Avatar
from items import artefacts as artefacts
_SMN_ARCADE_ARTILLERY_ITEMS: tuple
_SMN_ARCADE_ARTILLERY_DESTROYER_ITEMS: set
_EQUIPMENT_STAGE_DESTROYER_SHOOTING = -1

class _SmnRefillEquipmentItem(equipment_ctrl._RefillEquipmentItem):
    _mapCaseModeActive: Any
    def __init__(self, *args, **kwargs):
        ...
    def getAimingControlMode(self):
        ...
    def update(self, quantity, stage, timeRemaining, totalTime):
        ...

class _SmnArcadeArtilleryItem(_SmnRefillEquipmentItem, equipment_ctrl._ArcadeArtilleryItem):
    ...

class _SmnReplayArcadeArtilleryItem(_SmnRefillEquipmentItem, equipment_ctrl._ReplayArcadeArtilleryItem):
    ...

class _SmnArcadeArtilleryBaseItem(object):
    def update(self, quantity, stage, timeRemaining, totalTime):
        ...

class _SmnArcadeArtilleryDestroyerItem(_SmnArcadeArtilleryBaseItem, equipment_ctrl._ArcadeArtilleryItem):
    ...

class _SmnReplayArcadeArtilleryDestroyerItem(_SmnArcadeArtilleryBaseItem, equipment_ctrl._ReplayArcadeArtilleryItem):
    ...

class AbilityItem(equipment_ctrl._RefillEquipmentItem, equipment_ctrl._OrderItem):
    _abilityUseInProgress: Any
    def __init__(self, *args, **kwargs):
        ...
    def canActivate(self, entityName=None, avatar=None):
        ...
    def getTimeRemaining(self):
        ...
    def getAimingControlMode(self):
        ...
    def _playSoundAndChangeState(self, sound, final):
        ...

class SMStrategicAbilityItem(AbilityItem):
    _PREFAB_URL = ''
    _prefab: Any
    _isSelecting: Any
    def __init__(self, descriptor, quantity, stage, timeRemaining, totalTime, tags):
        ...
    def getAimingControlMode(self):
        ...
    def updateMapCase(self, stage=None):
        ...
    def _cancelPreviousMode(self):
        ...
    def clear(self):
        ...
    def _updateVisual(self, stage):
        ...
    def _loadPrefab(self):
        ...
    def _onPrefabLoaded(self, objects, queue):
        ...
    def _removePrefab(self):
        ...

class DistractionAbilityItem(SMStrategicAbilityItem):
    _PREFAB_URL = 'content/CGFPrefabs/Storymode/tank_rectangle.prefab'
    def update(self, quantity, stage, timeRemaining, totalTime):
        ...

class ReconAbilityItem(SMStrategicAbilityItem):
    _PREFAB_URL = 'content/CGFPrefabs/Storymode/tank_rectangle.prefab'
    appLoader: Any
    _isEntityViewModeActive: Any
    _abilityUseInProgress: Any
    def __init__(self, *args, **kwargs):
        ...
    def clear(self):
        ...
    def isInCooldown(self):
        ...
    def isInPreparing(self):
        ...
    def canDeactivate(self):
        ...
    @property
    def becomeReady(self):
        ...
    def getAnimationType(self):
        ...
    def updateMapCase(self, stage=None):
        ...
    def update(self, quantity, stage, timeRemaining, totalTime):
        ...
    def _onSMReconEntityCreated(self, entityId):
        ...
    def _activateMapCase(self):
        ...
    def _turnOffMapCase(self):
        ...
    @staticmethod
    def _changeControlMode(mode, **kwargs):
        ...

class AbilityReplayItem(equipment_ctrl._ReplayOrderItem):
    def getAimingControlMode(self):
        ...

class SccAirstrikeAbilityItem(SMStrategicAbilityItem, _SmnRefillEquipmentItem):
    ...

class SccReplayAirstrikeAbilityItem(_SmnRefillEquipmentItem, equipment_ctrl._ReplayOrderItem):
    ...

def register():
    ...
