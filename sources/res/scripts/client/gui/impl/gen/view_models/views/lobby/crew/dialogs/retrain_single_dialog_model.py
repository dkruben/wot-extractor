# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/dialogs/retrain_single_dialog_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/dialogs/retrain_single_dialog_model.py
from gui.impl.gen import R
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel
from gui.impl.gen.view_models.views.lobby.crew.dialogs.role_change_model import RoleChangeModel
from gui.impl.gen.view_models.views.lobby.crew.dialogs.tankman_skills_change_base_dialog_model import TankmanSkillsChangeBaseDialogModel

class RetrainSingleDialogModel(TankmanSkillsChangeBaseDialogModel):
    __slots__ = ('onRoleCheckChanged', 'onRoleSelected')

    def __init__(self, properties=14, commands=4):
        super(RetrainSingleDialogModel, self).__init__(properties=properties, commands=commands)

    @property
    def targetVehicle(self):
        return self._getViewModel(8)

    @staticmethod
    def getTargetVehicleType():
        return VehicleInfoModel

    @property
    def roleChange(self):
        return self._getViewModel(9)

    @staticmethod
    def getRoleChangeType():
        return RoleChangeModel

    def getTitle(self):
        return self._getResource(10)

    def setTitle(self, value):
        self._setResource(10, value)

    def getWarning(self):
        return self._getResource(11)

    def setWarning(self, value):
        self._setResource(11, value)

    def getIsPriceSelected(self):
        return self._getBool(12)

    def setIsPriceSelected(self, value):
        self._setBool(12, value)

    def getHasRetrainDiscount(self):
        return self._getBool(13)

    def setHasRetrainDiscount(self, value):
        self._setBool(13, value)

    def _initialize(self):
        super(RetrainSingleDialogModel, self)._initialize()
        self._addViewModelProperty('targetVehicle', VehicleInfoModel())
        self._addViewModelProperty('roleChange', RoleChangeModel())
        self._addResourceProperty('title', R.invalid())
        self._addResourceProperty('warning', R.invalid())
        self._addBoolProperty('isPriceSelected', False)
        self._addBoolProperty('hasRetrainDiscount', False)
        self.onRoleCheckChanged = self._addCommand('onRoleCheckChanged')
        self.onRoleSelected = self._addCommand('onRoleSelected')
