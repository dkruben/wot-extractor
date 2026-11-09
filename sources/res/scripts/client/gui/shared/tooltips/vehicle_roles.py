# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/tooltips/vehicle_roles.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/tooltips/vehicle_roles.py
from __future__ import absolute_import
from gui.shared.tooltips import ToolTipBaseData
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.impl.backport.backport_tooltip import DecoratedTooltipWindow
from gui.impl.lobby.tooltips.vehicle_role_descr_view import VehicleRolesTooltipView

class VehicleRolesTooltipContentWindowData(ToolTipBaseData):

    def __init__(self, context):
        super(VehicleRolesTooltipContentWindowData, self).__init__(context, TOOLTIPS_CONSTANTS.VEHICLE_ROLES)

    def getDisplayableData(self, vehicleCD, *args, **kwargs):
        return DecoratedTooltipWindow(VehicleRolesTooltipView(vehicleCD), useDecorator=False)
