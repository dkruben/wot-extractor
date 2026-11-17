# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/visual_script_client/arena_blocks.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
from future.utils import lmap as lmap
from typing import List as List
import BigWorld as BigWorld
import Math as Math
from ArenaType import g_cache as g_cache
from constants import IS_VS_EDITOR as IS_VS_EDITOR, ARENA_PERIOD as ARENA_PERIOD, ARENA_PERIOD_NAMES as ARENA_PERIOD_NAMES, CollisionFlags as CollisionFlags, TEAMS_IN_ARENA as TEAMS_IN_ARENA
from visual_script.block import Block as Block, InitParam as InitParam
from visual_script.dependency import dependencyImporter as dependencyImporter
from visual_script.misc import ASPECT as ASPECT, errorVScript as errorVScript
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE, arrayOf as arrayOf
from visual_script.arena_blocks import ArenaMeta as ArenaMeta, GetUDOByNameBase as GetUDOByNameBase, GetDataFromStorageBase as GetDataFromStorageBase
from visual_script.tunable_event_block import TunableEventBlock as TunableEventBlock
from PlayerEvents import g_playerEvents as g_playerEvents
helpers: Any
clientArena: Any
dependency: Any
battle_session: Any

class ClientArena(Block, ArenaMeta):
    _arena: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execArena(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class GetControlPoint(Block, ArenaMeta):
    _CACHE: dict
    _team: Any
    _baseID: Any
    _value: Any
    team: Any
    baseID: Any
    class TeamBase(object):
        team: Any
        baseID: Any
        def __init__(self, team, baseID):
            ...
    def __init__(self, *args, **kwargs):
        ...
    def _execValue(self):
        ...
    @classmethod
    def blockIcon(cls):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class GetActiveControlPoints(Block, ArenaMeta):
    TeamBase = GetControlPoint.TeamBase
    _CACHE: dict
    _team: Any
    _value: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execValue(self):
        ...
    @classmethod
    def blockIcon(cls):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class OnCaptureControlPoint(TunableEventBlock, ArenaMeta):
    _EVENT_SLOT_NAMES: list
    _points: Any
    _invadersCount: Any
    _controlPoint: Any
    _index: Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def blockIcon(cls):
        ...
    def onStartScript(self):
        ...
    def onFinishScript(self):
        ...
    @property
    def arena(self):
        ...
    def _isCurrControlPoint(self, baseID, team):
        ...
    def _capturingInfoUpdate(self, team, baseID, lastData, currData):
        ...
    def _onCaptured(self, team, baseID):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def _callUpdated(self):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def _callStopped(self):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def _callStarted(self):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def _callCompleted(self):
        ...
    def _getPoints(self):
        ...
    def _getInvadersCount(self):
        ...
    def validate(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class ArenaPeriod(Block, ArenaMeta):
    _isPeriodActive: Any
    _timeFromStartSlot: Any
    _timeToEndSlot: Any
    _periodType: Any
    class PlayerArenaDummy(object):
        period = None
    def __init__(self, *args, **kwargs):
        ...
    @property
    def _arena(self):
        ...
    def _execIsStart(self):
        ...
    def _execTimeFromStart(self):
        ...
    def _execTimeToEnd(self):
        ...
    @classmethod
    def blockIcon(cls):
        ...
    def captionText(self):
        ...
    @classmethod
    def initParams(cls):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class ArenaPeriodStartEvent(Block, ArenaMeta):
    _start: Any
    _update: Any
    _timeToEndSlot: Any
    _periodType: Any
    __periodTypeLast: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def _arena(self):
        ...
    @classmethod
    def blockIcon(cls):
        ...
    def captionText(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...
    @classmethod
    def initParams(cls):
        ...
    def onStartScript(self):
        ...
    def onFinishScript(self):
        ...
    def _execTimeToEnd(self):
        ...
    def __subscribe(self):
        ...
    def __unsubscribe(self):
        ...
    def __onPeriodChange(self, period, periodEndTime, periodLength, *args):
        ...

class OnBattleRoundFinished(Block, ArenaMeta):
    _out: Any
    _winner: Any
    _reason: Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def blockIcon(cls):
        ...
    def onStartScript(self):
        ...
    def onFinishScript(self):
        ...
    def _onRoundFinished(self, winnerTeam, reason):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class GetUDOByName(GetUDOByNameBase):
    _UDOTypes: list
    @classmethod
    def blockAspects(cls):
        ...
    def _getUDOsOfType(self, typeName):
        ...

class GetArenaBorders(Block, ArenaMeta):
    _min: Any
    _max: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def _arena(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class GetVehicles(Block, ArenaMeta):
    _team: Any
    _excludePlayer: Any
    _excludeDestroyed: Any
    _vehicles: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self):
        ...
    def validate(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class GetDataFromStorage(GetDataFromStorageBase):
    arena: Any
    @classmethod
    def blockAspects(cls):
        ...
    def _exec(self):
        ...

class CollideSegment(Block, ArenaMeta):
    _in: Any
    _out: Any
    _spaceID: Any
    _from: Any
    _to: Any
    _hitFlags: Any
    _collision: Any
    _collidePosition: Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def blockAspects(cls):
        ...
    def _collide(self):
        ...

class GetControlPointPosition(Block, ArenaMeta):
    DELTA_Y = 500.0
    _controlPoint: Any
    _position: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execValue(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...
    @classmethod
    def blockIcon(cls):
        ...

class SetEnvironment(Block, ArenaMeta):
    _in: Any
    _name: Any
    _out: Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def blockAspects(cls):
        ...
    def _execute(self):
        ...
