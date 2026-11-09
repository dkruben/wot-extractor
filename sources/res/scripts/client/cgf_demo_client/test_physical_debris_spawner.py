# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/cgf_demo_client/test_physical_debris_spawner.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/cgf_demo_client/test_physical_debris_spawner.py
from __future__ import absolute_import
import functools, CGF, Triggers, Physics
from cgf_demo.demo_category import DEMO_CATEGORY
from cgf_script.registration import ComponentProperty, registerComponent

@registerComponent
class TestEntranceSpawner(object):
    group = DEMO_CATEGORY
    editorTitle = 'Test Entrance Spawner'
    domain = CGF.Domain.Client
    trigger = ComponentProperty(type=CGF.PropertyType.Link, editorName='AreaTrigger to subscribe', value=Triggers.AreaTriggerComponent)
    debrisSpawner = ComponentProperty(type=CGF.PropertyType.Link, editorName='Spawner to subscribe', value=Physics.PhysicalDebrisSpawnerComponent)


class EntranceSpawnerSystem(CGF.System):
    EntranceSpawnerActivated = CGF.ActivateReaction(CGF.ReactRw(TestEntranceSpawner))
    AreaTriggerAccess = CGF.AccessReaction(CGF.Rw(Triggers.AreaTriggerComponent))
    DebrisSpawnerAccess = CGF.AccessReaction(CGF.Rw(Physics.PhysicalDebrisSpawnerComponent))
    Reactions = CGF.Reactions(EntranceSpawnerActivated, AreaTriggerAccess, DebrisSpawnerAccess)

    def update(self):
        triggerAccess = self.reaction(self.AreaTriggerAccess)
        for entrance in self.reaction(self.EntranceSpawnerActivated):
            self._onEntranceAdded(entrance, triggerAccess)

    def _onEntranceAdded(self, entrance, triggerAccess):
        trigger = triggerAccess.find(entrance.trigger)
        if trigger:
            debrisSpawner = entrance.debrisSpawner
            trigger.addEnterReaction(functools.partial(self.__onEnter, debrisSpawner))
            trigger.addExitReaction(functools.partial(self.__onExit, debrisSpawner))

    def __onEnter(self, debrisSpawnerUuid, who, where):
        debrisSpawnerAccess = self.reaction(self.DebrisSpawnerAccess)
        spawner = debrisSpawnerAccess.find(debrisSpawnerUuid)
        if spawner:
            spawner.spawnDebris()

    def __onExit(self, debrisSpawnerUuid, who, where):
        debrisSpawnerAccess = self.reaction(self.DebrisSpawnerAccess)
        spawner = debrisSpawnerAccess.find(debrisSpawnerUuid)
        if spawner:
            spawner.removeDebris()
