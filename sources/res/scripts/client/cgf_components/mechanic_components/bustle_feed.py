# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/cgf_components/mechanic_components/bustle_feed.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/cgf_components/mechanic_components/bustle_feed.py
from __future__ import absolute_import
import CGF
from constants import IS_CLIENT
from cgf_modules.variable_components import VariableStorageComponent
if IS_CLIENT:
    from BustleFeedController import BustleFeedController
else:

    class BustleFeedController(object):
        pass


class BustleFeedVariableStorageCachingSystem(CGF.System):
    Activated = CGF.ActivateReaction(CGF.GameObject, CGF.ReactRw(BustleFeedController), CGF.Ro(VariableStorageComponent))
    Deactivated = CGF.DeactivateReaction(CGF.ReactRw(BustleFeedController), CGF.Ro(VariableStorageComponent))
    Reactions = CGF.Reactions(Deactivated, Activated)

    def update(self):
        for controller, _ in self.reaction(self.Deactivated):
            controller.setVariableStorageGO(None)

        for go, controller, _ in self.reaction(self.Activated):
            controller.setVariableStorageGO(go)

        return
