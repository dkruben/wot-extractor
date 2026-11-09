# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client_common/vehicle_appearance/component.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client_common/vehicle_appearance/component.py
from __future__ import absolute_import
import logging, typing, CGF
from cgf_script.registration import registerComponent
if typing.TYPE_CHECKING:
    from vehicle_appearance.common_tank_appearance import CommonTankAppearance
    from gui.hangar_vehicle_appearance import HangarVehicleAppearance
    TAppearance = typing.Union[(HangarVehicleAppearance, CommonTankAppearance, None)]
_logger = logging.getLogger(__name__)

@registerComponent
class VehicleAppearanceComponent(object):
    domain = CGF.Domain.ClientEditor
    userVisible = False
    vseVisible = False

    def __init__(self, appearance):
        if appearance is None:
            _logger.error('Unable to find appearance')
        self.appearance = appearance
        return
