# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/items/combined_crew_skill.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/items/combined_crew_skill.py
from __future__ import absolute_import
from typing import Optional
from math_common import round_py2_style_int
from items import tankmen

class CombinedCrewSkill(object):
    __slots__ = ('tankmanLevel', 'levelIncrease', 'skillsEfficiency', 'isTankmanActive',
                 'hasActiveTankmanForBooster', 'boosterMultiplier')

    def __init__(self, tankmanLevel, levelIncrease, skillsEfficiency, isTankmanActive, hasActiveTankmanForBooster=False, boosterMultiplier=None):
        self.tankmanLevel = tankmanLevel
        self.levelIncrease = levelIncrease
        self.skillsEfficiency = skillsEfficiency
        self.isTankmanActive = isTankmanActive
        self.hasActiveTankmanForBooster = hasActiveTankmanForBooster
        self.boosterMultiplier = boosterMultiplier

    @property
    def level(self):
        return round_py2_style_int(self._floatLevel())

    def _floatLevel(self):
        if self.boosterMultiplier is None:
            return self.tankmanLevel + self.levelIncrease
        else:
            if self.tankmanLevel < tankmen.MAX_SKILL_LEVEL or self.skillsEfficiency < tankmen.MAX_SKILLS_EFFICIENCY:
                return tankmen.MAX_SKILL_LEVEL + self.levelIncrease
            return (tankmen.MAX_SKILL_LEVEL + self.levelIncrease) * self.boosterMultiplier

    @property
    def isActive(self):
        return self.isTankmanActive or self.boosterMultiplier is not None and self.hasActiveTankmanForBooster

    def __str__(self):
        return ('CombinedCrewSkill(level={}, isActive={}, tankmanLevel={}, skillsEfficiency={},levelIncrease={}, isTankmanActive={}, boosterMultiplier={})').format(self.level, self.isActive, self.tankmanLevel, self.skillsEfficiency, self.levelIncrease, self.isTankmanActive, self.boosterMultiplier)
