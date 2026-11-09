# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/ribbons_aggregator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import BattleReplay as BattleReplay
from halloween_common.hw_battle_feedback import HWGameplayActionID as HWGameplayActionID
from halloween_common.hw_battle_feedback import unpackGameplayActionFeedback as unpackGameplayActionFeedback
from gui.Scaleform.daapi.view.battle.shared.ribbons_aggregator import RibbonsAggregator as RibbonsAggregator, _RibbonClassFactory as _RibbonClassFactory, _ACCUMULATED_RIBBON_TYPES as _ACCUMULATED_RIBBON_TYPES, _FEEDBACK_EVENTS_TO_IGNORE as _DEFAULT_EVENTS_TO_IGNORE, _FEEDBACK_EVENT_TO_RIBBON_CLS_FACTORY as _DEFAULT_RIBBON_FACTORIES, _CausedDamageRibbon as _CausedDamageRibbon, _RIBBON_TYPES_AGGREGATED_WITH_KILL_RIBBON as _DEFAULT_RIBBONS_AGGREGATED_WITH_KILL, DAMAGE_SOURCE as DAMAGE_SOURCE, _Ribbon as _Ribbon, _SingleVehicleReceivedHitRibbon as _SingleVehicleReceivedHitRibbon, _AssistRibbonClassFactory as _AssistRibbonClassFactory, _RadioAssistRibbon as _RadioAssistRibbon, _TrackAssistRibbon as _TrackAssistRibbon, _StunAssistRibbon as _StunAssistRibbon, _EnemyKillRibbon as _EnemyKillRibbon, _RIBBON_TYPES_EXCLUDED_IF_KILL_RIBBON as _RIBBON_TYPES_EXCLUDED_IF_KILL_RIBBON
from gui.Scaleform.daapi.view.battle.shared.ribbons_panel import _singleVehRibbonFormatter as _singleVehRibbonFormatter, _getVehicleData as _getVehicleData
from halloween.gui.halloween_gui_constants import FEEDBACK_EVENT_ID as FEEDBACK_EVENT_ID
from halloween_common.halloween_constants import ATTACK_REASON as ATTACK_REASON, BATTLE_EVENT_TYPE as BATTLE_EVENT_TYPE
from halloween.gui.scaleform.genConsts.HW_BATTLE_EFFICIENCY_TYPES import HW_BATTLE_EFFICIENCY_TYPES as HW_BATTLE_EFFICIENCY_TYPES
from gui.Scaleform.genConsts.BATTLE_EFFICIENCY_TYPES import BATTLE_EFFICIENCY_TYPES as BATTLE_EFFICIENCY_TYPES
from gui.battle_control.controllers.feedback_events import _BATTLE_EVENT_TO_PLAYER_FEEDBACK_EVENT as _BATTLE_EVENT_TO_PLAYER_FEEDBACK_EVENT, _PLAYER_FEEDBACK_EXTRA_DATA_CONVERTERS as _PLAYER_FEEDBACK_EXTRA_DATA_CONVERTERS
from gui.impl import backport as backport
from gui.impl.gen import R as R
_HW_FEEDBACK_EVENT_TO_RIBBON_CLS_FACTORY: dict
_HW_FEEDBACK_EVENTS_TO_IGNORE: Any
_HW_RIBBON_TYPES_AGGREGATED_WITH_KILL_RIBBON: list
_HW_RIBBON_TYPES_COPY_TO: dict
_HW_EXCLUDED_RIBBONS: dict

class _HWGameplayActionRibbon(_Ribbon):
    __slots__: tuple
    BATTLE_EFFICIENCY_TYPE = None
    _vehicleID: Any
    _actionValue: Any
    _actionID: Any
    _effType: Any
    _isPlayerVehicle: Any
    def __init__(self, ribbonID, actionCtx):
        ...
    @classmethod
    def createFromFeedbackEvent(cls, ribbonID, event):
        ...
    @property
    def actionValue(self):
        ...
    @property
    def actionID(self):
        ...
    @property
    def vehicleID(self):
        ...
    @property
    def isShowActionSource(self):
        ...
    def getFormatter(self):
        ...
    def getType(self):
        ...
    def _canAggregate(self, ribbon):
        ...
    def _aggregate(self, ribbon):
        ...

class _HWCausedDamageRibbon(_CausedDamageRibbon):
    __slots__: tuple
    BATTLE_EFFICIENCY_TYPE = None
    def getType(self):
        ...
    def getFormatter(self):
        ...

class _HWCausedAoeAbilityDamage(_HWCausedDamageRibbon):
    __slots__: tuple
    BATTLE_EFFICIENCY_TYPE = None
    def getDamageSource(self):
        ...
    def _canAggregate(self, ribbon):
        ...

class _HWEnemyKillRibbon(_EnemyKillRibbon):
    __slots__: tuple
    BATTLE_EFFICIENCY_TYPE = None
    def getType(self):
        ...
    @property
    def isShowActionSource(self):
        ...
    @property
    def vehicleID(self):
        ...

class _HWAbstractDamageRibbonsFactory(_RibbonClassFactory):
    ATTACK_REASONS = None
    def getRibbonClass(self, event):
        ...
    @classmethod
    def registerAttackReasonRibbon(cls, reason, secondaryReason=None):
        ...
    @classmethod
    def _getHWRibbonClass(cls, reasonID, secondaryReasonID):
        ...

# decorador original: @registerRibbonsFactory(...)
class HWDamageRibbonsFactory(_HWAbstractDamageRibbonsFactory):
    ATTACK_REASONS: dict
    _DEFAULT_FACTORY: Any

# decorador original: @registerRibbonsFactory(...)
class HWReceiveDamageRibbonsFactory(_HWAbstractDamageRibbonsFactory):
    ATTACK_REASONS: dict
    _DEFAULT_FACTORY: Any

# decorador original: @registerRibbonsFactory(...)
class HWGameplayActionRibbonsFactory(_RibbonClassFactory):
    GAMEPLAY_ACTIONS: dict
    def getRibbonClass(self, event):
        ...
    @classmethod
    def registerActionRibbon(cls, reason):
        ...
    @classmethod
    def _getHWRibbonClass(cls, key):
        ...

# decorador original: @hwCopyTo(...)
# decorador original: @HWDamageRibbonsFactory.registerAttackReasonRibbon(...)
class _HWCausedVampiricDamageRibbon(_HWCausedAoeAbilityDamage):
    __slots__: tuple
    BATTLE_EFFICIENCY_TYPE = HW_BATTLE_EFFICIENCY_TYPES.HALLOWEEN_DMG_VAMPIRE

# decorador original: @hwCopyTo(...)
# decorador original: @HWDamageRibbonsFactory.registerAttackReasonRibbon(...)
class _HWCausedAoeDamageRibbon(_HWCausedAoeAbilityDamage):
    __slots__: tuple
    BATTLE_EFFICIENCY_TYPE = HW_BATTLE_EFFICIENCY_TYPES.HALLOWEEN_AOE_DAMAGE

# decorador original: @hwCopyTo(...)
# decorador original: @HWDamageRibbonsFactory.registerAttackReasonRibbon(...)
class _HWCausedAoeDamageInstantShotRibbon(_HWCausedAoeAbilityDamage):
    __slots__: tuple
    BATTLE_EFFICIENCY_TYPE = HW_BATTLE_EFFICIENCY_TYPES.HALLOWEEN_SHOT_AOE_DAMAGE

# decorador original: @hwCopyTo(...)
# decorador original: @HWDamageRibbonsFactory.registerAttackReasonRibbon(...)
class _HWCausedAoeDrainEnemyHpInstantShotDamageRibbon(_HWCausedAoeAbilityDamage):
    __slots__: tuple
    BATTLE_EFFICIENCY_TYPE = HW_BATTLE_EFFICIENCY_TYPES.HALLOWEEN_SHOT_AOE_DRAIN_ENEMY_HP

# decorador original: @hwCopyTo(...)
# decorador original: @HWDamageRibbonsFactory.registerAttackReasonRibbon(...)
class _HWCausedAoeStunInstantShotRibbon(_HWCausedAoeAbilityDamage):
    __slots__: tuple
    BATTLE_EFFICIENCY_TYPE = HW_BATTLE_EFFICIENCY_TYPES.HALLOWEEN_SHOT_AOE_STUN

# decorador original: @hwCopyTo(...)
# decorador original: @HWDamageRibbonsFactory.registerAttackReasonRibbon(...)
class _HWAoeFireDamageRibbon(_HWCausedAoeAbilityDamage):
    __slots__: tuple
    BATTLE_EFFICIENCY_TYPE = HW_BATTLE_EFFICIENCY_TYPES.HALLOWEEN_AOE_BURN

# decorador original: @HWDamageRibbonsFactory.registerAttackReasonRibbon(...)
class _HWPassiveFireDamageRibbon(_SingleVehicleReceivedHitRibbon):
    __slots__: tuple
    TYPE = HW_BATTLE_EFFICIENCY_TYPES.HALLOWEEN_PASSIVE_IGNITE
    def getType(self):
        ...
    def getFormatter(self):
        ...

# decorador original: @HWReceiveDamageRibbonsFactory.registerAttackReasonRibbon(...)
class _ReceivedBossAuraHitRibbon(_SingleVehicleReceivedHitRibbon):
    __slots__: tuple
    TYPE = HW_BATTLE_EFFICIENCY_TYPES.HALLOWEEN_AOE_BOSS_BURN
    def getType(self):
        ...
    def getFormatter(self):
        ...

# decorador original: @HWReceiveDamageRibbonsFactory.registerAttackReasonRibbon(...)
class _HWReceivedBomberExplosionHitRibbon(_SingleVehicleReceivedHitRibbon):
    __slots__: tuple
    TYPE = HW_BATTLE_EFFICIENCY_TYPES.HALLOWEEN_BOMBER_EXPLOSION
    def getType(self):
        ...
    def getFormatter(self):
        ...

# decorador original: @HWReceiveDamageRibbonsFactory.registerAttackReasonRibbon(...)
class _ReceivedVampireAbilityRibbon(_SingleVehicleReceivedHitRibbon):
    __slots__: tuple
    TYPE = HW_BATTLE_EFFICIENCY_TYPES.HALLOWEEN_DMG_VAMPIRE_RECEIVED
    def getType(self):
        ...
    def getFormatter(self):
        ...

# decorador original: @HWReceiveDamageRibbonsFactory.registerAttackReasonRibbon(...)
class _ReceivedAOEDamageAbilityHitRibbon(_SingleVehicleReceivedHitRibbon):
    __slots__: tuple
    TYPE = HW_BATTLE_EFFICIENCY_TYPES.HALLOWEEN_AOE_DAMAGE_RECEIVED
    def getType(self):
        ...
    def getFormatter(self):
        ...

# decorador original: @HWReceiveDamageRibbonsFactory.registerAttackReasonRibbon(...)
class _HWDeathZoneIgniteDamageRibbon(_SingleVehicleReceivedHitRibbon):
    __slots__: tuple
    TYPE = HW_BATTLE_EFFICIENCY_TYPES.HALLOWEEN_IGNITE_DAMAGE_RECEIVED
    def getType(self):
        ...
    def getFormatter(self):
        ...

# decorador original: @HWReceiveDamageRibbonsFactory.registerAttackReasonRibbon(...)
class _HWDeathZoneSingleIgniteDamageRibbon(_HWDeathZoneIgniteDamageRibbon):
    ...

# decorador original: @HWReceiveDamageRibbonsFactory.registerAttackReasonRibbon(...)
class _HWDeathZoneStunDamageRibbon(_SingleVehicleReceivedHitRibbon):
    __slots__: tuple
    TYPE = HW_BATTLE_EFFICIENCY_TYPES.HALLOWEEN_STUN_DAMAGE_RECEIVED
    def getType(self):
        ...
    def getFormatter(self):
        ...

# decorador original: @HWReceiveDamageRibbonsFactory.registerAttackReasonRibbon(...)
class _HWDeathZoneIntervalDamageRibbon(_SingleVehicleReceivedHitRibbon):
    __slots__: tuple
    TYPE = HW_BATTLE_EFFICIENCY_TYPES.HALLOWEEN_DAMAGE_OVERTIME_RECEIVED
    def getType(self):
        ...
    def getDamageSource(self):
        ...
    def getFormatter(self):
        ...

# decorador original: @HWReceiveDamageRibbonsFactory.registerAttackReasonRibbon(...)
class _HWStaticDeathZoneRibbon(_SingleVehicleReceivedHitRibbon):
    __slots__: tuple
    TYPE = BATTLE_EFFICIENCY_TYPES.STATIC_DEATH_ZONE
    def getType(self):
        ...
    def getDamageSource(self):
        ...
    def getFormatter(self):
        ...

# decorador original: @HWReceiveDamageRibbonsFactory.registerAttackReasonRibbon(...)
class _HWCorrosionDamageRibbon(_SingleVehicleReceivedHitRibbon):
    __slots__: tuple
    TYPE = HW_BATTLE_EFFICIENCY_TYPES.HALLOWEEN_CORROSION_DAMAGE
    def getType(self):
        ...
    def getDamageSource(self):
        ...
    def getFormatter(self):
        ...

# decorador original: @HWReceiveDamageRibbonsFactory.registerAttackReasonRibbon(...)
class _HWStompingDamageRibbon(_SingleVehicleReceivedHitRibbon):
    __slots__: tuple
    TYPE = HW_BATTLE_EFFICIENCY_TYPES.HALLOWEEN_STOMPING_DAMAGE
    def getType(self):
        ...
    def getFormatter(self):
        ...

# decorador original: @HWGameplayActionRibbonsFactory.registerActionRibbon(...)
class _HWIncomingRepairRibbon(_HWGameplayActionRibbon):
    BATTLE_EFFICIENCY_TYPE = HW_BATTLE_EFFICIENCY_TYPES.HALLOWEEN_REPAIR
    @property
    def healerID(self):
        ...
    @property
    def isSelfHeal(self):
        ...
    def getType(self):
        ...
    def _canAggregate(self, ribbon):
        ...

# decorador original: @HWGameplayActionRibbonsFactory.registerActionRibbon(...)
class _HWOutcomingRepairRibbon(_HWGameplayActionRibbon):
    BATTLE_EFFICIENCY_TYPE = HW_BATTLE_EFFICIENCY_TYPES.HALLOWEEN_REPAIR_OTHER
    @property
    def isShowActionSource(self):
        ...
    def _canAggregate(self, ribbon):
        ...

# decorador original: @HWGameplayActionRibbonsFactory.registerActionRibbon(...)
class _HWModulesDamageBlockedRibbon(_HWGameplayActionRibbon):
    BATTLE_EFFICIENCY_TYPE = HW_BATTLE_EFFICIENCY_TYPES.HALLOWEEN_MODULES_DAMAGE_BLOCKED
    _actionValue: Any
    @property
    def isShowActionSource(self):
        ...
    def getFormatter(self):
        ...
    def _canAggregate(self, ribbon):
        ...
    def _aggregate(self, ribbon):
        ...

# decorador original: @HWGameplayActionRibbonsFactory.registerActionRibbon(...)
class _HWHealthDrainedByPassiveVampireRibbon(_HWGameplayActionRibbon):
    BATTLE_EFFICIENCY_TYPE = HW_BATTLE_EFFICIENCY_TYPES.HALLOWEEN_PASSIVE_VAMPIRE
    @property
    def isShowActionSource(self):
        ...
    def _canAggregate(self, ribbon):
        ...

# decorador original: @HWGameplayActionRibbonsFactory.registerActionRibbon(...)
class _HWShellsPickupRibbon(_HWGameplayActionRibbon):
    BATTLE_EFFICIENCY_TYPE = HW_BATTLE_EFFICIENCY_TYPES.HALLOWEEN_SHELLS_PICKUP
    @property
    def isShowActionSource(self):
        ...
    def getFormatter(self):
        ...
    def _canAggregate(self, ribbon):
        ...

# decorador original: @HWGameplayActionRibbonsFactory.registerActionRibbon(...)
class _HWShellsReceiveRibbon(_HWGameplayActionRibbon):
    BATTLE_EFFICIENCY_TYPE = HW_BATTLE_EFFICIENCY_TYPES.HALLOWEEN_SHELLS_RECEIVE
    @property
    def isShowActionSource(self):
        ...
    def getFormatter(self):
        ...
    def _canAggregate(self, ribbon):
        ...

# decorador original: @HWGameplayActionRibbonsFactory.registerActionRibbon(...)
class _HWSoulsPickupRibbon(_HWGameplayActionRibbon):
    BATTLE_EFFICIENCY_TYPE = HW_BATTLE_EFFICIENCY_TYPES.HALLOWEEN_SOULS_PICKUP
    @property
    def isShowActionSource(self):
        ...
    def getFormatter(self):
        ...
    def _canAggregate(self, ribbon):
        ...

# decorador original: @HWGameplayActionRibbonsFactory.registerActionRibbon(...)
class _HWSoulsMiriumizationAddedRibbon(_HWSoulsPickupRibbon):
    ...

# decorador original: @HWGameplayActionRibbonsFactory.registerActionRibbon(...)
class _HWSoulsMiriumizationDecreasedRibbon(_HWSoulsPickupRibbon):
    BATTLE_EFFICIENCY_TYPE = HW_BATTLE_EFFICIENCY_TYPES.HALLOWEEN_SOULS_DRAINED
    def getFormatter(self):
        ...

# decorador original: @HWGameplayActionRibbonsFactory.registerActionRibbon(...)
class _HWSoulsReceiveRibbon(_HWGameplayActionRibbon):
    BATTLE_EFFICIENCY_TYPE = HW_BATTLE_EFFICIENCY_TYPES.HALLOWEEN_SOULS_RECEIVE
    @property
    def isShowActionSource(self):
        ...
    def getFormatter(self):
        ...
    def _canAggregate(self, ribbon):
        ...

# decorador original: @HWGameplayActionRibbonsFactory.registerActionRibbon(...)
class _HWSoulsRefundRibbon(_HWGameplayActionRibbon):
    BATTLE_EFFICIENCY_TYPE = HW_BATTLE_EFFICIENCY_TYPES.HALLOWEEN_SOULS_REFUND
    @property
    def isShowActionSource(self):
        ...
    def getFormatter(self):
        ...
    def _canAggregate(self, ribbon):
        ...

# decorador original: @HWGameplayActionRibbonsFactory.registerActionRibbon(...)
class _HWHangarItemPickupRibbon(_HWGameplayActionRibbon):
    BATTLE_EFFICIENCY_TYPE = HW_BATTLE_EFFICIENCY_TYPES.HALLOWEEN_HANGAR_ITEMS_PICKUP
    @property
    def isShowActionSource(self):
        ...
    def getFormatter(self):
        ...
    def _canAggregate(self, ribbon):
        ...

# decorador original: @HWGameplayActionRibbonsFactory.registerActionRibbon(...)
class _HWHangarItemReceiveRibbon(_HWHangarItemPickupRibbon):
    BATTLE_EFFICIENCY_TYPE = HW_BATTLE_EFFICIENCY_TYPES.HALLOWEEN_HANGAR_ITEMS_RECEIVE
    @property
    def isShowActionSource(self):
        ...

# decorador original: @HWGameplayActionRibbonsFactory.registerActionRibbon(...)
class _HWAnomalyPickupRibbon(_HWGameplayActionRibbon):
    BATTLE_EFFICIENCY_TYPE = HW_BATTLE_EFFICIENCY_TYPES.HALLOWEEN_ANOMALY_PICKUP
    @property
    def isShowActionSource(self):
        ...
    def getFormatter(self):
        ...
    def _canAggregate(self, ribbon):
        ...

# decorador original: @HWGameplayActionRibbonsFactory.registerActionRibbon(...)
class _HWAnomalyReceiveRibbon(_HWAnomalyPickupRibbon):
    BATTLE_EFFICIENCY_TYPE = HW_BATTLE_EFFICIENCY_TYPES.HALLOWEEN_ANOMALY_RECEIVE
    @property
    def isShowActionSource(self):
        ...

# decorador original: @HWGameplayActionRibbonsFactory.registerActionRibbon(...)
class _HWBomberResistRibbon(_HWGameplayActionRibbon):
    BATTLE_EFFICIENCY_TYPE = HW_BATTLE_EFFICIENCY_TYPES.HALLOWEEN_BOMBER_RESIST
    @property
    def isShowActionSource(self):
        ...
    def getFormatter(self):
        ...

# decorador original: @hwExcludeRibbons(...)
# decorador original: @HWDamageRibbonsFactory.registerAttackReasonRibbon(...)
class _HWInstantKillRibbon(_HWEnemyKillRibbon):
    __slots__: tuple
    BATTLE_EFFICIENCY_TYPE = HW_BATTLE_EFFICIENCY_TYPES.HALLOWEEN_INSTANT_KILL
    def getFormatter(self):
        ...

class HWRibbonsAggregator(RibbonsAggregator):
    FEEDBACK_EVENT_TO_RIBBON_CLS_FACTORY = _HW_FEEDBACK_EVENT_TO_RIBBON_CLS_FACTORY
    FEEDBACK_EVENTS_TO_IGNORE = _HW_FEEDBACK_EVENTS_TO_IGNORE
    RIBBON_TYPES_AGGREGATED_WITH_KILL_RIBBON = _HW_RIBBON_TYPES_AGGREGATED_WITH_KILL_RIBBON
    RIBBON_TYPES_COPY_TO = _HW_RIBBON_TYPES_COPY_TO
    EXCLUDED_RIBBONS = _HW_EXCLUDED_RIBBONS
    def _aggregateRibbons(self, ribbons):
        ...

class _HWStunAssistRibbon(_StunAssistRibbon):
    def getDamageSource(self):
        ...
    def _canAggregate(self, ribbon):
        ...

# decorador original: @registerRibbonsFactory(...)
class HWAssistToKillEnemyRibbonsFactory(_AssistRibbonClassFactory):
    def __init__(self):
        ...

# decorador original: @registerRibbonsFactory(...)
class HWAssistToStunEnemyRibbonsFactory(_AssistRibbonClassFactory):
    def __init__(self):
        ...

class HWRibbonsAggregatorPlayer(HWRibbonsAggregator):
    def _onPlayerFeedbackReceived(self, events):
        ...
    def _aggregateRibbons(self, ribbons):
        ...

def _formatAddition(value):
    ...
def _formatSubtraction(value):
    ...
def _formatCounter(value):
    ...
def _hwWithoutLeftFieldRibbonFormatter(ribbon, arenaDP, updater):
    ...
def _hwActionRibbonFormatter(ribbon, arenaDP, updater):
    ...
def _hwCounterRibbonFormatter(ribbon, arenaDP, updater):
    ...
def _hwShellsPickupRibbonFormatter(ribbon, arenaDP, updater, format_=...):
    ...
def _hwSoulsMiriumizationDecreaseRibbonFormatter(ribbon, arenaDP, updater):
    ...
def _hwSoulsRefundRibbonFormatter(ribbon, _, updater):
    ...
def registerRibbonsFactory(eventID):
    ...
def aggregateWithKillRibbon(cls):
    ...
def hwCopyTo(ribbonType, isMergeCopy=False):
    ...
def hwExcludeRibbons(ribbonTypes):
    ...
def createRibbonsAggregator():
    ...
