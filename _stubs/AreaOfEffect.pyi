# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AreaOfEffect.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import Optional as Optional, List as List
import math as math
import random as random
from functools import partial as partial
from future.utils import viewvalues as viewvalues
from past.builtins import xrange as xrange
import BigWorld as BigWorld
import AnimationSequence as AnimationSequence
import CGF as CGF
import Math as Math
import math_utils as math_utils
import CombatSelectedArea as CombatSelectedArea
from ProjectileMover import collideDynamicAndStatic as collideDynamicAndStatic
from account_helpers.settings_core.settings_constants import GRAPHICS as GRAPHICS
from gui.battle_control import avatar_getter as avatar_getter
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import MarkersManagerEvent as MarkersManagerEvent
from helpers import dependency as dependency
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from items import vehicles as vehicles
from items.artefacts import AoeEffects as AoeEffects, AreaShow as AreaShow, OrderTypes as OrderTypes
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from random_utils import getValueWithDeviationInPercent as getValueWithDeviationInPercent
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class EffectRunner(object):
    SHOT_HEIGHT = 100.0
    RAY_CAST_HEIGHT = 2.0
    MAX_SHOTS = 1000
    GRAVITY = 9.8
    SHELL_VELOCITY: tuple
    _sequences: Any
    _callbacks: Any
    _areas: Any
    _idGen: Any
    salvo: Any
    _entity: Any
    _equipment: Any
    def __init__(self, entity, equipment):
        ...
    @property
    def areaColor(self):
        ...
    def prerequisites(self):
        ...
    def playEffect(self, effectType, position, radius):
        ...
    def _play(self, playID, effect, targetPosition):
        ...

class AreaOfEffect(BigWorld.Entity, EffectRunner):
    MAX_LAG = 0.5
    sessionProvider: Any
    __settingsCore: Any
    _equipment: Any
    __areaGo: Any
    __mainAreaID: Any
    __destroyGoCallback: Any
    _callbacks: Any
    _areas: Any
    _sequences: Any
    def __init__(self):
        ...
    @property
    def areaColor(self):
        ...
    def onEnterWorld(self, prereqs):
        ...
    def onLeaveWorld(self):
        ...
    def _areaDestroy(self, areaID):
        ...
    @property
    def _isMarkersManagerReady(self):
        ...
    def _onMarkersCreated(self, event):
        ...
    @property
    def _adjustedDelay(self):
        ...
    @property
    def _direction(self):
        ...
    def _showArea(self):
        ...
    def _showMarker(self):
        ...
    def _isAttackerEnemy(self):
        ...
    def _isAreaVisible(self):
        ...
    def __onAreaGOLoaded(self, objects, queue):
        ...
    def __destroyAreaGO(self):
        ...
    def __onSettingsChanged(self, diff):
        ...
