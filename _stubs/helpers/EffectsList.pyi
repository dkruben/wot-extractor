# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/helpers/EffectsList.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import random as random
from collections import namedtuple as namedtuple
from enum import Enum as Enum
from functools import partial as partial
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from past.builtins import intern as intern, xrange as xrange
import AnimationSequence as AnimationSequence
import BigWorld as BigWorld
import Math as Math
import WWISE as WWISE
import SoundGroups as SoundGroups
import helpers as helpers
import material_kinds as material_kinds
from helpers import dependency as dependency, DecalMap as DecalMap
from helpers.PixieBG import PixieBG as PixieBG
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from soft_exception import SoftException as SoftException
from vehicle_systems.sound_objects import getGunSoundObject as getGunSoundObject, getGunSoundObjectDistance as getGunSoundObjectDistance
from constants import IS_EDITOR as IS_EDITOR
from wrapped_reflection_framework import reflectedNamedTuple as reflectedNamedTuple
from gui.Scaleform.genConsts.EPIC_CONSTS import EPIC_CONSTS as EPIC_CONSTS
_logger: Any
COLOR_WHITE = 4294967295
_ALLOW_DYNAMIC_LIGHTS = True
KeyPoint: Any
EffectsTimeLine: Any
EffectsTimeLinePrereqs: Any
__START_KEY_POINT: Any
SoundStartParam: Any
ImpactNames: Any
_effectDescFactory: dict
_effectDescTypeToKey: dict

class SpecialKeyPointNames(object):
    START = 'start'
    END = 'end'
    STATIC = 'static'

class EFFECT_DELETE_REASON(Enum):
    LIST_DESTRUCTION = 0
    REACHED_END_KEY = 1
    KEEP_POSTEFFECTS = 2
    FORCE_DELETE = 3

class EffectsList(object):
    __slots__: tuple
    __effectDescList: Any
    relatedEffects: Any
    def __init__(self, section):
        ...
    def prerequisites(self):
        ...
    def attachTo(self, model, data, key, excludeTags=None, **args):
        ...
    def reattachTo(self, model, data):
        ...
    def detachFrom(self, data, key, reason=...):
        ...
    def detachAllFrom(self, data, keepPosteffects=False, forceDelete=False):
        ...
    def descriptors(self):
        ...

class EffectsListPlayer(object):
    effectsList: Any
    isPlaying: Any
    activeEffects: Any
    clearInProgress = False
    __keyPoints: Any
    __effectsList: Any
    __excludeTags: Any
    __args: Any
    __curKeyPoint: Any
    __callbackFunc: Any
    __callbackID: Any
    __keyPointIdx: Any
    __isStarted: Any
    __waitForKeyOff: Any
    __data: Any
    __model: Any
    @staticmethod
    def clear():
        ...
    def __init__(self, effectsList, keyPoints, excludeTags=None, **args):
        ...
    def play(self, model, startKeyPoint=None, callbackFunc=None, waitForKeyOff=False):
        ...
    def keyOff(self, waitForNextKeyOff=False):
        ...
    def reattachTo(self, model):
        ...
    def __isNeedToPlay(self, waitForKeyOff):
        ...
    def stop(self, keepPosteffects=False, forceCallback=False, forceDelete=False):
        ...
    def __getKeyPointIdx(self, name):
        ...
    def __playKeyPoint(self, waitForKeyOff=False):
        ...

class _EffectDesc(object):
    __slots__: tuple
    startKey: Any
    endKey: Any
    _nodeName: Any
    def __init__(self, dataSection):
        ...
    def prerequisites(self):
        ...
    def reattach(self, elem, model):
        ...
    def create(self, model, effects, args):
        ...
    def delete(self, elem, reason):
        ...

class _PixieEffectDesc(_EffectDesc):
    __slots__: tuple
    TYPE = '_PixieEffectDesc'
    _files: Any
    _force: Any
    _orientByClosestSurfaceNormal: Any
    _alwaysUpdate: Any
    __prototypePixies: Any
    _surfaceMatKinds: Any
    def __init__(self, dataSection):
        ...
    def prerequisites(self):
        ...
    def reattach(self, elem, model):
        ...
    def create(self, model, effects, args):
        ...
    def delete(self, elem, reason):
        ...
    def _callbackAfterLoading(self, pixieBG, elem):
        ...
    def _callbackCreate(self, elem):
        ...

class _AnimationEffectDesc(_EffectDesc):
    __slots__: tuple
    TYPE = '_AnimationEffectDesc'
    _name: Any
    def __init__(self, dataSection):
        ...
    def create(self, model, effects, args):
        ...
    def delete(self, elem, reason):
        ...

class _VisibilityEffectDesc(_EffectDesc):
    __slots__: tuple
    TYPE = '_VisibilityEffectDesc'
    _hasInitial: Any
    _initial: Any
    def __init__(self, dataSection):
        ...
    def create(self, model, effects, args):
        ...
    def delete(self, elem, reason):
        ...

class _ModelEffectDesc(_EffectDesc):
    __slots__: tuple
    TYPE = '_ModelEffectDesc'
    _modelName: Any
    _animation: Any
    def __init__(self, dataSection):
        ...
    def prerequisites(self):
        ...
    def reattach(self, elem, model):
        ...
    def create(self, model, effects, args):
        ...
    def delete(self, elem, reason):
        ...

class _BaseSoundEvent(_EffectDesc):
    __slots__: tuple
    _parameters: Any
    def __init__(self, dataSection):
        ...
    def reattach(self, elem, model):
        ...
    def delete(self, elem, reason):
        ...
    def prerequisites(self):
        ...
    def _isPlayer(self, args):
        ...
    def _getName(self, args):
        ...
    def _register(self, effects, node, sound, args=None):
        ...
    def _makeElem(self, node, sound):
        ...

class _ShotSoundEffectDesc(_BaseSoundEvent):
    __slots__: tuple
    TYPE = '_ShotSoundEffectDesc'
    _soundName: Any
    def __init__(self, dataSection):
        ...
    def create(self, model, effects, args):
        ...

class _NodeSoundEffectDesc(_BaseSoundEvent):
    TYPE = '_NodeSoundEffectDesc'
    effectUniqId = 0
    __slots__: tuple
    _soundName: Any
    _dopplerEffect: Any
    def __init__(self, dataSection):
        ...
    @classmethod
    def nextUniqueID(cls):
        ...
    def create(self, model, effects, args):
        ...

class _TracerSoundEffectDesc(_NodeSoundEffectDesc):
    __slots__: tuple
    TYPE = '_TracerSoundEffectDesc'
    shellTypesMap: dict
    _parameters: Any
    __tracerDelaySound: Any
    def __init__(self, dataSection):
        ...
    def _getName(self, args):
        ...
    def create(self, model, effects, args):
        ...
    def delete(self, elem, reason):
        ...
    def _isPlayer(self, args):
        ...
    def _canCreateSoundObject(self, attackerID):
        ...
    def _register(self, effects, node, sound, args=None):
        ...

class _AutoShootTracerSoundEffectDesc(_TracerSoundEffectDesc):
    __slots__: tuple
    TYPE = '_AutoShootTracerSoundEffectDesc'
    __sessionProvider: Any
    def _canCreateSoundObject(self, attackerID):
        ...

class _CollisionSoundEffectDesc(_BaseSoundEvent):
    __slots__: tuple
    TYPE = '_CollisionSoundEffectDesc'
    _parameters: Any
    _soundName: Any
    def __init__(self, dataSection):
        ...
    def __parceNames(self, events):
        ...
    def _getName(self, args):
        ...
    def create(self, model, effects, args):
        ...

class _CollisionDamageSoundEffectDesc(_BaseSoundEvent):
    TYPE = '_CollisionDamageSoundEffectDesc'
    _soundName: Any
    def __init__(self, dataSection):
        ...
    def create(self, model, effects, args):
        ...

class _DestructionSoundEffectDesc(_BaseSoundEvent):
    TYPE = '_DestructionSoundEffectDesc'
    __slots__: tuple
    _soundName: Any
    _parameters: Any
    def __init__(self, dataSection):
        ...
    def create(self, model, effects, args):
        ...
    def __readParameters(self, dataSection):
        ...

class _LifetimeSoundEffectDesc(_DestructionSoundEffectDesc):
    TYPE = '_LifetimeSoundEffectDesc'

class _SoundEffectDesc(_EffectDesc):
    __slots__: tuple
    TYPE = '_SoundEffectDesc'
    __lobbyContext: Any
    __sessionProvider: Any
    _soundName: Any
    _soundNames: Any
    _switch_impact_surface: Any
    _switch_shell_type: Any
    _stopSyncVisual: Any
    _impactNames: Any
    def __init__(self, dataSection):
        ...
    def reattach(self, elem, model):
        ...
    def create(self, model, effects, args):
        ...
    def delete(self, elem, reason):
        ...
    def prerequisites(self):
        ...
    def __setFriendlyFireRTPC(self, attackerID, sound, soundNames):
        ...

class _DecalEffectDesc(_EffectDesc):
    __slots__: tuple
    TYPE = '_DecalEffectDesc'
    _texName: Any
    _bumpTexName: Any
    _smTexName: Any
    _groupName: Any
    _size: Any
    _randomYaw: Any
    _variation: Any
    def __init__(self, dataSection):
        ...
    def create(self, model, effects, args):
        ...
    def delete(self, elem, reason):
        ...

class _ShockWaveEffectDesc(_EffectDesc):
    __slots__: tuple
    TYPE = '_ShockWaveEffectDesc'
    def __init__(self, dataSection):
        ...

class _PostProcessEffectDesc(_EffectDesc):
    __slots__: tuple
    TYPE = '_PostProcessEffectDesc'
    def prerequisites(self):
        ...
    def create(self, model, effects, args):
        ...
    def delete(self, elem, reason):
        ...

class _FlashBangEffectDesc(_EffectDesc):
    __slots__: tuple
    TYPE = '_FlashBangEffectDesc'
    renderSettings: Any
    __sessionProvider: Any
    _duration: Any
    _keyframes: Any
    __fba: Any
    __clbackId: Any
    def __init__(self, dataSection):
        ...
    def prerequisites(self):
        ...
    def create(self, model, effects, args):
        ...
    @classmethod
    def _isMarkedForPlay(cls, args):
        ...
    def __removeMe(self):
        ...
    def delete(self, elem, reason):
        ...

class _FriendlyFlashBangEffectDesc(_FlashBangEffectDesc):
    TYPE = '_FriendlyFlashBangEffectDesc'
    @classmethod
    def _isMarkedForPlay(cls, args):
        ...

class _StopEmissionEffectDesc(_EffectDesc):
    __slots__: tuple
    TYPE = '_StopEmissionEffectDesc'
    def create(self, model, effects, args):
        ...

class _LightEffectDesc(_EffectDesc):
    __slots__: tuple
    TYPE = '_LightEffectDesc'
    _innerRadius: Any
    _outerRadius: Any
    _castShadows: Any
    _color: Any
    _offset: Any
    _alwaysUpdate: Any
    _colorAnimation: Any
    _multiplierAnimation: Any
    def __init__(self, dataSection):
        ...
    def reattach(self, elem, model):
        ...
    def create(self, model, effects, args):
        ...
    def _callbackCreate(self, elem):
        ...
    def delete(self, elem, reason):
        ...

class _TracerDelaySound(object):
    __slots__: tuple
    __sessionProvider: Any
    _soundName: Any
    __soundDelayBeforeEnd: Any
    def __init__(self, dataSection):
        ...
    def create(self, soundObject, args):
        ...
    def delete(self, state):
        ...
    def __needPlay(self, collisionTime, entityID):
        ...
    def __playSound(self, state, soundName):
        ...
    def __getSoundName(self, entityID):
        ...

class _TracerDelaySoundState(object):
    __slots__: tuple
    soundObject: Any
    soundCallback: Any
    def __init__(self, soundObject=None, soundCallback=None):
        ...

class _NodeWithLocal(object):
    actualNode: Any
    __localMatrix: Any
    __node: Any
    def __init__(self, model, nodeName='', local=None):
        ...
    def attach(self, attachment):
        ...
    def __getattr__(self, item):
        ...

class RespawnDestroyEffect(object):
    @classmethod
    def play(cls, vehicle_id):
        ...
    @classmethod
    def __playDestroyEffect(cls, entity, effects):
        ...

def _isPyModel(model):
    ...
def reload():
    ...
def _getDamageSize(args):
    ...
def _isVehiclePresent(args):
    ...
def _createEffectDesc(eType, dataSection):
    ...
def _raiseWrongConfig(paramName, effectType):
    ...
def __getTransformAlongNormal(localTransform, worldTransform, normal):
    ...
def _getDynCollisionTransformProvider(entityID, componentIDx):
    ...
def _getSurfaceAlignedTransform(model, nodeName, localTransform, precalculatedNormal=None):
    ...
def _findTargetNode(model, nodes, localTransform=None, orientByClosestSurfaceNormal=False, precalculatedNormal=None):
    ...
def _findTargetNodeSafe(model, nodes, local=None):
    ...
def _findTargetModel(model, nodes):
    ...
def _getHitPoint(model, nodeName, args):
    ...
def __keyPointsFromStagesSection(stagesSection):
    ...
def __keyPointsFromTimeLineSection(keyPointSection):
    ...
def effectsFromSection(section):
    ...
