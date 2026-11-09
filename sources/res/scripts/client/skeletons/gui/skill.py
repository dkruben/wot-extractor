# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/skeletons/gui/skill.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/gui/skill.py
from __future__ import absolute_import
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Optional

class ISkill(object):

    @property
    def name(self):
        raise NotImplementedError

    @property
    def customName(self):
        raise NotImplementedError

    @property
    def crewCustomName(self):
        raise NotImplementedError


class ISkillPresenter(ISkill):

    @property
    def userName(self):
        raise NotImplementedError

    @property
    def description(self):
        raise NotImplementedError

    @property
    def shortDescription(self):
        raise NotImplementedError

    @property
    def maxLvlDescription(self):
        raise NotImplementedError

    @property
    def currentLvlDescription(self):
        raise NotImplementedError

    @property
    def altDescription(self):
        raise NotImplementedError

    @property
    def altInfo(self):
        raise NotImplementedError

    @property
    def icon(self):
        raise NotImplementedError

    @property
    def extensionLessIconName(self):
        raise NotImplementedError

    @property
    def bigIconPath(self):
        raise NotImplementedError


class ISkillData(ISkill):

    @property
    def level(self):
        raise NotImplementedError

    @property
    def roleType(self):
        raise NotImplementedError

    @property
    def typeName(self):
        raise NotImplementedError

    @property
    def isEnable(self):
        raise NotImplementedError

    @property
    def isZero(self):
        raise NotImplementedError

    @property
    def isSituational(self):
        raise NotImplementedError

    @property
    def isLearned(self):
        raise NotImplementedError

    @property
    def isLearnedAsMajor(self):
        raise NotImplementedError

    @property
    def isLearnedAsBonus(self):
        raise NotImplementedError

    @property
    def isMaxLevel(self):
        raise NotImplementedError

    @property
    def isSkillActive(self):
        raise NotImplementedError

    @property
    def isRelevant(self):
        raise NotImplementedError

    @property
    def learnState(self):
        raise NotImplementedError

    @property
    def skillRole(self):
        raise NotImplementedError

    @property
    def tankmanRole(self):
        raise NotImplementedError

    def setIsSkillActive(self, isSkillActive):
        raise NotImplementedError
