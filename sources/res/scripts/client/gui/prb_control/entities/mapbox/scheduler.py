# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/prb_control/entities/mapbox/scheduler.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/mapbox/scheduler.py
from gui.impl import backport
from gui.impl.gen import R
from gui import SystemMessages
from gui.prb_control.entities.base.scheduler import BaseScheduler
from gui.prb_control.events_dispatcher import g_eventDispatcher
from gui.periodic_battles.models import PrimeTimeStatus
from helpers import dependency
from skeletons.gui.game_control import IMapboxController

class MapboxScheduler(BaseScheduler):
    __mapboxController = dependency.descriptor(IMapboxController)

    def __init__(self, entity):
        super(MapboxScheduler, self).__init__(entity)
        self.__isPrimeTime = False

    def init(self):
        status, _, _ = self.__mapboxController.getPrimeTimeStatus()
        self.__isPrimeTime = status == PrimeTimeStatus.AVAILABLE
        self.__mapboxController.onPrimeTimeStatusUpdated += self.__update

    def fini(self):
        self.__mapboxController.onPrimeTimeStatusUpdated -= self.__update

    def __update(self, status):
        if not self.__mapboxController.isEnabled():
            return
        else:
            isPrimeTime = status == PrimeTimeStatus.AVAILABLE
            if isPrimeTime != self.__isPrimeTime:
                self.__isPrimeTime = isPrimeTime
                if not isPrimeTime and self.__mapboxController.getCurrentCycleID() is not None:
                    SystemMessages.pushMessage(backport.text(R.strings.system_messages.mapbox.notification.primeTime()), type=SystemMessages.SM_TYPE.PrimeTime, messageData={'title': (backport.text(R.strings.system_messages.mapbox.notification.primeTime.title()))})
                g_eventDispatcher.updateUI()
            return
