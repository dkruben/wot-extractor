# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/gui_items/vehicle_mechanics/factories/engine_mechanics.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/gui_items/vehicle_mechanics/factories/engine_mechanics.py
from __future__ import absolute_import
from future.utils import viewitems
from gui.shared.gui_items.vehicle_mechanics.mechanic_detectors import ENGINE_MECHANIC_DETECTORS
from gui.shared.gui_items.vehicle_mechanics.factories.base_factory import BaseMechanicFactory
from gui.shared.items_parameters.params_cache import g_paramsCache

class EngineMechanicFactory(BaseMechanicFactory):

    @classmethod
    def _getMechanicsChecks(cls, guiItem, vehDescr):
        if vehDescr is not None:
            return [(detector(vehDescr), mechanic) for mechanic, (_, detector) in viewitems(ENGINE_MECHANIC_DETECTORS)]
        else:
            return [(g_paramsCache.hasEngineMechanic(guiItem.intCD, mechanic), mechanic) for mechanic in ENGINE_MECHANIC_DETECTORS]
