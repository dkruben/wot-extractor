# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/ribbons_aggregator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import defaultdict as defaultdict
from future.utils import viewitems as viewitems, viewvalues as viewvalues
import Event as Event
import BattleReplay as BattleReplay
from constants import ROLE_TYPE as ROLE_TYPE
from gui.Scaleform.genConsts.DAMAGE_SOURCE_TYPES import DAMAGE_SOURCE_TYPES as DAMAGE_SOURCE_TYPES
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from gui.Scaleform.genConsts.BATTLE_EFFICIENCY_TYPES import BATTLE_EFFICIENCY_TYPES as BATTLE_EFFICIENCY_TYPES
from BattleFeedbackCommon import BATTLE_EVENT_TYPE as _BET
from gui.battle_control.battle_constants import FEEDBACK_EVENT_ID as FEEDBACK_EVENT_ID, VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE
from gui.battle_control import avatar_getter as avatar_getter
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_logger: Any
_RIBBON_TYPES_AGGREGATED_WITH_KILL_RIBBON: tuple
_RIBBON_TYPES_EXCLUDED_IF_KILL_RIBBON: tuple
_RIBBON_TYPES_EXCLUDED_IN_POSTMORTEM: tuple
_NOT_CACHED_RIBBON_TYPES: tuple
_ACCUMULATED_RIBBON_TYPES: tuple
_FEEDBACK_EVENT_TO_RIBBON_CLS_FACTORY: dict
_FEEDBACK_EVENTS_TO_IGNORE: tuple

class DAMAGE_SOURCE(object):
    PLAYER = 'player'
    ARTILLERY = 'artillery'
    BOMBERS = 'airstrike'
    HIDE = ''

class _Ribbon(object):
    __slots__: tuple
    _id: Any
    _isAggregating: Any
    def __init__(self, ribbonID):
        ...
    @classmethod
    def createFromFeedbackEvent(cls, ribbonID, event):
        ...
    def getFormatter(self):
        ...
    def getType(self):
        ...
    def isRoleBonus(self):
        ...
    def getID(self):
        ...
    def aggregate(self, ribbon):
        ...
    @property
    def isAggregating(self):
        ...
    def _aggregate(self, ribbon):
        ...
    def _canAggregate(self, ribbon):
        ...

class _RoleRibbon(_Ribbon):
    __slots__: tuple
    _isRoleBonus: Any
    _role: Any
    def __init__(self, ribbonID, isRoleBonus, role):
        ...
    @classmethod
    def createFromFeedbackEvent(cls, ribbonID, event):
        ...
    def isRoleBonus(self):
        ...
    def role(self):
        ...

class _BasePointsRibbon(_Ribbon):
    __slots__: tuple
    _points: Any
    def __init__(self, ribbonID, points):
        ...
    @classmethod
    def createFromFeedbackEvent(cls, ribbonID, event):
        ...
    def getPoints(self):
        ...
    def _aggregate(self, ribbon):
        ...

class _PerkRibbon(_Ribbon):
    __slots__: tuple
    __perkID: Any
    def __init__(self, ribbonID, perkID):
        ...
    @classmethod
    def createFromFeedbackEvent(cls, ribbonID, event):
        ...
    def getType(self):
        ...
    def getPerkID(self):
        ...
    def _canAggregate(self, ribbon):
        ...

class _WeatherZoneRibbon(_Ribbon):
    __slots__: tuple
    __weatherZoneID: Any
    _isAggregating: Any
    def __init__(self, ribbonID, weatherZoneID):
        ...
    @classmethod
    def createFromFeedbackEvent(cls, ribbonID, event):
        ...
    def getType(self):
        ...
    def getWeatherZoneID(self):
        ...
    def _canAggregate(self, ribbon):
        ...
    def _aggregate(self, ribbon):
        ...

class _BaseCaptureRibbon(_BasePointsRibbon):
    __slots__: tuple
    _sessionID: Any
    def __init__(self, ribbonID, points, sessionID):
        ...
    @classmethod
    def createFromFeedbackEvent(cls, ribbonID, event):
        ...
    def getType(self):
        ...
    def getSessionID(self):
        ...
    def _canAggregate(self, ribbon):
        ...

class _BaseCaptureBlocked(_BaseCaptureRibbon):
    __slots__: tuple
    def getType(self):
        ...

class _BaseDefenceRibbon(_BasePointsRibbon):
    __slots__: tuple
    def getType(self):
        ...

class _SingleVehicleRibbon(_RoleRibbon):
    __slots__: tuple
    _extraValue: Any
    _targetVehID: Any
    def __init__(self, ribbonID, vehID, isRoleBonus, role, extraValue):
        ...
    @classmethod
    def createFromFeedbackEvent(cls, ribbonID, event):
        ...
    def getExtraValue(self):
        ...
    def setExtraValue(self, value):
        ...
    def getVehicleID(self):
        ...
    @classmethod
    def _extractExtraValue(cls, event):
        ...
    def _canAggregate(self, ribbon):
        ...
    def _aggregate(self, ribbon):
        ...
    def getDamageSource(self):
        ...

class _SingleVehicleDamageRibbon(_SingleVehicleRibbon):
    __slots__: tuple
    @classmethod
    def _extractExtraValue(cls, event):
        ...
    def _canAggregate(self, ribbon):
        ...

class _CriticalHitRibbon(_SingleVehicleRibbon):
    __slots__: tuple
    def getType(self):
        ...
    @classmethod
    def _extractExtraValue(cls, event):
        ...

class _TrackAssistRibbon(_SingleVehicleDamageRibbon):
    __slots__: tuple
    def getType(self):
        ...

class _RadioAssistRibbon(_SingleVehicleDamageRibbon):
    __slots__: tuple
    def getType(self):
        ...

class _EnemyKillRibbon(_SingleVehicleDamageRibbon):
    __slots__: tuple
    @classmethod
    def createFromFeedbackEvent(cls, ribbonID, event):
        ...
    def getType(self):
        ...
    @classmethod
    def _extractExtraValue(cls, event):
        ...
    def _canAggregate(self, ribbon):
        ...

class _BlockedDamageRibbon(_SingleVehicleDamageRibbon):
    __slots__: tuple
    def getType(self):
        ...

class _CausedDamageRibbon(_SingleVehicleDamageRibbon):
    __slots__: tuple
    def getType(self):
        ...

class _FireHitRibbon(_SingleVehicleDamageRibbon):
    __slots__: tuple
    def getType(self):
        ...

class _RamHitRibbon(_SingleVehicleDamageRibbon):
    __slots__: tuple
    def getType(self):
        ...

class _ArtilleryHitRibbon(_SingleVehicleDamageRibbon):
    __slots__: tuple
    def getType(self):
        ...

class _FortArtilleryHitRibbon(_SingleVehicleDamageRibbon):
    __slots__: tuple
    def getType(self):
        ...

class _BombersHitRibbon(_SingleVehicleDamageRibbon):
    __slots__: tuple
    def getType(self):
        ...

class _ArtilleryFireHitRibbon(_SingleVehicleDamageRibbon):
    __slots__: tuple
    def getType(self):
        ...

class _BombersFireHitRibbon(_SingleVehicleDamageRibbon):
    __slots__: tuple
    def getType(self):
        ...

class _WorldCollisionHitRibbon(_SingleVehicleDamageRibbon):
    __slots__: tuple
    def getType(self):
        ...

class _SpawnedBotCausedDamageRibbon(_SingleVehicleDamageRibbon):
    __slots__: tuple
    def getType(self):
        ...

class _MinefieldDamageRibbon(_SingleVehicleDamageRibbon):
    __slots__: tuple
    def getType(self):
        ...

class _AirStrikeDamageRibbon(_SingleVehicleDamageRibbon):
    __slots__: tuple
    def getType(self):
        ...

class _ArtilleryDamageRibbon(_SingleVehicleDamageRibbon):
    __slots__: tuple
    def getType(self):
        ...

class _ReceivedCriticalHitRibbon(_CriticalHitRibbon):
    __slots__: tuple
    def getType(self):
        ...

class _ArtilleryCriticalHitRibbon(_ReceivedCriticalHitRibbon):
    __slots__: tuple
    def getDamageSource(self):
        ...

class _BombersReceivedCriticalHitRibbon(_ReceivedCriticalHitRibbon):
    __slots__: tuple
    def getDamageSource(self):
        ...

class _FortArtilleryReceivedCriticalHitRibbon(_ReceivedCriticalHitRibbon):
    __slots__: tuple
    def getDamageSource(self):
        ...

class _SingleVehicleReceivedHitRibbon(_SingleVehicleRibbon):
    __slots__: tuple
    @classmethod
    def _extractExtraValue(cls, event):
        ...
    def _canAggregate(self, ribbon):
        ...

class _ReceivedDamageHitRibbon(_SingleVehicleReceivedHitRibbon):
    __slots__: tuple
    def getType(self):
        ...

class _ArtilleryReceivedDamageHitRibbon(_ReceivedDamageHitRibbon):
    __slots__: tuple
    def getType(self):
        ...
    def getDamageSource(self):
        ...

class _FortArtilleryReceivedDamageHitRibbon(_ReceivedDamageHitRibbon):
    __slots__: tuple
    def getDamageSource(self):
        ...

class _BombersReceivedDamageHitRibbon(_ReceivedDamageHitRibbon):
    __slots__: tuple
    def getType(self):
        ...
    def getDamageSource(self):
        ...

class _ReceivedFireHitRibbon(_SingleVehicleReceivedHitRibbon):
    __slots__: tuple
    def getType(self):
        ...

class _ReceivedBerserkerHitRibbon(_SingleVehicleReceivedHitRibbon):
    __slots__: tuple
    def getType(self):
        ...

class _ReceivedBySpawnedBotHitRibbon(_SingleVehicleReceivedHitRibbon):
    __slots__: tuple
    def getType(self):
        ...

class _ReceivedByMinefieldRibbon(_SingleVehicleReceivedHitRibbon):
    __slots__: tuple
    def getType(self):
        ...

class _ReceivedByAirStrikeRibbon(_SingleVehicleReceivedHitRibbon):
    __slots__: tuple
    def getType(self):
        ...

class _ReceivedByArtilleryRibbon(_SingleVehicleReceivedHitRibbon):
    __slots__: tuple
    def getType(self):
        ...

class _BombersReceivedFireHitRibbon(_ReceivedFireHitRibbon):
    __slots__: tuple
    def getDamageSource(self):
        ...

class _ArtilleryReceivedFireHitRibbon(_ReceivedFireHitRibbon):
    __slots__: tuple
    def getDamageSource(self):
        ...

class _ReceivedRamHitRibbon(_SingleVehicleReceivedHitRibbon):
    __slots__: tuple
    def getType(self):
        ...

class _ReceivedWorldCollisionHitRibbon(_SingleVehicleReceivedHitRibbon):
    __slots__: tuple
    def getType(self):
        ...

class _StunAssistRibbon(_SingleVehicleDamageRibbon):
    __slots__: tuple
    def getType(self):
        ...

class _MultiTargetsRibbon(_RoleRibbon):
    __slots__: tuple
    _targetsAmount: Any
    def __init__(self, ribbonID, isRoleBonus, role, extraValue):
        ...
    @classmethod
    def _extractExtraValue(cls, event):
        ...
    @classmethod
    def _extractTargetsAmount(cls, _):
        ...
    def getTargetsAmount(self):
        ...
    def _canAggregate(self, ribbon):
        ...
    def _aggregate(self, ribbon):
        ...

class _EnemiesStunRibbon(_MultiTargetsRibbon):
    __slots__: tuple
    @classmethod
    def createFromFeedbackEvent(cls, ribbonID, event):
        ...
    @classmethod
    def _extractTargetsAmount(cls, extraValue):
        ...
    def getType(self):
        ...

class _ReceivedDamageByUnknownSourceRibbon(_RoleRibbon):
    __slots__: tuple
    __extraValue: Any
    def __init__(self, ribbonID, extra):
        ...
    def getDamageSource(self):
        ...
    def setExtraValue(self, value):
        ...
    def getExtraValue(self):
        ...
    @classmethod
    def createFromFeedbackEvent(cls, ribbonID, event):
        ...

class _ReceivedByDamagingSmokeRibbon(_ReceivedDamageByUnknownSourceRibbon):
    __slots__: tuple
    def getType(self):
        ...

class _DealtDamageByCorrodingShot(_SingleVehicleDamageRibbon):
    __slots__: tuple
    def getType(self):
        ...

class _DealtDamageByThunderStrike(_SingleVehicleDamageRibbon):
    __slots__: tuple
    def getType(self):
        ...

class _DealtDamageByFireCircle(_SingleVehicleDamageRibbon):
    __slots__: tuple
    def getType(self):
        ...

class _DealtDamageByClingBrander(_SingleVehicleDamageRibbon):
    __slots__: tuple
    def getType(self):
        ...

class _ReceivedByDamagingCorrodingShotRibbon(_SingleVehicleReceivedHitRibbon):
    __slots__: tuple
    def getType(self):
        ...

class _ReceivedByDamagingThunderStrikeRibbon(_SingleVehicleReceivedHitRibbon):
    __slots__: tuple
    def getType(self):
        ...
    def _aggregate(self, ribbon):
        ...

class _ReceivedByHealthAddedRibbon(_SingleVehicleRibbon):
    __slots__: tuple
    def getType(self):
        ...
    @classmethod
    def _extractExtraValue(cls, event):
        ...

class _ReceivedByFireCircleRibbon(_SingleVehicleReceivedHitRibbon):
    __slots__: tuple
    def getType(self):
        ...
    def _aggregate(self, ribbon):
        ...

class _ReceivedByClingBranderRibbon(_SingleVehicleReceivedHitRibbon):
    __slots__: tuple
    def getType(self):
        ...
    def _aggregate(self, ribbon):
        ...

class _DeathZoneRibbon(_ReceivedDamageByUnknownSourceRibbon):
    __slots__: tuple
    def getType(self):
        ...
    def _aggregate(self, ribbon):
        ...

class _StaticDeathZoneRibbon(_ReceivedDamageByUnknownSourceRibbon):
    __slots__: tuple
    def getType(self):
        ...
    def _aggregate(self, ribbon):
        ...

class _MinefieldZoneRibbon(_ReceivedDamageByUnknownSourceRibbon):
    __slots__: tuple
    def getType(self):
        ...
    def _aggregate(self, ribbon):
        ...

class _BattleshipRibbon(_SingleVehicleDamageRibbon):
    __slots__: tuple
    def getType(self):
        ...
    def _aggregate(self, ribbon):
        ...

class _MultiVehicleRibbon(_MultiTargetsRibbon):
    __slots__: tuple
    _vehicles: Any
    def __init__(self, ribbonID, vehID, isRoleBonus, role, extraValue):
        ...
    @classmethod
    def createFromFeedbackEvent(cls, ribbonID, event):
        ...
    def getVehIDs(self):
        ...
    def getExtraValue(self, vehID):
        ...
    def getTotalExtraValue(self):
        ...
    def _canAggregate(self, ribbon):
        ...
    def _aggregate(self, ribbon):
        ...

class _EnemyDetectionRibbon(_MultiVehicleRibbon):
    __slots__: tuple
    @classmethod
    def _extractExtraValue(cls, _):
        ...
    @classmethod
    def _extractTargetsAmount(cls, _):
        ...
    def getType(self):
        ...

class _ReceivedFireDamageZoneRibbon(_SingleVehicleReceivedHitRibbon):
    __slots__: tuple
    def getType(self):
        ...
    def getDamageSource(self):
        ...

class _HERocketDamageRibbon(_SingleVehicleDamageRibbon):
    def getType(self):
        ...

class _ReceivedHERocketDamageRibbon(_SingleVehicleDamageRibbon):
    def getType(self):
        ...

class _RibbonClassFactory(object):
    __slots__: tuple
    def getRibbonClass(self, event):
        ...

class _RibbonSingleClassFactory(_RibbonClassFactory):
    __slots__: tuple
    __cls: Any
    def __init__(self, ribbonCls):
        ...
    def getRibbonClass(self, event):
        ...

class _CriticalRibbonClassFactory(_RibbonClassFactory):
    def getRibbonClass(self, event):
        ...

class _DamageRibbonClassFactory(_RibbonClassFactory):
    __slots__: tuple
    __damageCls: Any
    __fireCls: Any
    __ramCls: Any
    __wcCls: Any
    __artDmgCls: Any
    __artFireCls: Any
    __bombDmgCls: Any
    __bombFireCls: Any
    __recoveryCls: Any
    __deathZoneCls: Any
    __berserker: Any
    __spawnedBotDmgCls: Any
    __damageByMinefield: Any
    __damagedBySmoke: Any
    __damagedByCorrodingShot: Any
    __dmgByFireCircle: Any
    __dmgByClingBrander: Any
    __damageByThunderStrike: Any
    __damagedByFortArtillery: Any
    __damageByAirStrike: Any
    __damageByArtillery: Any
    __staticDeathZoneCls: Any
    __minefieldZoneCls: Any
    __damagedByBattleshipCls: Any
    __damagedByDestroyerCls: Any
    __fireDamageZoneCls: Any
    __heRocketDamageCls: Any
    def __init__(self, damageCls, fireCls, ramCls, wcCls, artDmgCls, bombDmgCls, artFireCls, bombFireCls, deathZoneCls, recoveryCls, berserker, spawnedBotDmgCls, minefieldDamageCls, damagedBySmoke, dmgByCorrodingShot, dmgByFireCircle, dmgByClingBrander, dmgByThunderStrike, damagedByFortArtillery, airStrikeDamageCls, artilleryDamageCls, staticDeathZoneCls, minefieldZoneCls, damagedByBattleshipCls, damagedByDestroyerCls, fireDamageZoneCls, heRocketDamageCls):
        ...
    def getRibbonClass(self, event):
        ...

class _AssistRibbonClassFactory(_RibbonClassFactory):
    __slots__: tuple
    __trackAssistCls: Any
    __radioAssistCls: Any
    __stunAssistCls: Any
    def __init__(self, trackAssistCls, radioAssistCls, stunAssistCls):
        ...
    def getRibbonClass(self, event):
        ...

class _EpicBaseRibbon(_Ribbon):
    __slots__: tuple
    @classmethod
    def createFromFeedbackEvent(cls, ribbonID, event):
        ...
    def getExtraValue(self):
        ...

class _EpicRecoveryRibbon(_EpicBaseRibbon):
    __slots__: tuple
    __extraValue: Any
    def __init__(self, ribbonID, extraValue):
        ...
    @classmethod
    def createFromFeedbackEvent(cls, ribbonID, event):
        ...
    def getType(self):
        ...
    def getExtraValue(self):
        ...

class _EpicEnemySectorCapturedRibbon(_EpicBaseRibbon):
    __slots__: tuple
    def getType(self):
        ...

class _EpicDestructibleDestroyed(_EpicBaseRibbon):
    __slots__: tuple
    __extraValue: Any
    def __init__(self, ribbonID, extraValue):
        ...
    def getType(self):
        ...
    @classmethod
    def createFromFeedbackEvent(cls, ribbonID, event):
        ...
    def getExtraValue(self):
        ...

class _EpicDestructiblesDefended(_EpicBaseRibbon):
    __slots__: tuple
    __extraValue: Any
    def __init__(self, ribbonID, extraValue):
        ...
    @classmethod
    def createFromFeedbackEvent(cls, ribbonID, event):
        ...
    def getType(self):
        ...
    def getExtraValue(self):
        ...

class _EpicDefenderBonus(_EpicBaseRibbon):
    __slots__: tuple
    def getType(self):
        ...

class _EpicAbilityAssist(_SingleVehicleReceivedHitRibbon):
    __slots__: tuple
    @classmethod
    def createFromFeedbackEvent(cls, ribbonID, event):
        ...
    def getType(self):
        ...

class _EpicDestructibleDamaged(_Ribbon):
    __slots__: tuple
    _damagePoints: Any
    def __init__(self, ribbonID, extra):
        ...
    @classmethod
    def createFromFeedbackEvent(cls, ribbonID, event):
        ...
    def getType(self):
        ...
    def getExtraValue(self):
        ...
    def _canAggregate(self, ribbon):
        ...
    def _aggregate(self, ribbon):
        ...

class ATTACK_REASON(object):
    SHOT = 'shot'
    FIRE = 'fire'
    RAM = 'ramming'
    WORLD_COLLISION = 'world_collision'
    DEATH_ZONE = 'death_zone'
    DROWNING = 'drowning'
    OVERTURN = 'overturn'
    ARTILLERY_PROTECTION = 'artillery_protection'
    ARTILLERY_SECTOR = 'artillery_sector'
    BOMBERS = 'bombers'
    RECOVERY = 'recovery'

class _RibbonsCache(object):
    __slots__: tuple
    __ribbons: Any
    __typeToIDs: Any
    def __init__(self):
        ...
    def clear(self):
        ...
    def get(self, ribbonID, default):
        ...
    def pop(self, ribbonID):
        ...
    def add(self, ribbon):
        ...
    def iterByType(self, ribbonType):
        ...
    def __contains__(self, ribbonID):
        ...
    def __iter__(self):
        ...
    def __len__(self):
        ...
    def __getitem__(self, index):
        ...
    def __setitem__(self, ribbonID, ribbon):
        ...

class RibbonsAggregator(object):
    sessionProvider: Any
    FEEDBACK_EVENT_TO_RIBBON_CLS_FACTORY = _FEEDBACK_EVENT_TO_RIBBON_CLS_FACTORY
    FEEDBACK_EVENTS_TO_IGNORE = _FEEDBACK_EVENTS_TO_IGNORE
    KILL_RIBBON_BATTLE_EFFICIENCY_TYPE = BATTLE_EFFICIENCY_TYPES.DESTRUCTION
    RIBBON_TYPES_AGGREGATED_WITH_KILL_RIBBON = _RIBBON_TYPES_AGGREGATED_WITH_KILL_RIBBON
    __feedbackProvider: Any
    __vehicleStateCtrl: Any
    __perksCtrl: Any
    __cache: Any
    __accumulatedRibbons: Any
    __rules: Any
    __idGenerator: Any
    onRibbonAdded: Any
    onRibbonUpdated: Any
    __isStarted: Any
    __isSuspended: Any
    __isInPostmortemMode: Any
    def __init__(self):
        ...
    def start(self):
        ...
    def suspend(self):
        ...
    def resume(self):
        ...
    def stop(self):
        ...
    def getRibbon(self, ribbonID):
        ...
    def resetRibbonData(self, ribbonID):
        ...
    def clearRibbonsData(self):
        ...
    def _onPostMortemSwitched(self, noRespawnPossible, respawnAvailable):
        ...
    def __onRespawnBaseMoving(self):
        ...
    def _onPerksChanged(self, perkData):
        ...
    def _onVehicleStateUpdated(self, state, value):
        ...
    def _onPlayerFeedbackReceived(self, events):
        ...
    def _aggregateRibbons(self, ribbons):
        ...
    def __filterRibbons(self, ribbons):
        ...
    def __getSortedList(self, ribbons):
        ...

class RibbonsAggregatorPlayer(RibbonsAggregator):
    def _onPlayerFeedbackReceived(self, events):
        ...
    def _aggregateRibbons(self, ribbons):
        ...

def _isRoleBonus(event):
    ...
def _createRibbonFromPlayerFeedbackEvent(aggregator, ribbonID, event):
    ...
def createRibbonsAggregator():
    ...
