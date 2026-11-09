# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/loot_box_view/blueprint_congrats_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/loot_box_view/blueprint_congrats_model.py
from gui.impl.gen.view_models.views.loot_box_view.congrats_view_model import CongratsViewModel

class BlueprintCongratsModel(CongratsViewModel):
    __slots__ = ()

    def __init__(self, properties=13, commands=0):
        super(BlueprintCongratsModel, self).__init__(properties=properties, commands=commands)

    def getFragments(self):
        return self._getNumber(10)

    def setFragments(self, value):
        self._setNumber(10, value)

    def getFragmentsTotal(self):
        return self._getNumber(11)

    def setFragmentsTotal(self, value):
        self._setNumber(11, value)

    def getCanConvert(self):
        return self._getBool(12)

    def setCanConvert(self, value):
        self._setBool(12, value)

    def _initialize(self):
        super(BlueprintCongratsModel, self)._initialize()
        self._addNumberProperty('fragments', 0)
        self._addNumberProperty('fragmentsTotal', 1)
        self._addBoolProperty('canConvert', False)
