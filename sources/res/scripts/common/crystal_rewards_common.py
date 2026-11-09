# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/crystal_rewards_common.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/crystal_rewards_common.py
from __future__ import absolute_import
from constants import ARENA_BONUS_TYPE_NAMES
from soft_exception import SoftException

def readCrystalRewards(section, logId=''):
    results = {}
    for bonusTypeName, rewards in section.items():
        bonus_type = ARENA_BONUS_TYPE_NAMES.get(bonusTypeName)
        if not bonus_type:
            raise SoftException('%s %s: %s' % (section.name, logId, 'Unknown ARENA_BONUS_TYPE <%s>' % bonusTypeName))
        winner_rewards = rewards.readString('winner').strip()
        if not winner_rewards:
            raise SoftException('%s %s: %s' % (section.name, logId, 'not found <winner>'))
        loser_rewards = rewards.readString('loser').strip()
        if not loser_rewards:
            raise SoftException('%s %s: %s' % (section.name, logId, 'not found <loser>'))
        comparator = rewards.readString('comparator', 'fareTeamXPPosition')
        results[bonus_type] = {True: {i + 1: int(reward) for i, reward in enumerate(winner_rewards.split(' '))}, False: {i + 1: int(reward) for i, reward in enumerate(loser_rewards.split(' '))}, 'comparator': comparator}

    return results
