# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/hangar/presenters/hangar_vehicle_params_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/hangar/presenters/hangar_vehicle_params_presenter.py
from __future__ import absolute_import
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.impl.gen import R
from gui.impl.lobby.hangar.sub_views.vehicle_params_view import CurrentVehicleParamsPresenter
from gui.shared.items_parameters import params_helper
from helpers import dependency
from skeletons.gui.game_control import ILoadoutController

class HangarVehicleParamsPresenter(CurrentVehicleParamsPresenter):
    __loadoutController = dependency.descriptor(ILoadoutController)

    def __init__(self):
        self.__interactor = None
        self.__vehicleAfterInstall = None
        super(HangarVehicleParamsPresenter, self).__init__(layoutID=R.aliases.common.none(), applyFormatting=False)
        return

    def updateModel(self):
        self.__vehicleAfterInstall = self._getVehicle()
        super(HangarVehicleParamsPresenter, self).updateModel()
        self.__vehicleAfterInstall = None
        return

    def _finalize(self):
        super(HangarVehicleParamsPresenter, self)._finalize()
        if self.__interactor is not None and self.__interactor.affectsTTC and self.__interactor.hasItem:
            self.__interactor.getInteractingItem().onItemUpdated -= self.__onItemUpdated
            self.__interactor.getInteractingItem().onRevert -= self.__onItemUpdated
        return

    def _getEvents(self):
        return super(HangarVehicleParamsPresenter, self)._getEvents() + (
         (
          self.__loadoutController.onInteractorUpdated, self.__onInteractorUpdated),)

    def _isExtraParamEnabled(self):
        return True

    def _isAdditionalValueEnabled(self):
        return True

    def _getAdvancedParamTooltip(self):
        return TOOLTIPS_CONSTANTS.VEHICLE_TANK_SETUP_PARAMETERS

    def _getVehicle(self):
        if self.__vehicleAfterInstall is not None:
            return self.__vehicleAfterInstall
        else:
            if self.__interactor is not None and self.__interactor.hasChanged():
                return self.__interactor.getVehicleAfterInstall()
            return super(HangarVehicleParamsPresenter, self)._getVehicle()

    def _getDefaultVehicle(self):
        return super(HangarVehicleParamsPresenter, self)._getVehicle()

    def _getComparator(self):
        return params_helper.previewVehiclesComparator(self._getVehicle(), self._getDefaultVehicle(), True)

    def __onItemUpdated(self, _):
        self.updateModel()

    def __onInteractorUpdated(self):
        if self.__interactor is not None and self.__interactor.affectsTTC and self.__interactor.hasItem:
            self.__interactor.getInteractingItem().onItemUpdated -= self.__onItemUpdated
            self.__interactor.getInteractingItem().onRevert -= self.__onItemUpdated
        self.__interactor = self.__loadoutController.interactor
        if self.__interactor is not None and self.__interactor.affectsTTC and self.__interactor.hasItem:
            self.__interactor.getInteractingItem().onItemUpdated += self.__onItemUpdated
            self.__interactor.getInteractingItem().onRevert += self.__onItemUpdated
        self.updateModel()
        return
