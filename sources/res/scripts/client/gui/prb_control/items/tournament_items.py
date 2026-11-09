# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/prb_control/items/tournament_items.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/items/tournament_items.py
from collections import namedtuple
from gui.prb_control.items.stronghold_items import StrongholdSettings

def isEnemyBattleIndex(index):
    return index >= 4


class TournamentSettings(StrongholdSettings):

    def isTournamentUnitFreezed(self):
        return super(TournamentSettings, self).isStrongholdUnitFreezed()


TournamentUnitStats = namedtuple('UnitStats', ('readyCount', 'occupiedSlotsCount',
                                               'openedSlotsCount', 'freeSlotsCount',
                                               'curTotalLevel', 'levelsSeq', 'clanMembersInRoster',
                                               'legionariesInRoster', 'playersMatchingSlotsCount'))
TournamentUnitStats.__new__.__defaults__ = (
 0, 0, 0, 0, 0, (), 0, 0, 0)
