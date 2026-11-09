# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/battle/ribbons_aggregator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BattleReplay as BattleReplay
from constants import ATTACK_REASON as ATTACK_REASON
from gui.Scaleform.daapi.view.battle.shared.ribbons_aggregator import RibbonsAggregator as RibbonsAggregator, _ACCUMULATED_RIBBON_TYPES as _ACCUMULATED_RIBBON_TYPES, _FEEDBACK_EVENT_TO_RIBBON_CLS_FACTORY as _DEFAULT_RIBBON_FACTORIES, _Ribbon as _Ribbon, _RibbonSingleClassFactory as _RibbonSingleClassFactory, _RibbonClassFactory as _RibbonClassFactory, _DamageRibbonClassFactory as _DamageRibbonClassFactory, _ReceivedDamageHitRibbon as _ReceivedDamageHitRibbon, _ReceivedFireHitRibbon as _ReceivedFireHitRibbon, _ReceivedRamHitRibbon as _ReceivedRamHitRibbon, _ReceivedWorldCollisionHitRibbon as _ReceivedWorldCollisionHitRibbon, _ArtilleryReceivedDamageHitRibbon as _ArtilleryReceivedDamageHitRibbon, _BombersReceivedDamageHitRibbon as _BombersReceivedDamageHitRibbon, _ArtilleryReceivedFireHitRibbon as _ArtilleryReceivedFireHitRibbon, _BombersReceivedFireHitRibbon as _BombersReceivedFireHitRibbon, _EpicRecoveryRibbon as _EpicRecoveryRibbon, _DeathZoneRibbon as _DeathZoneRibbon, _ReceivedBerserkerHitRibbon as _ReceivedBerserkerHitRibbon, _ReceivedBySpawnedBotHitRibbon as _ReceivedBySpawnedBotHitRibbon, _ReceivedByMinefieldRibbon as _ReceivedByMinefieldRibbon, _ReceivedByDamagingSmokeRibbon as _ReceivedByDamagingSmokeRibbon, _ReceivedByDamagingCorrodingShotRibbon as _ReceivedByDamagingCorrodingShotRibbon, _ReceivedByFireCircleRibbon as _ReceivedByFireCircleRibbon, _ReceivedByClingBranderRibbon as _ReceivedByClingBranderRibbon, _ReceivedByDamagingThunderStrikeRibbon as _ReceivedByDamagingThunderStrikeRibbon, _FortArtilleryReceivedDamageHitRibbon as _FortArtilleryReceivedDamageHitRibbon, _ReceivedByAirStrikeRibbon as _ReceivedByAirStrikeRibbon, _ReceivedByArtilleryRibbon as _ReceivedByArtilleryRibbon, _StaticDeathZoneRibbon as _StaticDeathZoneRibbon, _MinefieldZoneRibbon as _MinefieldZoneRibbon, _BattleshipRibbon as _BattleshipRibbon, DAMAGE_SOURCE as DAMAGE_SOURCE, _ReceivedFireDamageZoneRibbon as _ReceivedFireDamageZoneRibbon, _ReceivedHERocketDamageRibbon as _ReceivedHERocketDamageRibbon
from gui.Scaleform.genConsts.BATTLE_EFFICIENCY_TYPES import BATTLE_EFFICIENCY_TYPES as BATTLE_EFFICIENCY_TYPES
from gui.battle_control.battle_constants import FEEDBACK_EVENT_ID as FEEDBACK_EVENT_ID
from gui.impl import backport as backport
from gui.impl.gen import R as R
from story_mode_common.story_mode_constants import VEHICLE_BUNKER_TURRET_TAG as VEHICLE_BUNKER_TURRET_TAG
_SM_FEEDBACK_EVENT_TO_RIBBON_CLS_FACTORY: dict

class _BunkerRibbon(_Ribbon):
    __slots__: tuple
    _damagePoints: Any
    def __init__(self, ribbonID, damagePoints):
        ...
    @classmethod
    def createFromFeedbackEvent(cls, ribbonID, event):
        ...
    def getExtraValue(self):
        ...
    def _canAggregate(self, ribbon):
        ...
    def _aggregate(self, ribbon):
        ...
    def getFormatter(self):
        ...
    @property
    def isShowActionSource(self):
        ...
    @staticmethod
    def getVehicleID():
        ...

class StoryModeReceivedArtilleryDamageRibbon(_ReceivedByArtilleryRibbon):
    __slots__: tuple
    def getDamageSource(self):
        ...

class BunkerDamagedRibbon(_BunkerRibbon):
    __slots__: tuple
    def __init__(self, ribbonID, extra):
        ...
    def getType(self):
        ...

class BunkerBattleshipDamagedRibbon(BunkerDamagedRibbon):
    __slots__: tuple
    def getType(self):
        ...

class BunkerDestroyerDamagedRibbon(BunkerDamagedRibbon):
    __slots__: tuple
    def getType(self):
        ...

class BunkerDestroyedRibbon(_BunkerRibbon):
    __slots__: tuple
    def getType(self):
        ...
    def _canAggregate(self, ribbon):
        ...

class _BunkerDamagedRibbonClassFactory(_RibbonClassFactory):
    __slots__: tuple
    __damageCls: Any
    __damageByBattleship: Any
    __damageByDestroyer: Any
    def __init__(self, damageCls, artilleryDamageCls, damageByDestroyerCls):
        ...
    def getRibbonClass(self, event):
        ...

class StoryModeRibbonsAggregator(RibbonsAggregator):
    FEEDBACK_EVENT_TO_RIBBON_CLS_FACTORY = _SM_FEEDBACK_EVENT_TO_RIBBON_CLS_FACTORY

class StoryModeRibbonsAggregatorPlayer(StoryModeRibbonsAggregator):
    def _onPlayerFeedbackReceived(self, events):
        ...
    def _aggregateRibbons(self, ribbons):
        ...

def _bunkerRibbonFormatter(ribbon, _, updater):
    ...
def createRibbonsAggregator():
    ...
