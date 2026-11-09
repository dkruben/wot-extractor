# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/battle_results/composer.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/battle_results/composer.py
from __future__ import absolute_import
from gui.battle_results.composer import IBattleResultStatsCtrl
from gui.battle_results.components import base
from battle_royale.gui.battle_results import templates
from battle_royale.gui.shared import event_dispatcher

class BattleRoyaleStatsComposer(IBattleResultStatsCtrl):

    def __init__(self, _):
        super(BattleRoyaleStatsComposer, self).__init__()
        self._block = base.StatsBlock(templates.BR_TOTAL_VO_META)
        self._block.addNextComponent(templates.BR_TEAM_STATS_BLOCK.clone())
        self._block.addNextComponent(templates.BR_COMMON_STATS_BLOCK.clone())
        self._block.addNextComponent(templates.BR_PERSONAL_STATS_BLOCK.clone())

    def clear(self):
        self._block.clear()

    def setResults(self, results, reusable):
        self._block.setRecord(results, reusable)

    def getVO(self):
        return self._block.getVO()

    def onResultsPosted(self, arenaUniqueID):
        event_dispatcher.showBattleRoyaleResults({'arenaUniqueID': arenaUniqueID})

    @staticmethod
    def onShowResults(arenaUniqueID):
        return
