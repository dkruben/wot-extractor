# wot-extractor: codigo DESCOMPILADO de sources/res/event_platform/scripts/client/event_platform/respawns/respawns_client_module.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: event_platform/scripts/client/event_platform/respawns/respawns_client_module.py
from __future__ import absolute_import
import CGF
from cgf_script.registration import registerModule
from event_platform.respawns.respawns import RespawnPolicySystem
from DisconnectRespawnValidatorComponent import DisconnectRespawnValidatorComponent
from IndividualRespawnTimerComponent import IndividualRespawnTimerComponent
from RespawnPolicyVehicleLinkComponent import RespawnPolicyVehicleLinkComponent

@registerModule
class ClientRespawnsModule(object):
    name = 'ClientRespawnsModule'
    group = 'Battle'
    systems = [
     CGF.RegisterSystem(RespawnPolicySystem, domain=CGF.Domain.Client)]
    components = [
     RespawnPolicyVehicleLinkComponent,
     DisconnectRespawnValidatorComponent,
     IndividualRespawnTimerComponent]
