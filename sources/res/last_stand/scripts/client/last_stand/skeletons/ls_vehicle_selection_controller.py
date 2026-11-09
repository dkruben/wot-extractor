# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/skeletons/ls_vehicle_selection_controller.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/skeletons/ls_vehicle_selection_controller.py
from __future__ import absolute_import
from skeletons.gui.game_control import IGameController

class ILSVehicleSelectionController(IGameController):

    def activate(self):
        raise NotImplementedError

    def deactivate(self):
        raise NotImplementedError

    def selectModeVehicle(self, vehInvID=0):
        raise NotImplementedError

    def selectVehicle(self, vehInvID):
        raise NotImplementedError
