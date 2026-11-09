# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/cgf_components/mechanic_components/cyclic_rocket/staged_jet_boosters.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/cgf_components/mechanic_components/cyclic_rocket/staged_jet_boosters.py
from __future__ import absolute_import
import CGF
from StagedJetBoostersController import StagedJetBoostersController

class StagedJetBoostersComponentSystem(CGF.System):
    Activated = CGF.ActivateReaction(CGF.ReactRw(StagedJetBoostersController))
    Deactivated = CGF.DeactivateReaction(CGF.ReactRw(StagedJetBoostersController))
    Reactions = CGF.Reactions(Activated, Deactivated)

    def update(self):
        for controller in self.reaction(self.Deactivated):
            if controller.isValid and not controller.isComponentDestroyed():
                controller.detachInput()

        for controller in self.reaction(self.Activated):
            controller.attachInput()
            controller.createInputLogger()
