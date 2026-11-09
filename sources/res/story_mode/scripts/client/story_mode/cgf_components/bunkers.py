# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/cgf_components/bunkers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/cgf_components/bunkers.py
from __future__ import absolute_import
from typing import Union
import CGF
from BunkerLogicComponent import BunkerLogicComponent

class BunkersSystem(CGF.System):
    BunkerLogicActivated = CGF.ActivateReaction(CGF.ReactRw(BunkerLogicComponent))
    BunkerLogicDeactivated = CGF.DeactivateReaction(CGF.ReactRw(BunkerLogicComponent))
    BunkerLogicIterate = CGF.IterateReaction(CGF.ActiveOnly, CGF.GameObject, CGF.Rw(BunkerLogicComponent), CGF.Ro(CGF.TransformComponent))
    Reactions = CGF.Reactions(BunkerLogicActivated, BunkerLogicDeactivated, BunkerLogicIterate)

    def update(self):
        for bunkerLogic in self.reaction(self.BunkerLogicDeactivated):
            bunkerLogic.stopLogic()

        for bunkerLogic in self.reaction(self.BunkerLogicActivated):
            bunkerLogic.startLogic(self.spaceID)

    def activeBunkersDirect(self):
        return self.reaction(self.BunkerLogicIterate)

    def findActiveBunkerDirect(self, entityID):
        for _, bunker, __ in self.reaction(self.BunkerLogicIterate):
            if bunker.destructibleEntityId == entityID:
                return bunker

        return

    def findActiveBunkerLink(self, entityID):
        for go, bunker, _ in self.reaction(self.BunkerLogicIterate):
            if bunker.destructibleEntityId == entityID:
                return CGF.ComponentLink(go, BunkerLogicComponent)

        return CGF.ComponentLink()
