# wot-extractor: codigo DESCOMPILADO de sources/res/resource_well/scripts/client/resource_well/gui/impl/lobby/feature/no_vehicles_confirm.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: resource_well/scripts/client/resource_well/gui/impl/lobby/feature/no_vehicles_confirm.py
from __future__ import absolute_import
from frameworks.wulf import ViewSettings, WindowFlags
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
from gui.impl.pub.lobby_window import LobbyWindow
from gui.shared.event_dispatcher import showHangar
from helpers import dependency
from resource_well.gui.impl.gen.view_models.views.lobby.no_vehicles_confirm_model import NoVehiclesConfirmModel
from resource_well.gui.impl.lobby.feature.sounds import RESOURCE_WELL_SOUND_SPACE
from skeletons.gui.resource_well import IResourceWellController

class NoVehiclesConfirm(ViewImpl):
    __slots__ = ()
    _COMMON_SOUND_SPACE = RESOURCE_WELL_SOUND_SPACE
    __resourceWell = dependency.descriptor(IResourceWellController)

    def __init__(self):
        settings = ViewSettings(R.views.resource_well.mono.lobby.no_vehicles_confirm(), model=NoVehiclesConfirmModel())
        super(NoVehiclesConfirm, self).__init__(settings)

    @property
    def viewModel(self):
        return super(NoVehiclesConfirm, self).getViewModel()

    def _getEvents(self):
        return (
         (
          self.viewModel.showHangar, self.__showHangar),
         (
          self.__resourceWell.onEventUpdated, self.__onEventStateUpdated),
         (
          self.__resourceWell.onSettingsChanged, self.__onEventStateUpdated))

    def __showHangar(self):
        self.destroyWindow()
        showHangar()

    def __onEventStateUpdated(self):
        if not self.__resourceWell.isActive():
            self.destroyWindow()
            showHangar()


class NoVehiclesConfirmWindow(LobbyWindow):

    def __init__(self, parent=None):
        super(NoVehiclesConfirmWindow, self).__init__(wndFlags=WindowFlags.DIALOG | WindowFlags.WINDOW_FULLSCREEN, content=NoVehiclesConfirm(), parent=parent)
