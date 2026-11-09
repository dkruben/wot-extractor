# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/personal_missions_30/campaign_selector_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/personal_missions_30/campaign_selector_model.py
from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.personal_missions_30.campaign_model import CampaignModel

class CampaignSelectorViewState(Enum):
    FIRST_TWO = 'firstTwo'
    THIRD = 'third'
    COMPLETED_WITH_HONOR = 'completedWithHonor'
    LOCKED = 'locked'


class CampaignSelectorModel(ViewModel):
    __slots__ = ('onOperation', 'switchCampaign', 'onClose')
    OPERATION_ID = 'operationId'
    CAMPAIGNS_STATE = 'campaignsState'
    FIRST_ACTIVATE = 'firstActivate'

    def __init__(self, properties=4, commands=3):
        super(CampaignSelectorModel, self).__init__(properties=properties, commands=commands)

    def getCampaigns(self):
        return self._getArray(0)

    def setCampaigns(self, value):
        self._setArray(0, value)

    @staticmethod
    def getCampaignsType():
        return CampaignModel

    def getBlockedByVehicle(self):
        return self._getBool(1)

    def setBlockedByVehicle(self, value):
        self._setBool(1, value)

    def getFirstTimeEntrance(self):
        return self._getBool(2)

    def setFirstTimeEntrance(self, value):
        self._setBool(2, value)

    def getCampaignSelectorViewState(self):
        return CampaignSelectorViewState(self._getString(3))

    def setCampaignSelectorViewState(self, value):
        self._setString(3, value.value)

    def _initialize(self):
        super(CampaignSelectorModel, self)._initialize()
        self._addArrayProperty('campaigns', Array())
        self._addBoolProperty('blockedByVehicle', False)
        self._addBoolProperty('firstTimeEntrance', False)
        self._addStringProperty('campaignSelectorViewState')
        self.onOperation = self._addCommand('onOperation')
        self.switchCampaign = self._addCommand('switchCampaign')
        self.onClose = self._addCommand('onClose')
