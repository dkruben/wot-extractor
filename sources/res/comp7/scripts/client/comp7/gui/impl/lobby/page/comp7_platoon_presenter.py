# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/page/comp7_platoon_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/lobby/page/comp7_platoon_presenter.py
from __future__ import absolute_import
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.impl.lobby.page.platoon_presenter import PlatoonPresenter
from helpers import dependency
from skeletons.gui.game_control import IPlatoonController, IComp7Controller

class Comp7PlatoonPresenter(PlatoonPresenter):
    __platoonCtrl = dependency.descriptor(IPlatoonController)
    __comp7Controller = dependency.descriptor(IComp7Controller)

    def _getEvents(self):
        return super(Comp7PlatoonPresenter, self)._getEvents() + (
         (
          self.__comp7Controller.onQualificationStateUpdated, self._onUpdatePlatoon),
         (
          self.__comp7Controller.onModeConfigChanged, self._onUpdatePlatoon),
         (
          self.__comp7Controller.onBanUpdated, self._onUpdatePlatoon))

    def _initialize(self, *args, **kwargs):
        super(Comp7PlatoonPresenter, self)._initialize(args, kwargs)
        g_clientUpdateManager.addCallbacks({'inventory.1': (self._onInventoryUpdate)})

    def _finalize(self):
        g_clientUpdateManager.removeObjectCallbacks(self)
        super(Comp7PlatoonPresenter, self)._finalize()

    def _onInventoryUpdate(self, *args):
        self._onUpdatePlatoon()
