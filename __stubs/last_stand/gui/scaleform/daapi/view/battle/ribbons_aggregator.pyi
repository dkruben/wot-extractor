# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/battle/ribbons_aggregator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import BattleReplay as BattleReplay
from last_stand_common.ls_battle_feedback import LSGameplayActionID as LSGameplayActionID
from last_stand_common.ls_battle_feedback import unpackGameplayActionFeedback as unpackGameplayActionFeedback
from gui.Scaleform.daapi.view.battle.shared.ribbons_aggregator import RibbonsAggregator as RibbonsAggregator, _RibbonClassFactory as _RibbonClassFactory, _ACCUMULATED_RIBBON_TYPES as _ACCUMULATED_RIBBON_TYPES, _FEEDBACK_EVENTS_TO_IGNORE as _DEFAULT_EVENTS_TO_IGNORE, _FEEDBACK_EVENT_TO_RIBBON_CLS_FACTORY as _DEFAULT_RIBBON_FACTORIES, _CausedDamageRibbon as _CausedDamageRibbon, _RIBBON_TYPES_AGGREGATED_WITH_KILL_RIBBON as _DEFAULT_RIBBONS_AGGREGATED_WITH_KILL, DAMAGE_SOURCE as DAMAGE_SOURCE, _Ribbon as _Ribbon, _SingleVehicleReceivedHitRibbon as _SingleVehicleReceivedHitRibbon, _AssistRibbonClassFactory as _AssistRibbonClassFactory, _RadioAssistRibbon as _RadioAssistRibbon, _TrackAssistRibbon as _TrackAssistRibbon, _StunAssistRibbon as _StunAssistRibbon
from gui.Scaleform.daapi.view.battle.shared.ribbons_panel import _singleVehRibbonFormatter as _singleVehRibbonFormatter, _getVehicleData as _getVehicleData, _formatCounter as _formatCounter
from last_stand.gui.ls_gui_constants import FEEDBACK_EVENT_ID as FEEDBACK_EVENT_ID
from last_stand.gui.ls_vehicle_role_helper import getVehicleRole as getVehicleRole
from last_stand_common.last_stand_constants import ATTACK_REASON as ATTACK_REASON, BATTLE_EVENT_TYPE as BATTLE_EVENT_TYPE
from last_stand.gui.scaleform.genConsts.LS_BATTLE_EFFICIENCY_TYPES import LS_BATTLE_EFFICIENCY_TYPES as LS_BATTLE_EFFICIENCY_TYPES
from gui.Scaleform.genConsts.BATTLE_EFFICIENCY_TYPES import BATTLE_EFFICIENCY_TYPES as BATTLE_EFFICIENCY_TYPES
from gui.battle_control.controllers.feedback_events import _BATTLE_EVENT_TO_PLAYER_FEEDBACK_EVENT as _BATTLE_EVENT_TO_PLAYER_FEEDBACK_EVENT, _PLAYER_FEEDBACK_EXTRA_DATA_CONVERTERS as _PLAYER_FEEDBACK_EXTRA_DATA_CONVERTERS
from items import vehicles as vehicles
_LS_FEEDBACK_EVENT_TO_RIBBON_CLS_FACTORY: dict
_LS_FEEDBACK_EVENTS_TO_IGNORE: Any
_LS_RIBBON_TYPES_AGGREGATED_WITH_KILL_RIBBON: list
_LS_RIBBON_TYPES_COPY_TO: dict

class _LSGameplayActionRibbon(_Ribbon):
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

class _LSDelayedRibbonMixin(object):
    DELAY = 0.1
    _delayedTill: Any
    def __init__(self):
        ...
    @property
    def delayedTill(self):
        ...

class _LSCausedDamageRibbon(_CausedDamageRibbon):
    __slots__: tuple
    BATTLE_EFFICIENCY_TYPE = None
    def getType(self):
        ...
    def getFormatter(self):
        ...

class _LSCausedAoeAbilityDamage(_LSCausedDamageRibbon):
    __slots__: tuple
    BATTLE_EFFICIENCY_TYPE = None
    def getDamageSource(self):
        ...
    def _canAggregate(self, ribbon):
        ...

class _LSAbstractDamageRibbonsFactory(_RibbonClassFactory):
    ATTACK_REASONS = None
    def getRibbonClass(self, event):
        ...
    @classmethod
    def registerAttackReasonRibbon(cls, reason, secondaryReason=None):
        ...
    @classmethod
    def _getLSRibbonClass(cls, reasonID, secondaryReasonID):
        ...

# decorador original: @registerRibbonsFactory(...)
class LSDamageRibbonsFactory(_LSAbstractDamageRibbonsFactory):
    ATTACK_REASONS: dict
    _DEFAULT_FACTORY: Any

# decorador original: @registerRibbonsFactory(...)
class LSReceiveDamageRibbonsFactory(_LSAbstractDamageRibbonsFactory):
    ATTACK_REASONS: dict
    _DEFAULT_FACTORY: Any

# decorador original: @registerRibbonsFactory(...)
class LSGameplayActionRibbonsFactory(_RibbonClassFactory):
    GAMEPLAY_ACTIONS: dict
    def getRibbonClass(self, event):
        ...
    @classmethod
    def registerActionRibbon(cls, reason):
        ...
    @classmethod
    def _getLSRibbonClass(cls, key):
        ...

# decorador original: @lsCopyTo(...)
# decorador original: @LSDamageRibbonsFactory.registerAttackReasonRibbon(...)
class _LSCausedVampiricDamageRibbon(_LSCausedAoeAbilityDamage):
    __slots__: tuple
    BATTLE_EFFICIENCY_TYPE = LS_BATTLE_EFFICIENCY_TYPES.LS_DMG_VAMPIRE

# decorador original: @lsCopyTo(...)
# decorador original: @LSDamageRibbonsFactory.registerAttackReasonRibbon(...)
class _LSCausedAoeDamageRibbon(_LSCausedAoeAbilityDamage):
    __slots__: tuple
    BATTLE_EFFICIENCY_TYPE = LS_BATTLE_EFFICIENCY_TYPES.LS_AOE_DAMAGE

# decorador original: @lsCopyTo(...)
# decorador original: @LSDamageRibbonsFactory.registerAttackReasonRibbon(...)
class _LSCausedAoeDamageInstantShotRibbon(_LSCausedAoeAbilityDamage):
    __slots__: tuple
    BATTLE_EFFICIENCY_TYPE = LS_BATTLE_EFFICIENCY_TYPES.LS_SHOT_AOE_DAMAGE

# decorador original: @lsCopyTo(...)
# decorador original: @LSDamageRibbonsFactory.registerAttackReasonRibbon(...)
class _LSCausedAoeDrainEnemyHpInstantShotDamageRibbon(_LSCausedAoeAbilityDamage):
    __slots__: tuple
    BATTLE_EFFICIENCY_TYPE = LS_BATTLE_EFFICIENCY_TYPES.LS_SHOT_AOE_DRAIN_ENEMY_HP

# decorador original: @lsCopyTo(...)
# decorador original: @LSDamageRibbonsFactory.registerAttackReasonRibbon(...)
class _LSCausedAoeStunInstantShotRibbon(_LSCausedAoeAbilityDamage):
    __slots__: tuple
    BATTLE_EFFICIENCY_TYPE = LS_BATTLE_EFFICIENCY_TYPES.LS_SHOT_AOE_STUN

# decorador original: @lsCopyTo(...)
# decorador original: @LSDamageRibbonsFactory.registerAttackReasonRibbon(...)
class _LSAoeFireDamageRibbon(_LSCausedAoeAbilityDamage):
    __slots__: tuple
    BATTLE_EFFICIENCY_TYPE = LS_BATTLE_EFFICIENCY_TYPES.LS_AOE_BURN

# decorador original: @LSDamageRibbonsFactory.registerAttackReasonRibbon(...)
class _LSCausedExtraDamageRibbon(_LSCausedDamageRibbon, _LSDelayedRibbonMixin):
    __slots__: tuple
    BATTLE_EFFICIENCY_TYPE = LS_BATTLE_EFFICIENCY_TYPES.LS_EXTRA_DAMAGE_SITUATIONAL
    DELAY = 0.8
    def getDamageSource(self):
        ...

# decorador original: @aggregateWithKillRibbon
# decorador original: @LSDamageRibbonsFactory.registerAttackReasonRibbon(...)
class _LSPassiveFireDamageRibbon(_LSCausedDamageRibbon):
    __slots__: tuple
    BATTLE_EFFICIENCY_TYPE = LS_BATTLE_EFFICIENCY_TYPES.LS_PASSIVE_IGNITE

# decorador original: @LSDamageRibbonsFactory.registerAttackReasonRibbon(...)
class _ObeliskDamageTransferRibbon(_LSCausedDamageRibbon):
    __slots__: tuple
    BATTLE_EFFICIENCY_TYPE = BATTLE_EFFICIENCY_TYPES.DAMAGE

# decorador original: @LSReceiveDamageRibbonsFactory.registerAttackReasonRibbon(...)
class _LSReceivedBomberExplosionHitRibbon(_SingleVehicleReceivedHitRibbon):
    __slots__: tuple
    TYPE = LS_BATTLE_EFFICIENCY_TYPES.LS_BOMBER_EXPLOSION
    def getType(self):
        ...
    def getFormatter(self):
        ...

# decorador original: @LSReceiveDamageRibbonsFactory.registerAttackReasonRibbon(...)
class _ReceivedVampireAbilityRibbon(_SingleVehicleReceivedHitRibbon):
    __slots__: tuple
    TYPE = LS_BATTLE_EFFICIENCY_TYPES.LS_DMG_VAMPIRE_RECEIVED
    def getType(self):
        ...
    def getFormatter(self):
        ...

# decorador original: @LSReceiveDamageRibbonsFactory.registerAttackReasonRibbon(...)
class _ReceivedAOEDamageAbilityHitRibbon(_SingleVehicleReceivedHitRibbon):
    __slots__: tuple
    TYPE = LS_BATTLE_EFFICIENCY_TYPES.LS_AOE_DAMAGE_RECEIVED
    def getType(self):
        ...
    def getFormatter(self):
        ...

# decorador original: @LSGameplayActionRibbonsFactory.registerActionRibbon(...)
class _LSIncomingRepairRibbon(_LSGameplayActionRibbon):
    BATTLE_EFFICIENCY_TYPE = LS_BATTLE_EFFICIENCY_TYPES.LS_REPAIR
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

# decorador original: @LSGameplayActionRibbonsFactory.registerActionRibbon(...)
class _LSOutcomingRepairRibbon(_LSGameplayActionRibbon):
    BATTLE_EFFICIENCY_TYPE = LS_BATTLE_EFFICIENCY_TYPES.LS_REPAIR_OTHER
    @property
    def isShowActionSource(self):
        ...
    def _canAggregate(self, ribbon):
        ...

# decorador original: @LSGameplayActionRibbonsFactory.registerActionRibbon(...)
class _LSModulesDamageBlockedRibbon(_LSGameplayActionRibbon):
    BATTLE_EFFICIENCY_TYPE = LS_BATTLE_EFFICIENCY_TYPES.LS_MODULES_DAMAGE_BLOCKED
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

# decorador original: @LSGameplayActionRibbonsFactory.registerActionRibbon(...)
class _LSHealthDrainedByPassiveVampireRibbon(_LSGameplayActionRibbon):
    BATTLE_EFFICIENCY_TYPE = LS_BATTLE_EFFICIENCY_TYPES.LS_PASSIVE_VAMPIRE
    @property
    def isShowActionSource(self):
        ...
    def _canAggregate(self, ribbon):
        ...

# decorador original: @LSGameplayActionRibbonsFactory.registerActionRibbon(...)
class _LSHealthByObelisk(_LSGameplayActionRibbon):
    BATTLE_EFFICIENCY_TYPE = LS_BATTLE_EFFICIENCY_TYPES.LS_REPAIR_VEHICLE_BY_OBELISK
    @property
    def isShowActionSource(self):
        ...
    def _canAggregate(self, ribbon):
        ...
    def getFormatter(self):
        ...

# decorador original: @LSGameplayActionRibbonsFactory.registerActionRibbon(...)
class _LSSituationalHealRibbon(_LSGameplayActionRibbon):
    BATTLE_EFFICIENCY_TYPE = LS_BATTLE_EFFICIENCY_TYPES.LS_HEAL_SITUATIONAL
    @property
    def isShowActionSource(self):
        ...
    def _canAggregate(self, ribbon):
        ...

# decorador original: @LSGameplayActionRibbonsFactory.registerActionRibbon(...)
class _LSEquipmentActivatedRibbon(_LSGameplayActionRibbon):
    EQUIPMENT_TO_RIBBON: dict
    _effType: Any
    def __init__(self, ribbonID, actionCtx):
        ...
    @property
    def isShowActionSource(self):
        ...
    @property
    def actionValue(self):
        ...
    @property
    def shouldShow(self):
        ...
    def getFormatter(self):
        ...
    def getType(self):
        ...
    def _canAggregate(self, ribbon):
        ...

class LSRibbonsAggregator(RibbonsAggregator):
    FEEDBACK_EVENT_TO_RIBBON_CLS_FACTORY = _LS_FEEDBACK_EVENT_TO_RIBBON_CLS_FACTORY
    FEEDBACK_EVENTS_TO_IGNORE = _LS_FEEDBACK_EVENTS_TO_IGNORE
    RIBBON_TYPES_AGGREGATED_WITH_KILL_RIBBON = _LS_RIBBON_TYPES_AGGREGATED_WITH_KILL_RIBBON
    RIBBON_TYPES_COPY_TO = _LS_RIBBON_TYPES_COPY_TO
    def _aggregateRibbons(self, ribbons):
        ...

class _LSStunAssistRibbon(_StunAssistRibbon):
    def getDamageSource(self):
        ...
    def _canAggregate(self, ribbon):
        ...

# decorador original: @registerRibbonsFactory(...)
class LSAssistToKillEnemyRibbonsFactory(_AssistRibbonClassFactory):
    def __init__(self):
        ...

# decorador original: @registerRibbonsFactory(...)
class LSAssistToStunEnemyRibbonsFactory(_AssistRibbonClassFactory):
    def __init__(self):
        ...

class LSRibbonsAggregatorPlayer(LSRibbonsAggregator):
    def _onPlayerFeedbackReceived(self, events):
        ...
    def _aggregateRibbons(self, ribbons):
        ...

def _lsActionRibbonFormatter(ribbon, arenaDP, updater):
    ...
def _lsActionRibbonFormatterWithRole(ribbon, arenaDP, updater):
    ...
def _lsModulesInvulnerabilityRibbonFormatter(ribbon, arenaDP, updater):
    ...
def registerRibbonsFactory(eventID):
    ...
def aggregateWithKillRibbon(cls):
    ...
def lsCopyTo(ribbonType, isMergeCopy=False):
    ...
def createRibbonsAggregator():
    ...
