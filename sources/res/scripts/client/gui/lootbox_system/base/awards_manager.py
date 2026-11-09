# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/lootbox_system/base/awards_manager.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/lootbox_system/base/awards_manager.py
from typing import TYPE_CHECKING
from gui.lootbox_system.base.bonuses_layout import BonusesLayout
from gui.server_events.bonuses import getNonQuestBonuses, mergeBonuses, splitBonuses
if TYPE_CHECKING:
    from typing import Any, Dict, List
    from gui.server_events.bonuses import SimpleBonus

def awardsFactory(items, ctx=None):
    bonuses = []
    for key, value in items.iteritems():
        bonuses.extend(getNonQuestBonuses(key, value, ctx))

    return bonuses


class AwardsManager(object):
    __bonusesLayout = BonusesLayout()

    @classmethod
    def init(cls):
        cls.__bonusesLayout.init()

    @classmethod
    def finalize(cls):
        cls.__bonusesLayout.fini()

    @classmethod
    def bonusesLayoutUpdate(cls):
        cls.__bonusesLayout.updateStorage()

    @classmethod
    def composeBonuses(cls, eventName, rewards, ctx=None):
        bonuses = []
        for reward in rewards:
            bonuses.extend(awardsFactory(reward, ctx))

        return cls.sortMergeBonuses(eventName, bonuses)

    @classmethod
    def sortMergeBonuses(cls, eventName, bonuses, reverse=False):
        bonuses = splitBonuses(mergeBonuses(bonuses))
        return cls.sortBonuses(eventName, bonuses, reverse)

    @classmethod
    def sortBonuses(cls, eventName, bonuses, reverse=False):
        bonuses.sort(key=(lambda bonus: cls.__bonusesLayout.getPriority(eventName, bonus)), reverse=reverse)
        return bonuses

    @classmethod
    def getRarity(cls, eventName, bonus):
        return cls.__bonusesLayout.getRarity(eventName, bonus)

    @classmethod
    def getIsVisible(cls, eventName, bonus):
        return cls.__bonusesLayout.getIsVisible(eventName, bonus)
