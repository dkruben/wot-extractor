# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/VehicleModulesViewMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehicleModulesViewMeta.py
from gui.Scaleform.daapi.view.lobby.vehicle_compare.cmp_configurator_base import VehicleCompareConfiguratorBaseView

class VehicleModulesViewMeta(VehicleCompareConfiguratorBaseView):

    def onModuleHover(self, id):
        self._printOverrideError('onModuleHover')

    def onModuleClick(self, id):
        self._printOverrideError('onModuleClick')

    def as_setItemS(self, nation, raw):
        if self._isDAAPIInited():
            return self.flashObject.as_setItem(nation, raw)

    def as_setNodesStatesS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setNodesStates(data)
