# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/StateMachineNetworkSync.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/StateMachineNetworkSync.py
from __future__ import absolute_import
import CGF
from cgf_client_common.entity_dyn_components import ReplicableDynamicScriptComponent
from cgf_script.registration import registerReplicableComponent
from CgfStateMachine import StateMachineComponent

@registerReplicableComponent
class StateMachineNetworkSync(ReplicableDynamicScriptComponent):
    editorTitle = 'CGF State Machine Network Sync'


class StateMachineNetworkSyncSystem(CGF.System):
    StateMachineIterate = CGF.IterateReaction(CGF.ActiveOnly, CGF.Rw(StateMachineComponent), CGF.Ro(StateMachineNetworkSync))
    Reactions = CGF.Reactions(StateMachineIterate)

    def update(self):
        for stateMachineComponent, networkSync in self.reaction(self.StateMachineIterate):
            if networkSync.replicableStateIndex is not None:
                stateMachineComponent.replicatedActiveStateIndex = networkSync.replicableStateIndex

        return
