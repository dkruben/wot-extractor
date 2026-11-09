# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/easy_tank_equip/common/preset_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/easy_tank_equip/common/preset_model.py
from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.price_model import PriceModel

class PresetDisableReason(Enum):
    NONE = 'none'
    DEMOUNT_NOT_POSSIBLE = 'demountNotPossible'
    NOT_ENOUGH_BUNKS = 'notEnoughBunks'


class PresetModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(PresetModel, self).__init__(properties=properties, commands=commands)

    @property
    def price(self):
        return self._getViewModel(0)

    @staticmethod
    def getPriceType():
        return PriceModel

    def getInstalled(self):
        return self._getBool(1)

    def setInstalled(self, value):
        self._setBool(1, value)

    def getDisableReason(self):
        return PresetDisableReason(self._getString(2))

    def setDisableReason(self, value):
        self._setString(2, value.value)

    def getStoredItemsCount(self):
        return self._getNumber(3)

    def setStoredItemsCount(self, value):
        self._setNumber(3, value)

    def getInstalledItemsCount(self):
        return self._getNumber(4)

    def setInstalledItemsCount(self, value):
        self._setNumber(4, value)

    def _initialize(self):
        super(PresetModel, self)._initialize()
        self._addViewModelProperty('price', PriceModel())
        self._addBoolProperty('installed', False)
        self._addStringProperty('disableReason')
        self._addNumberProperty('storedItemsCount', 0)
        self._addNumberProperty('installedItemsCount', 0)
