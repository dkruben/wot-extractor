# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/battleground/mines_object.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import Math as Math
import AnimationSequence as AnimationSequence
from Math import Matrix as Matrix
import SoundGroups as SoundGroups
from PlayerEvents import g_playerEvents as g_playerEvents
from gui.battle_control import avatar_getter as avatar_getter
from helpers import dependency as dependency
from battleground.component_loading import loadComponentSystem as loadComponentSystem, Loader as Loader, CompositeLoaderMixin as CompositeLoaderMixin
from battleground.components import TerrainAreaObject as TerrainAreaObject, EffectPlayerObject as EffectPlayerObject, SequenceObject as SequenceObject, SmartSequenceObject as SmartSequenceObject
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from skeletons.dynamic_objects_cache import IBattleDynamicObjectsCache as IBattleDynamicObjectsCache
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_CONFIG_PATH = 'scripts/dynamic_objects.xml'
_idGen: Any

class MinesObject(TerrainAreaObject, CompositeLoaderMixin):
    __spaceID: Any
    __position: Any
    isAllyMine: Any
    __startEffectEnabled: Any
    __isEnemyMarkerEnabled: Any
    __isActivated: Any
    activationTimeDelay: Any
    mineNumber: Any
    id: Any
    __pendingEffects: Any
    startEffectPlayer: Any
    idleEffectPlayer: Any
    destroyEffectPlayer: Any
    blowUpEffectPlayer: Any
    activationEffectPlayer: Any
    decalEffectPlayer: Any
    __soundTimerEventStart: Any
    __soundTimerEventEnd: Any
    __soundTimerObjStart: Any
    __soundTimerObjEnd: Any
    __children: Any
    def __init__(self, isAllyMine, hasActivationDelay, startEffectEnabled=True):
        ...
    def destroy(self):
        ...
    def setPosition(self, position):
        ...
    def setIsEnemyMarkerEnabled(self, value):
        ...
    def setIsActivated(self, value):
        ...
    def setActivationTimeDelay(self, value):
        ...
    def setMineNumber(self, value):
        ...
    def hasActivationEffect(self):
        ...
    def activate(self):
        ...
    def activateMine(self):
        ...
    def deactivate(self):
        ...
    def detonate(self):
        ...
    def enableEnemyIdleEffect(self, isEnabled):
        ...
    def _piecesNum(self):
        ...
    def __getSoundObject(self, name):
        ...
    def __getSoundObjName(self, eventName):
        ...
    def __isFirstMine(self):
        ...
    @property
    def __isAvatarReady(self):
        ...
    def __playStartEffects(self):
        ...
    def __playActivateMineEffects(self):
        ...
    def __playStopEffects(self):
        ...
    def __playIdleEffects(self):
        ...
    def __playDetonateEffects(self):
        ...
    def __playEffectOnAvatarReady(self, effect):
        ...
    def __onAvatarReady(self):
        ...

def _getSequenceResourceMapping(path, spaceId):
    ...
def _getEffectResourceMapping(name):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def loadMines(ownerVehicleID, callback, startEffectEnabled=True, dynamicObjectsCache=None, battleSession=None):
    ...
