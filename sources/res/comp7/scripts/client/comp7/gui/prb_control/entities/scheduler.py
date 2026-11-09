# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/prb_control/entities/scheduler.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/prb_control/entities/scheduler.py
from __future__ import absolute_import
import BigWorld
from adisp import adisp_process
from gui import SystemMessages
from gui.impl import backport
from gui.impl.gen import R
from gui.periodic_battles.models import PrimeTimeStatus
from gui.prb_control import prbDispatcherProperty
from gui.prb_control.entities.base.ctx import LeavePrbAction
from gui.prb_control.entities.base.scheduler import BaseScheduler
from gui.prb_control.events_dispatcher import g_eventDispatcher
from helpers import dependency
from skeletons.gui.game_control import IComp7Controller

class Comp7Scheduler(BaseScheduler):
    comp7Controller = dependency.descriptor(IComp7Controller)

    def __init__(self, entity):
        super(Comp7Scheduler, self).__init__(entity)
        self.__isPrimeTime = False
        self.__hasPrimeTimePeripheries = False

    @prbDispatcherProperty
    def prbDispatcher(self):
        return

    def init(self):
        status, _, _ = self.comp7Controller.getPrimeTimeStatus()
        self.__isPrimeTime = status == PrimeTimeStatus.AVAILABLE
        self.__hasPrimeTimePeripheries = self.comp7Controller.hasAvailablePrimeTimeServers()
        self.comp7Controller.onStatusUpdated += self.__update

    def fini(self):
        self.comp7Controller.onStatusUpdated -= self.__update

    def __checkLeave(self):
        if not self.comp7Controller.isEnabled() or self.comp7Controller.isFrozen():
            BigWorld.callback(0.0, self.__doLeave)
            return True
        return False

    @adisp_process
    def __doLeave(self):
        yield self.prbDispatcher.doLeaveAction(LeavePrbAction(True))

    def __update(self, status):
        if self.__checkLeave():
            return
        else:
            isPrimeTime = status == PrimeTimeStatus.AVAILABLE
            hasPrimeTimePeripheries = self.comp7Controller.hasAvailablePrimeTimeServers()
            if isPrimeTime != self.__isPrimeTime:
                self.__isPrimeTime = isPrimeTime
                if self.comp7Controller.getCurrentCycleID() is not None:
                    if self.__isPrimeTime and not self.__hasPrimeTimePeripheries:
                        SystemMessages.pushMessage(text=backport.text(R.strings.comp7_ext.system_messages.primeTime.start.body()), type=SystemMessages.SM_TYPE.PrimeTime, messageData={'title': (backport.text(R.strings.comp7_ext.system_messages.primeTime.start.title()))})
                    elif not hasPrimeTimePeripheries:
                        SystemMessages.pushMessage(text=backport.text(R.strings.comp7_ext.system_messages.primeTime.end.body()), type=SystemMessages.SM_TYPE.PrimeTime, messageData={'title': (backport.text(R.strings.comp7_ext.system_messages.primeTime.end.title()))})
                g_eventDispatcher.updateUI()
            self.__hasPrimeTimePeripheries = hasPrimeTimePeripheries
            return
