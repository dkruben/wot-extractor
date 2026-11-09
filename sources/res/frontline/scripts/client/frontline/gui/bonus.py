# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/bonus.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/bonus.py
from __future__ import absolute_import
import typing
from epic_constants import EPIC_SKILL_TOKEN_NAME, EPIC_SELECT_BONUS_NAME
from gui.server_events.bonuses import IntegralBonus
if typing.TYPE_CHECKING:
    from gui.server_events.bonuses import SimpleBonus

class FrontlineSkillBonus(IntegralBonus):

    def __init__(self, value, ctx=None):
        super(FrontlineSkillBonus, self).__init__(EPIC_SKILL_TOKEN_NAME, value, ctx=ctx)


def isBonusesEqual(lhv, rhv):
    if len(lhv) != len(rhv):
        return False
    for index, bonus in enumerate(lhv):
        if not bonus.isEqual(rhv[index]):
            return False

    return True


def mergeSelectable(frontlineLevel, startLvl, endLvl, bonuses, bonusesByLvl):
    indexToCheck = []
    for idx, bonus in enumerate(bonuses):
        if bonus.getName() == EPIC_SELECT_BONUS_NAME:
            if bonus.isReceived():
                indexToCheck.append(idx)
            elif frontlineLevel >= startLvl:
                bonuses[idx].updateContext({'canClaim': True})

    level = startLvl + 1
    if not indexToCheck:
        return
    while level <= endLvl:
        for idx in indexToCheck:
            mergedBonus = bonusesByLvl[level][idx]
            if level > frontlineLevel:
                bonuses[idx].updateContext({'canClaim': False})
                indexToCheck.remove(idx)
            elif mergedBonus.getName() == EPIC_SELECT_BONUS_NAME and not mergedBonus.isReceived():
                bonuses[idx].updateContext({'canClaim': True})
                indexToCheck.remove(idx)

        level += 1
