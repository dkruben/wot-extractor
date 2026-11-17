# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/client/ApplicationPoint.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
import BigWorld as BigWorld
import CGF as CGF
import CombatSelectedArea as CombatSelectedArea
import Math as Math
import SoundGroups as SoundGroups
import math as math
import math_utils as math_utils
from account_helpers.settings_core.settings_constants import GRAPHICS as GRAPHICS
from helpers import dependency as dependency
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from items import vehicles as vehicles
from items.artefacts import AoeEffects as AoeEffects, AreaShow as AreaShow
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control.battle_constants import FEEDBACK_EVENT_ID as FEEDBACK_EVENT_ID
from AreaOfEffect import EffectRunner as EffectRunner
from typing import List as List
from LightComponents import OmniLightComponent as OmniLightComponent
_EQUIPMENT_APPLICATION_POINTS: dict

class ApplicationPoint(BigWorld.Entity):
    _effect: Any
    def __init__(self):
        ...
    @property
    def areaColor(self):
        ...
    def prerequisites(self):
        ...
    def onEnterWorld(self, prereqs):
        ...
    def onLeaveWorld(self):
        ...

class _ApplicationPointEffect(object):
    __slots__: tuple
    _entity: Any
    _equipment: Any
    def __init__(self, entity, equipment):
        ...
    def __del__(self):
        ...
    @property
    def equipment(self):
        ...
    @property
    def areaColor(self):
        ...
    def onEnterWorld(self):
        ...
    def onLeaveWorld(self):
        ...

class _Comp7ApplicationPointEffect(_ApplicationPointEffect):
    _VIEW_STATE_DURATION = 0.0
    _guiSessionProvider: Any
    _position: Any
    _direction: Any
    _markerID: Any
    _area: Any
    _vehicle: Any
    __areaGO: Any
    _callbackDelayer: Any
    def __init__(self, *args, **kwargs):
        ...
    def onEnterWorld(self, prereqs):
        ...
    def onLeaveWorld(self):
        ...
    def _getAreaDuration(self):
        ...
    def _getViewStateDuration(self):
        ...
    def _getFeedbackEventId(self):
        ...
    def _createMarker(self, duration):
        ...
    def _clearMarker(self):
        ...
    def _createArea(self, duration):
        ...
    def _clearArea(self):
        ...
    def _getEndTime(self):
        ...
    def _isEnded(self):
        ...
    def _updateViewState(self):
        ...
    def _updateCoordinates(self):
        ...
    def _isEnemy(self):
        ...
    def _isVisible(self):
        ...
    def _getRadius(self):
        ...
    def _onAreaGOLoaded(self, objects, queue):
        ...

class _Comp7ReconApplicationPointEffect(_Comp7ApplicationPointEffect):
    _VIEW_STATE_DURATION = 5.0
    _COMP7_RECON_MARKER = 'COMP7_RECON'
    _markerID: Any
    def _getFeedbackEventId(self):
        ...
    def _createMarker(self, duration):
        ...
    def _clearMarker(self):
        ...

class _Comp7IlluminationFlareApplicationPointEffect(_Comp7ApplicationPointEffect):
    _APPLY_SOUND_SELF = 'comp_7_ability_flare_apply'
    _APPLY_SOUND_ALLY = 'comp_7_ability_flare_ally'
    _APPLY_SOUND_ENEMY = 'comp_7_ability_flare_enemy'
    _START_EFFECT_TIME = 2.0
    _END_EFFECT_OFFSET = 2.7
    _settingsCore: Any
    _rocketAreaGO: Any
    _omniLightGO: Any
    _areaGO: Any
    _effectStart: Any
    _effectIdle: Any
    _effectEnd: Any
    _spaceID: Any
    _soundObj: Any
    _markerID: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def areaColor(self):
        ...
    def _getRadius(self):
        ...
    def _getAreaDuration(self):
        ...
    def _getViewStateDuration(self):
        ...
    def _createMarker(self, duration):
        ...
    def _clearMarker(self):
        ...
    def _clearArea(self):
        ...
    def onEnterWorld(self, prereqs):
        ...
    def _playApplySound(self):
        ...
    def _showDelayedPrefab(self):
        ...
    def _onAreaGOLoaded(self, objects, queue):
        ...
    def _activatePrefab(self):
        ...
    def _updateTransformTick(self):
        ...
    def _isVisible(self):
        ...
    def _updateViewState(self):
        ...

class _Comp7RedLineApplicationPointEffect(_Comp7ApplicationPointEffect, EffectRunner):
    _VIEW_STATE_DURATION = 5.0
    def __init__(self, *args, **kwargs):
        ...
    def _getFeedbackEventId(self):
        ...
    def onEnterWorld(self, prereqs):
        ...
    def _createMarker(self, duration):
        ...
    def _playEffect(self, duration):
        ...

class _PoiArtilleryAoeApplicationPointEffect(_Comp7RedLineApplicationPointEffect):
    def _getRadius(self):
        ...

def _equipmentEffectFactory(entity):
    ...
