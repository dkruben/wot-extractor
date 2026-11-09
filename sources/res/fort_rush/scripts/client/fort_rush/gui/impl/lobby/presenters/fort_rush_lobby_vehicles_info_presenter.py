# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/presenters/fort_rush_lobby_vehicles_info_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/gui/impl/lobby/presenters/fort_rush_lobby_vehicles_info_presenter.py
from __future__ import absolute_import
import typing
from fort_rush.skeletons.battle_controller import IFortRushBattleController
from gui.impl.lobby.common.presenters.vehicles_info_presenter import VehiclesInfoPresenter
from helpers import dependency
if typing.TYPE_CHECKING:
    from gui.shared.gui_items import Vehicle

class FortRushLobbyVehiclesInfoPresenter(VehiclesInfoPresenter):
    __battleController = dependency.descriptor(IFortRushBattleController)

    def _toModelItem(self, vehicle):
        modelItem = super(FortRushLobbyVehiclesInfoPresenter, self)._toModelItem(vehicle)
        modelItem['isSuitableVehicle'] = self.__battleController.isSuitableVehicle(vehicle) is None
        return modelItem
