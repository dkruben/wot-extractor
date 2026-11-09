# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/blueprints/blueprint_balance_content_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/blueprints/blueprint_balance_content_model.py
from gui.impl.gen.view_models.views.common_balance_content_model import CommonBalanceContentModel
from gui.impl.gen.view_models.views.lobby.blueprints.fragment_item_model import FragmentItemModel

class BlueprintBalanceContentModel(CommonBalanceContentModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(BlueprintBalanceContentModel, self).__init__(properties=properties, commands=commands)

    @property
    def intelligenceBalance(self):
        return self._getViewModel(1)

    @staticmethod
    def getIntelligenceBalanceType():
        return FragmentItemModel

    def getAllianceName(self):
        return self._getString(2)

    def setAllianceName(self, value):
        self._setString(2, value)

    def _initialize(self):
        super(BlueprintBalanceContentModel, self)._initialize()
        self._addViewModelProperty('intelligenceBalance', FragmentItemModel())
        self._addStringProperty('allianceName', '')
