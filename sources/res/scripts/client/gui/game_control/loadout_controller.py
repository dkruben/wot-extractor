# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/game_control/loadout_controller.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_control/loadout_controller.py
from __future__ import absolute_import
from Event import Event, EventManager
from skeletons.gui.game_control import ILoadoutController
from wg_async import wg_async, await_callback

class LoadoutController(ILoadoutController):

    def __init__(self):
        super(LoadoutController, self).__init__()
        self.__eManager = EventManager()
        self.onSlotSelected = Event(self.__eManager)
        self.onInteractorUpdated = Event(self.__eManager)
        self.onUpdateFromItem = Event(self.__eManager)
        self.onResetItem = Event(self.__eManager)
        self.onSpecializationSelect = Event(self.__eManager)
        self.__interactor = None
        return

    def fini(self):
        self.__eManager.clear()
        self.__interactor = None
        super(LoadoutController, self).fini()
        return

    @property
    def interactor(self):
        return self.__interactor

    def clearInteractor(self):
        self.__interactor = None
        self.onInteractorUpdated()
        return

    def setInteractor(self, interactor):
        self.__interactor = interactor
        self.onInteractorUpdated()


@wg_async
def updateInteractor(interactor, confirmed, rollback):
    applyQuit = True
    if confirmed:
        interactorConfirmed = yield await_callback(interactor.confirm)(skipDialog=True)
        if interactorConfirmed:
            interactor.onAcceptComplete()
        else:
            interactor.revert()
    elif rollback:
        interactor.revert()
    else:
        applyQuit = False
    if applyQuit:
        yield await_callback(interactor.applyQuit)(skipApplyAutoRenewal=False)
