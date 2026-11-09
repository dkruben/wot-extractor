# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_hub/views/sub_models/modules_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_hub/views/sub_models/modules_model.py
from frameworks.wulf import Array, Map, ViewModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.research_item_display_model import ResearchItemDisplayModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.research_item_model import ResearchItemModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.field_modification_model import FieldModificationModel

class ModulesModel(ViewModel):
    __slots__ = ('onVehicleChange', 'onInstallItem', 'onUnlockItem', 'onBuyAndInstallItem',
                 'onSellItem')

    def __init__(self, properties=4, commands=5):
        super(ModulesModel, self).__init__(properties=properties, commands=commands)

    @property
    def fieldModificationModel(self):
        return self._getViewModel(0)

    @staticmethod
    def getFieldModificationModelType():
        return FieldModificationModel

    def getPrevResearchItems(self):
        return self._getArray(1)

    def setPrevResearchItems(self, value):
        self._setArray(1, value)

    @staticmethod
    def getPrevResearchItemsType():
        return ResearchItemDisplayModel

    def getCurrentResearchItems(self):
        return self._getArray(2)

    def setCurrentResearchItems(self, value):
        self._setArray(2, value)

    @staticmethod
    def getCurrentResearchItemsType():
        return ResearchItemDisplayModel

    def getResearchItems(self):
        return self._getMap(3)

    def setResearchItems(self, value):
        self._setMap(3, value)

    @staticmethod
    def getResearchItemsType():
        return (int, ResearchItemModel)

    def _initialize(self):
        super(ModulesModel, self)._initialize()
        self._addViewModelProperty('fieldModificationModel', FieldModificationModel())
        self._addArrayProperty('prevResearchItems', Array())
        self._addArrayProperty('currentResearchItems', Array())
        self._addMapProperty('researchItems', Map(int, ResearchItemModel))
        self.onVehicleChange = self._addCommand('onVehicleChange')
        self.onInstallItem = self._addCommand('onInstallItem')
        self.onUnlockItem = self._addCommand('onUnlockItem')
        self.onBuyAndInstallItem = self._addCommand('onBuyAndInstallItem')
        self.onSellItem = self._addCommand('onSellItem')
