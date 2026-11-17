# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale_client_cgf_module.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import CGF as CGF
from battleground.berserker_effect import BerserkerEffectObjectsSystem as BerserkerEffectObjectsSystem
from battleground.components import BattlegroundSequenceSystem as BattlegroundSequenceSystem
from battleground.loot_drop_object import PlaneLootAirdropSystem as PlaneLootAirdropSystem
from constants import IS_EDITOR as IS_EDITOR
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as ARENA_BONUS_TYPE_CAPS
from battle_royale.mechanics.death_zones import DeathZoneDrawSystem as DeathZoneDrawSystem
from cgf_script.registration import bonusCapsPredicate as bonusCapsPredicate, registerModule as registerModule
from BattleRoyaleAbilities import HealthRestoreAbilitySystem as HealthRestoreAbilitySystem
from battle_royale.abilities.adaptation_restore_health import AdaptationHealthRestoreEffectSystem as AdaptationHealthRestoreEffectSystem, AdaptationHealthRestoreAbilityPart as AdaptationHealthRestoreAbilityPart, AdaptationHealthRestoreEffectArea as AdaptationHealthRestoreEffectArea
from battle_royale.abilities.area_abilities import AreaAbilityVisualizationSystem as AreaAbilityVisualizationSystem, AreaAbilityVisualizer as AreaAbilityVisualizer
from battle_royale.abilities.corroding_shot_preparing import CorrodingShotPreparingSystem as CorrodingShotPreparingSystem, CorrodingShotPreparingComponent as CorrodingShotPreparingComponent, CorrodingShotPreparingNodeComponent as CorrodingShotPreparingNodeComponent
from battle_royale.abilities.influence_zones import InfluenceZoneVisualizationSystem as InfluenceZoneVisualizationSystem, InfluenceZoneEquipmentComponent as InfluenceZoneEquipmentComponent, InfluenceZoneMultiVisualizer as InfluenceZoneMultiVisualizer, InfluenceZoneTerrainArea as InfluenceZoneTerrainArea
from battle_royale.abilities.self_buff import SelfBuffSystem as SelfBuffSystem, SelfBuffComponent as SelfBuffComponent, SelfBuffNodeComponent as SelfBuffNodeComponent
from battle_royale.abilities.shot_passion import ShotPassionSystem as ShotPassionSystem, ShotPassionComponent as ShotPassionComponent, ShotPassionNodeComponent as ShotPassionNodeComponent
from battle_royale.abilities.thunder_strike import ThunderStrikeSystem as ThunderStrikeSystem, ThunderStrikeVisualizer as ThunderStrikeVisualizer
from battle_royale.cgf_components.loot_transparency import LootSensorSystem as LootSensorSystem, LootSensorComponent as LootSensorComponent, LootTransparencyTriggerComponent as LootTransparencyTriggerComponent
from battle_royale.cgf_components.vehicle_highlight import VehicleHighlightSystem as VehicleHighlightSystem
from battle_royale.abilities.dynamic_cache_loader import DynamicObjectsCacheLoaderSystem as DynamicObjectsCacheLoaderSystem

class MineFieldSystem(object):
    ...

class AffectComponentsSystem(object):
    ...

# decorador original: @registerModule
class ClientBattleRoyaleCommonModule(object):
    name = 'Battle Royale Common Client Module'
    group = 'Common'
    systems: list
    components: list

# decorador original: @registerModule
class ClientBattleRoyaleAbilitiesModule(object):
    name = 'Battle Royale Abilities Client Module'
    group = 'Abilities'
    systems: list
    components: list

# decorador original: @registerModule
class ClientBattleRoyaleSteelHunterModule(object):
    name = 'Battle Royale SteelHunter Client Module'
    group = 'Steel Hunter'
    systems: list
    components: list

# decorador original: @registerModule
class DeathZonesModule(object):
    name = 'Death Zones Mechanics Module'
    desc = 'All things related to death zones in battle royale'
    group = 'Steel Hunter'
    systems: list
