# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/cgf_demo/test_module.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/cgf_demo/test_module.py
from __future__ import absolute_import
import CGF, logging
from constants import IS_CLIENT, IS_EDITOR
from cgf_script.registration import registerModule
from cgf_demo.demo_category import DEMO_CATEGORY
from cgf_demo.test_bridge import TestBridgeSystem, TestBridge
from cgf_demo.test_movers import TestAxisRotatorSystem, TestScriptAxisRotator, TestScriptMover
from cgf_demo.test_triggers import TestComponentCreation, TestComponentCreationSystem, TestHealthTriggersComponent, TestPrefabSpawner, TestRotateWhileInTrigger, TestTriggersSystem, TestVehicleAreaTriggerComponent
if IS_CLIENT or IS_EDITOR:
    from cgf_demo.test_edge_drawer import TestEdgeDrawerComponentSystem
    from cgf_demo.test_edge_drawer import TestEdgeDrawerComponent
else:

    class TestEdgeDrawerComponentSystem(object):
        Reactions = CGF.Reactions()


    class TestEdgeDrawerComponent(object):
        pass


_logger = logging.getLogger(__name__)

@registerModule
class TestModule(object):
    name = 'Test Module'
    group = DEMO_CATEGORY
    systems = [
     CGF.RegisterSystem(TestBridgeSystem, updateBefore=(
      CGF.TransformUpdateSystem,), domain=CGF.Domain.ClientServer),
     CGF.RegisterSystem(TestAxisRotatorSystem, updateBefore=(
      CGF.TransformUpdateSystem,), domain=CGF.Domain.ClientServer),
     CGF.RegisterSystem(TestTriggersSystem, updateBefore=(
      CGF.TransformUpdateSystem,), domain=CGF.Domain.ClientServer),
     CGF.RegisterSystem(TestComponentCreationSystem, domain=CGF.Domain.ClientServer),
     CGF.RegisterSystem(TestEdgeDrawerComponentSystem, domain=CGF.Domain.Client)]
    components = [
     TestBridge, 
     TestEdgeDrawerComponent, 
     TestScriptAxisRotator, 
     TestScriptMover, 
     TestRotateWhileInTrigger, 
     TestComponentCreation, 
     TestPrefabSpawner, 
     TestVehicleAreaTriggerComponent, 
     TestHealthTriggersComponent]
