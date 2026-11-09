# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/configurable_vehicle_preview.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/configurable_vehicle_preview.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.lobby.vehicle_preview.vehicle_preview import VehiclePreview
from shared_utils import CONST_CONTAINER

class OptionalBlocks(CONST_CONTAINER):
    BUYING_PANEL = 'buyingPanel'
    CLOSE_BUTTON = 'closeBtn'
    ALL = (BUYING_PANEL, CLOSE_BUTTON)


class ConfigurableVehiclePreview(VehiclePreview):

    def __init__(self, ctx):
        super(ConfigurableVehiclePreview, self).__init__(ctx)
        self.__hiddenBlocks = ctx.get('hiddenBlocks')

    def setBottomPanel(self):
        if OptionalBlocks.BUYING_PANEL in self.__hiddenBlocks:
            self.as_setBottomPanelS('')
        else:
            super(ConfigurableVehiclePreview, self).setBottomPanel()
