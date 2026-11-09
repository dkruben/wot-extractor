# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/prb_control/entities/pre_queue/scheduler.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/prb_control/entities/pre_queue/scheduler.py
from __future__ import absolute_import
from gui.prb_control.entities.base.scheduler import BaseScheduler
from gui.prb_control.events_dispatcher import g_eventDispatcher
from shared_utils import nextTick
from helpers import dependency
from last_stand.skeletons.ls_controller import ILSController

class LastStandBattleScheduler(BaseScheduler):
    lsCtrl = dependency.descriptor(ILSController)

    def __init__(self, entity):
        super(LastStandBattleScheduler, self).__init__(entity)
        self._isLeaveRequestSent = False

    def init(self):
        self.lsCtrl.onEventDisabled += self.__onEventDisabled
        self.lsCtrl.onSettingsUpdate += self.__onSettingsUpdate

    def fini(self):
        self.lsCtrl.onEventDisabled -= self.__onEventDisabled
        self.lsCtrl.onSettingsUpdate -= self.__onSettingsUpdate

    def _doLeave(self):
        if self._entity and self._entity.isInQueue():
            if not self._isLeaveRequestSent:
                self._entity.exitFromQueue()
                self._isLeaveRequestSent = True
            nextTick(self._doLeave)()
        else:
            self._showRandomHangar()
            self._isLeaveRequestSent = False

    def _showRandomHangar(self):
        self.lsCtrl.selectRandomMode()

    def __onEventDisabled(self):
        nextTick(self._doLeave)()

    def __onSettingsUpdate(self):
        g_eventDispatcher.updateUI()
