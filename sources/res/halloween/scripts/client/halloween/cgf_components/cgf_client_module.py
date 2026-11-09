# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/cgf_components/cgf_client_module.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/cgf_components/cgf_client_module.py
from __future__ import absolute_import
import CGF
from cgf_script.registration import registerModule
from cgf_components.client_worlds_helpers import clientWorldsPredicate, ClientWorld
from halloween.cgf_components.hexapod_component import HWIsHexapod, HWHexapodSystem
from halloween.cgf_components.soul_collector_components import SoulCollectorProgressComponent, SoulCollectorComponent

@registerModule
class HalloweenClientBattleModule(object):
    name = 'Halloween Battle Client Module'
    group = 'Halloween'
    systems = [
     CGF.RegisterSystem(HWHexapodSystem, domain=CGF.Domain.Client, predicate=clientWorldsPredicate(ClientWorld.BATTLE | ClientWorld.EDITOR), perTickUpdate=True, updateAfter=(
      CGF.TransformUpdateSystem,))]
    components = [
     HWIsHexapod,
     SoulCollectorProgressComponent,
     SoulCollectorComponent]
