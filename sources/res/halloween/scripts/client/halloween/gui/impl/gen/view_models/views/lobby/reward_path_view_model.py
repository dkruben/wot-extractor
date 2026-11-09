# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/impl/gen/view_models/views/lobby/reward_path_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/impl/gen/view_models/views/lobby/reward_path_view_model.py
from frameworks.wulf import Array, ViewModel
from halloween.gui.impl.gen.view_models.views.lobby.reward_path_item_view_model import RewardPathItemViewModel
from halloween.gui.impl.gen.view_models.views.lobby.vehicle_title_view_model import VehicleTitleViewModel

class RewardPathViewModel(ViewModel):
    __slots__ = ('onClose', 'onPreview', 'onViewLoaded', 'goToMission', 'goToCrewSelect')

    def __init__(self, properties=5, commands=5):
        super(RewardPathViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def mainGiftVehicle(self):
        return self._getViewModel(0)

    @staticmethod
    def getMainGiftVehicleType():
        return VehicleTitleViewModel

    def getArtefacts(self):
        return self._getArray(1)

    def setArtefacts(self, value):
        self._setArray(1, value)

    @staticmethod
    def getArtefactsType():
        return RewardPathItemViewModel

    def getIsCompleted(self):
        return self._getBool(2)

    def setIsCompleted(self, value):
        self._setBool(2, value)

    def getProgress(self):
        return self._getNumber(3)

    def setProgress(self, value):
        self._setNumber(3, value)

    def getSelectedArtefactID(self):
        return self._getString(4)

    def setSelectedArtefactID(self, value):
        self._setString(4, value)

    def _initialize(self):
        super(RewardPathViewModel, self)._initialize()
        self._addViewModelProperty('mainGiftVehicle', VehicleTitleViewModel())
        self._addArrayProperty('artefacts', Array())
        self._addBoolProperty('isCompleted', False)
        self._addNumberProperty('progress', 0)
        self._addStringProperty('selectedArtefactID', '')
        self.onClose = self._addCommand('onClose')
        self.onPreview = self._addCommand('onPreview')
        self.onViewLoaded = self._addCommand('onViewLoaded')
        self.goToMission = self._addCommand('goToMission')
        self.goToCrewSelect = self._addCommand('goToCrewSelect')
