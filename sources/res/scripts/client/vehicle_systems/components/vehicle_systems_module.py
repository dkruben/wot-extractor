# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicle_systems/components/vehicle_systems_module.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicle_systems/components/vehicle_systems_module.py
from __future__ import absolute_import
import CGF, GenericComponents
from cgf_components.client_worlds_helpers import clientWorldsPredicate, ClientWorld
from cgf_script.registration import registerModule
from vehicle_systems.components.debris_crashed_track_component import DebrisCrashedTrackComponent
from vehicle_systems.components.debris_crashed_track_manager import DebrisCrashedTrackSystem
from vehicle_systems.components.decal_manager import DecalComponentSystem
from vehicle_systems.components.insignia_stickers_receiver_component import InsigniaStickersReceiverSystem, InsigniaStickersReceiverComponent
from vehicle_systems.components.shot_damage_components import DamageStickerSystem, DamageStickerComponent
from vehicle_systems.components.vehicle_assembly_manager import VehicleAssemblySystem, HangarVehicleStateSwitcherSystem
from vehicle_systems.components.vehicle_custom_effects_settings import VehicleCustomEffectsSystem, VehicleCustomEffectsSettings
from vehicle_systems.components.vehicle_pickup_manager import VehiclePickupSystem

@registerModule
class VehicleSystemsModule(object):
    name = 'Vehicle Module'
    desc = 'Vehicle Core Systems'
    group = 'Vehicle'
    systems = [
     CGF.RegisterSystem(VehicleCustomEffectsSystem, domain=CGF.Domain.ClientEditor),
     CGF.RegisterSystem(DamageStickerSystem, domain=CGF.Domain.ClientEditor, updateAfter=(
      CGF.TransformUpdateSystem,)),
     CGF.RegisterSystem(DebrisCrashedTrackSystem, domain=CGF.Domain.ClientEditor),
     CGF.RegisterSystem(DecalComponentSystem, domain=CGF.Domain.ClientEditor),
     CGF.RegisterSystem(InsigniaStickersReceiverSystem, domain=CGF.Domain.ClientEditor, updateAfter=(
      CGF.TransformUpdateSystem, GenericComponents.ModelComponentSystem)),
     CGF.RegisterSystem(VehicleAssemblySystem, domain=CGF.Domain.ClientEditor, predicate=clientWorldsPredicate(ClientWorld.AllWorlds)),
     CGF.RegisterSystem(VehiclePickupSystem, domain=CGF.Domain.ClientEditor, updateAfter=(
      CGF.TransformUpdateSystem,)),
     CGF.RegisterSystem(HangarVehicleStateSwitcherSystem, domain=CGF.Domain.ClientEditor, predicate=clientWorldsPredicate(ClientWorld.HANGAR | ClientWorld.EDITOR))]
    components = [
     VehicleCustomEffectsSettings,
     DamageStickerComponent,
     InsigniaStickersReceiverComponent,
     DebrisCrashedTrackComponent]
