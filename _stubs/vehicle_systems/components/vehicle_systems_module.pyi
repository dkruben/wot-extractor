# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicle_systems/components/vehicle_systems_module.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import CGF as CGF
import GenericComponents as GenericComponents
from cgf_components.client_worlds_helpers import clientWorldsPredicate as clientWorldsPredicate, ClientWorld as ClientWorld
from cgf_script.registration import registerModule as registerModule
from vehicle_systems.components.debris_crashed_track_component import DebrisCrashedTrackComponent as DebrisCrashedTrackComponent
from vehicle_systems.components.debris_crashed_track_manager import DebrisCrashedTrackSystem as DebrisCrashedTrackSystem
from vehicle_systems.components.decal_manager import DecalComponentSystem as DecalComponentSystem
from vehicle_systems.components.insignia_stickers_receiver_component import InsigniaStickersReceiverSystem as InsigniaStickersReceiverSystem, InsigniaStickersReceiverComponent as InsigniaStickersReceiverComponent
from vehicle_systems.components.shot_damage_components import DamageStickerSystem as DamageStickerSystem, DamageStickerComponent as DamageStickerComponent
from vehicle_systems.components.vehicle_assembly_manager import VehicleAssemblySystem as VehicleAssemblySystem, HangarVehicleStateSwitcherSystem as HangarVehicleStateSwitcherSystem
from vehicle_systems.components.vehicle_custom_effects_settings import VehicleCustomEffectsSystem as VehicleCustomEffectsSystem, VehicleCustomEffectsSettings as VehicleCustomEffectsSettings
from vehicle_systems.components.vehicle_pickup_manager import VehiclePickupSystem as VehiclePickupSystem

# decorador original: @registerModule
class VehicleSystemsModule(object):
    name = 'Vehicle Module'
    desc = 'Vehicle Core Systems'
    group = 'Vehicle'
    systems: list
    components: list
