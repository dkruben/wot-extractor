# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/personal_missions_30/tooltips/missions_category_tooltip_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/personal_missions_30/tooltips/missions_category_tooltip_model.py
from gui.impl.gen.view_models.views.lobby.personal_missions_30.common.enums import MissionCategory
from frameworks.wulf import ViewModel

class MissionsCategoryTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(MissionsCategoryTooltipModel, self).__init__(properties=properties, commands=commands)

    def getCategory(self):
        return MissionCategory(self._getString(0))

    def setCategory(self, value):
        self._setString(0, value.value)

    def getOperationName(self):
        return self._getString(1)

    def setOperationName(self, value):
        self._setString(1, value)

    def getMinLevel(self):
        return self._getNumber(2)

    def setMinLevel(self, value):
        self._setNumber(2, value)

    def getMaxLevel(self):
        return self._getNumber(3)

    def setMaxLevel(self, value):
        self._setNumber(3, value)

    def _initialize(self):
        super(MissionsCategoryTooltipModel, self)._initialize()
        self._addStringProperty('category')
        self._addStringProperty('operationName', '')
        self._addNumberProperty('minLevel', 0)
        self._addNumberProperty('maxLevel', 0)
