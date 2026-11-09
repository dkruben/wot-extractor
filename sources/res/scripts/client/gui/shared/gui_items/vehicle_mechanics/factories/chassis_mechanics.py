# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/gui_items/vehicle_mechanics/factories/chassis_mechanics.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/gui_items/vehicle_mechanics/factories/chassis_mechanics.py
from __future__ import absolute_import
from gui.shared.gui_items.vehicle_mechanics.factories.base_factory import BaseMechanicFactory
from gui.shared.gui_items.vehicle_mechanics.mechanic_detectors import CHASSIS_MECHANIC_DETECTORS
from gui.shared.items_parameters.params_cache import g_paramsCache
from items.vehicle_mechanics_types import VehicleMechanicKey
_CHASSIS_MECHANICS = frozenset(m for m in CHASSIS_MECHANIC_DETECTORS if isinstance(m, VehicleMechanicKey))

class ChassisMechanicFactory(BaseMechanicFactory):

    @classmethod
    def _getMechanicsChecks(cls, guiItem, _):
        intCD = guiItem.intCD
        return [(g_paramsCache.hasChassisMechanic(intCD, m), m) for m in _CHASSIS_MECHANICS]
