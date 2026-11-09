# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_pass/battle_pass_award.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_pass/battle_pass_award.py
from __future__ import absolute_import
import typing
from future.utils import viewitems
from battle_pass_common import BATTLE_PASS_SELECT_BONUS_NAME
from gui.battle_pass.battle_pass_helpers import extractCompensationMoney
from gui.server_events.bonuses import getNonQuestBonuses, mergeBonuses, splitBonuses
from gui.battle_pass.bonuses_layout_controller import BonusesLayoutController
from shared_utils import findFirst
if typing.TYPE_CHECKING:
    from gui.server_events.bonuses import BattlePassSelectTokensBonus

def awardsFactory(items, ctx=None):
    bonuses = []
    items = extractCompensationMoney(items)
    for key, value in viewitems(items):
        bonuses.extend(getNonQuestBonuses(key, value, ctx))

    return bonuses


class BattlePassAwardsManager(object):
    __bonusesLayoutController = BonusesLayoutController()

    @classmethod
    def init(cls):
        cls.__bonusesLayoutController.init()

    @classmethod
    def composeBonuses(cls, rewards, ctx=None):
        bonuses = []
        for reward in rewards:
            bonuses.extend(awardsFactory(reward, ctx))

        return cls.sortBonuses(bonuses)

    @classmethod
    def sortBonuses(cls, bonuses):
        bonuses = mergeBonuses(bonuses)
        bonuses = splitBonuses(bonuses)
        bonuses.sort(key=cls.__bonusesLayoutController.getPriority, reverse=True)
        return bonuses

    @classmethod
    def hideInvisible(cls, bonuses, needSplit=False):
        if needSplit:
            bonuses = mergeBonuses(bonuses)
            bonuses = splitBonuses(bonuses)
        bonuses = list(filter(cls.__bonusesLayoutController.getIsVisible, bonuses))
        return bonuses

    @classmethod
    def getBigIcon(cls, bonus):
        return cls.__bonusesLayoutController.getBigIcon(bonus)

    @classmethod
    def uniteTokenBonuses(cls, bonuses):
        keys = []
        for bonus in bonuses:
            if bonus.getName() == BATTLE_PASS_SELECT_BONUS_NAME:
                result = {}
                for key, value in viewitems(bonus.getValue()):
                    splitKey = key.rsplit(':', 3)[0]
                    newKey = findFirst((lambda x, sk=splitKey: x.startswith(sk)), keys, key)
                    result[newKey] = value
                    if newKey not in keys:
                        keys.append(newKey)

                bonus.setValue(result)

        return bonuses
