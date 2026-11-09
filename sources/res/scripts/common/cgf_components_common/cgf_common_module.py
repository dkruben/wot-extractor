# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/cgf_components_common/cgf_common_module.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/cgf_components_common/cgf_common_module.py
from __future__ import absolute_import
import CGF
from cgf_components_common.managers.state_managers import StateSwitcherSystem
from cgf_components_common.vehicle_components import VehicleDestroyingComponent, VehicleDamageLoggerComponent, VehicleSequenceParamsAttachedComponent
from cgf_components_common.material_component import MaterialComponent
from cgf_components_common.state_components import RemoveOnDeathComponent, SpawnOnDeathComponent, VehicleHealthObserverComponent
from cgf_components_common.vehicle_mechanics import StationaryReloadSequenceParamsComponent, CrestMovingSequenceParamsComponent
from cgf_script.registration import registerModule

@registerModule
class CommonScriptsModule(object):
    name = 'Common Module'
    desc = 'Client Server Common Components'
    group = 'Common'
    systems = [
     CGF.RegisterSystem(StateSwitcherSystem, domain=CGF.Domain.ClientServer)]
    components = [
     VehicleDestroyingComponent, 
     VehicleDamageLoggerComponent, 
     RemoveOnDeathComponent, 
     SpawnOnDeathComponent, 
     VehicleHealthObserverComponent, 
     MaterialComponent, 
     StationaryReloadSequenceParamsComponent, 
     CrestMovingSequenceParamsComponent, 
     VehicleSequenceParamsAttachedComponent]
