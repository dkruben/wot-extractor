# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_results/components/epic.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_results/components/epic.py
from constants import ARENA_BONUS_TYPE
from frontline.gui.frontline_helpers import FLBattleTypeDescription
from gui.battle_results.components import base
from gui.impl import backport
from gui.impl.gen import R

class BattleModificationItem(base.StatsItem):
    __slots__ = ()
    arenaBonusTypes = [ARENA_BONUS_TYPE.EPIC_BATTLE, ARENA_BONUS_TYPE.EPIC_BATTLE_TRAINING]

    def _convert(self, record, reusable):
        if reusable.common.arenaBonusType in self.arenaBonusTypes:
            return FLBattleTypeDescription.getBattleTypeIconPath(record['personal']['avatar'].get('reservesModifier'), 'c_18x18')
        return ''


class StrBattleModificationItem(BattleModificationItem):

    def _convert(self, record, reusable):
        if reusable.common.arenaBonusType in self.arenaBonusTypes:
            return backport.text(R.strings.fl_common.battleType.postBattle.title(), name=FLBattleTypeDescription.getTitle(record['personal']['avatar'].get('reservesModifier')))
        return ''
