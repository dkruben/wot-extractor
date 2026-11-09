# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/uilogging/veh_skill_tree/logging_constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/veh_skill_tree/logging_constants.py
from __future__ import absolute_import
from enum import Enum
FEATURE_VEH_SKILL_TREE = 'veh_skill_tree'
VEH_SKILL_TREE_SCREEN = 'tier_11_progression_screen'

class VehSkillTreeActions(str, Enum):
    CLICK = 'click'
    OPEN = 'open'
    CLOSE = 'close'


class VehSkillTreeItems(str, Enum):
    SKILL_TREE = 'skill_tree'
    RESEARCH_BUTTON = 'research_button'
