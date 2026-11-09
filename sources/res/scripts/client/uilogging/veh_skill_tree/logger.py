# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/uilogging/veh_skill_tree/logger.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/veh_skill_tree/logger.py
from __future__ import absolute_import
import typing
from uilogging.base.logger import MetricsLogger
from uilogging.veh_skill_tree.logging_constants import VehSkillTreeActions, VehSkillTreeItems, FEATURE_VEH_SKILL_TREE, VEH_SKILL_TREE_SCREEN
from wotdecorators import noexcept

class SkillTreeUILogger(MetricsLogger):

    def __init__(self):
        super(SkillTreeUILogger, self).__init__(FEATURE_VEH_SKILL_TREE)

    def onSkillTreeOpened(self):
        self.log(action=VehSkillTreeActions.OPEN, item=VehSkillTreeItems.SKILL_TREE, parentScreen=VEH_SKILL_TREE_SCREEN)

    def onSkillTreeClosed(self):
        self.log(action=VehSkillTreeActions.CLOSE, item=VehSkillTreeItems.SKILL_TREE, parentScreen=VEH_SKILL_TREE_SCREEN)

    @noexcept
    def onNodesResearched(self, selectedNodeIDs):
        if selectedNodeIDs is not None:
            self.log(action=VehSkillTreeActions.CLICK, item=VehSkillTreeItems.RESEARCH_BUTTON, parentScreen=VEH_SKILL_TREE_SCREEN, info=str(len(selectedNodeIDs)))
        return
