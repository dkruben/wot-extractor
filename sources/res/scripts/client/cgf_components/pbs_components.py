# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/cgf_components/pbs_components.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/cgf_components/pbs_components.py
from __future__ import absolute_import
import CGF, GenericComponents
from cgf_script.registration import registerComponent

@registerComponent
class PostBattleBoardComponent(object):
    editorTitle = 'Post-battle Board'
    serialName = 'PostBattleBoardComponent'
    domain = CGF.Domain.ClientEditor


class PostBattleSystem(CGF.System):
    PostBattleActivated = CGF.ActivateReaction(CGF.ReactRw(PostBattleBoardComponent), CGF.Rw(GenericComponents.DynamicModelComponent))
    PostBattleIterate = CGF.IterateReaction(CGF.ActiveOnly, CGF.Rw(GenericComponents.DynamicModelComponent), CGF.Has(PostBattleBoardComponent))
    Reactions = CGF.Reactions(PostBattleActivated, PostBattleIterate)

    def update(self):
        for _, dynamicComp in self.reaction(self.PostBattleActivated):
            self.onAdded(dynamicComp)

    def __init__(self, *args):
        super(PostBattleSystem, self).__init__(*args)
        self._lastWrittenMapImage = None
        return

    def onAdded(self, dynamicComp):
        if self._lastWrittenMapImage:
            dynamicComp.setMaterialDiffuseMap(self._lastWrittenMapImage)

    def applyArenaImage(self, mapImageName):
        self._lastWrittenMapImage = mapImageName
        postBattleIterate = self.reaction(self.PostBattleIterate)
        for dynamicComp in postBattleIterate:
            dynamicComp.setMaterialDiffuseMap(mapImageName)
