# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/lootbox_system/tooltips/box_compensation_tooltip_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/lootbox_system/tooltips/box_compensation_tooltip_model.py
from frameworks.wulf import ViewModel

class BoxCompensationTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(BoxCompensationTooltipModel, self).__init__(properties=properties, commands=commands)

    def getEventName(self):
        return self._getString(0)

    def setEventName(self, value):
        self._setString(0, value)

    def getBoxesCountToGuaranteed(self):
        return self._getNumber(1)

    def setBoxesCountToGuaranteed(self, value):
        self._setNumber(1, value)

    def getBoxCategory(self):
        return self._getString(2)

    def setBoxCategory(self, value):
        self._setString(2, value)

    def _initialize(self):
        super(BoxCompensationTooltipModel, self)._initialize()
        self._addStringProperty('eventName', '')
        self._addNumberProperty('boxesCountToGuaranteed', 0)
        self._addStringProperty('boxCategory', '')
