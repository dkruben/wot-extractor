# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/tank_setup/main_tank_setup/hangar.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/tank_setup/main_tank_setup/hangar.py
from BWUtil import AsyncReturn
from wg_async import wg_async
from gui.impl.lobby.tank_setup.intro_ammunition_setup_view import showIntro
from gui.impl.lobby.tank_setup.main_tank_setup.base import MainTankSetupView

class HangarMainTankSetupView(MainTankSetupView):
    __slots__ = ()

    @property
    def currentInteractor(self):
        selectedView = self.getCurrentSubView()
        if selectedView:
            return selectedView.getInteractor()
        else:
            return

    @wg_async
    def _doSwitch(self, setupName, slotID):
        yield showIntro(setupName)
        if self._viewModel is not None:
            yield super(HangarMainTankSetupView, self)._doSwitch(setupName, slotID)
        raise AsyncReturn(None)
        return
