# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/battle_results/composer.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/battle_results/composer.py
from __future__ import absolute_import
import BigWorld
from gui import SystemMessages
from gui.battle_results.composer import IBattleResultStatsCtrl
from gui.prb_control import prbEntityProperty
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.notifications import NotificationPriorityLevel
from last_stand.gui.battle_results import templates
from last_stand.gui.shared import event_dispatcher

def showErrorMessage():
    SystemMessages.pushI18nMessage(backport.text(R.strings.system_messages.queue.isInQueue()), type=SystemMessages.SM_TYPE.Error, priority=NotificationPriorityLevel.HIGH)


class LastStandBattleStatsComposer(IBattleResultStatsCtrl):

    def __init__(self, _):
        super(LastStandBattleStatsComposer, self).__init__()
        self._block = templates.LS_TOTAL_RESULTS_BLOCK.clone()

    @prbEntityProperty
    def prbEntity(self):
        return

    def clear(self):
        self._block.clear()

    def setResults(self, results, reusable):
        self._block.setRecord(results, reusable)

    def getVO(self):
        return self._block.getVO()

    def popAnimation(self):
        return

    def onResultsPosted(self, arenaUniqueID):
        if LastStandBattleStatsComposer.prbEntity.isInQueue():
            BigWorld.callback(0, showErrorMessage)
            return
        event_dispatcher.showBattleResult(arenaUniqueID)

    @staticmethod
    def onShowResults(arenaUniqueID):
        pass
