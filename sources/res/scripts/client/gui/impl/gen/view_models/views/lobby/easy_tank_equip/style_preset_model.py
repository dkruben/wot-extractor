# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/easy_tank_equip/style_preset_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/easy_tank_equip/style_preset_model.py
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.common.preset_model import PresetModel

class StylePresetModel(PresetModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(StylePresetModel, self).__init__(properties=properties, commands=commands)

    def getName(self):
        return self._getString(5)

    def setName(self, value):
        self._setString(5, value)

    def getImage(self):
        return self._getString(6)

    def setImage(self, value):
        self._setString(6, value)

    def getRentDuration(self):
        return self._getNumber(7)

    def setRentDuration(self, value):
        self._setNumber(7, value)

    def _initialize(self):
        super(StylePresetModel, self)._initialize()
        self._addStringProperty('name', '')
        self._addStringProperty('image', '')
        self._addNumberProperty('rentDuration', 0)
