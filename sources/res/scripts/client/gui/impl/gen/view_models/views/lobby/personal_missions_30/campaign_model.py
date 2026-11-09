# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/personal_missions_30/campaign_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/personal_missions_30/campaign_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.personal_missions_30.select_operation_model import SelectOperationModel

class CampaignModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(CampaignModel, self).__init__(properties=properties, commands=commands)

    def getOperations(self):
        return self._getArray(0)

    def setOperations(self, value):
        self._setArray(0, value)

    @staticmethod
    def getOperationsType():
        return SelectOperationModel

    def getCampaignName(self):
        return self._getString(1)

    def setCampaignName(self, value):
        self._setString(1, value)

    def getCompletedWithHonor(self):
        return self._getBool(2)

    def setCompletedWithHonor(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(CampaignModel, self)._initialize()
        self._addArrayProperty('operations', Array())
        self._addStringProperty('campaignName', '')
        self._addBoolProperty('completedWithHonor', False)
