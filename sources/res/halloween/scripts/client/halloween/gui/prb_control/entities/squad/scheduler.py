# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/prb_control/entities/squad/scheduler.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/prb_control/entities/squad/scheduler.py
from __future__ import absolute_import
from shared_utils import nextTick
from halloween.gui.prb_control.entities.pre_queue.scheduler import HalloweenBattleScheduler

class HalloweenSquadScheduler(HalloweenBattleScheduler):

    def _doLeave(self):
        if self._entity and self._entity.getFlags().isInQueue():
            if self._entity.getPlayerInfo().isCommander() and not self._isLeaveRequestSent:
                self._entity.exitFromQueue()
                self._isLeaveRequestSent = True
            nextTick(self._doLeave)()
        else:
            self._showRandomHangar()
            self._isLeaveRequestSent = False
