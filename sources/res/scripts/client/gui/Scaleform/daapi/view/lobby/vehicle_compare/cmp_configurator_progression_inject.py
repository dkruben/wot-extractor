# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_compare/cmp_configurator_progression_inject.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_compare/cmp_configurator_progression_inject.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.lobby.vehicle_compare import cmp_helpers
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from gui.impl.lobby.vehicle_compare.modifications_panel import CompareModificationsPanelView
from gui.impl.lobby.vehicle_compare.upgrades_panel import CompareUpgradesPanelView

class VehicleCompareConfiguratorProgressionInject(InjectComponentAdaptor):

    def update(self):
        self.getInjectView().update()

    def _makeInjectView(self):
        vehicle = cmp_helpers.getCmpConfiguratorMainView().getCurrentVehicleItem()
        if vehicle.getItem().postProgression.isVehSkillTree():
            return CompareUpgradesPanelView()
        return CompareModificationsPanelView()
