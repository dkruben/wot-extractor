# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/blueprints/fragment_item_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/blueprints/fragment_item_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen import R

class FragmentItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(FragmentItemModel, self).__init__(properties=properties, commands=commands)

    def getValue(self):
        return self._getString(0)

    def setValue(self, value):
        self._setString(0, value)

    def getIcon(self):
        return self._getResource(1)

    def setIcon(self, value):
        self._setResource(1, value)

    def getFragmentCD(self):
        return self._getNumber(2)

    def setFragmentCD(self, value):
        self._setNumber(2, value)

    def getSpecialIcon(self):
        return self._getResource(3)

    def setSpecialIcon(self, value):
        self._setResource(3, value)

    def _initialize(self):
        super(FragmentItemModel, self)._initialize()
        self._addStringProperty('value', '--')
        self._addResourceProperty('icon', R.invalid())
        self._addNumberProperty('fragmentCD', 0)
        self._addResourceProperty('specialIcon', R.invalid())
