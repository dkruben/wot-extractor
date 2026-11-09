# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/progression/module_vehicle_progress_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/progression/module_vehicle_progress_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.battle_results.progression.unlock_module_progress_model import UnlockModuleProgressModel
from gui.impl.gen.view_models.views.lobby.battle_results.progression.unlock_vehicle_progress_model import UnlockVehicleProgressModel

class ModuleVehicleProgressModel(ViewModel):
    __slots__ = ('onNavigate', )
    PATH = 'coui://gui/gameface/_dist/production/mono/plugins/post_battle/vehicle_research/vehicle_research.js'

    def __init__(self, properties=2, commands=1):
        super(ModuleVehicleProgressModel, self).__init__(properties=properties, commands=commands)

    def getUnlockedVehicles(self):
        return self._getArray(0)

    def setUnlockedVehicles(self, value):
        self._setArray(0, value)

    @staticmethod
    def getUnlockedVehiclesType():
        return UnlockVehicleProgressModel

    def getUnlockedModule(self):
        return self._getArray(1)

    def setUnlockedModule(self, value):
        self._setArray(1, value)

    @staticmethod
    def getUnlockedModuleType():
        return UnlockModuleProgressModel

    def _initialize(self):
        super(ModuleVehicleProgressModel, self)._initialize()
        self._addArrayProperty('unlockedVehicles', Array())
        self._addArrayProperty('unlockedModule', Array())
        self.onNavigate = self._addCommand('onNavigate')
