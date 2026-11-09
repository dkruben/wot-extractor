# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/post_progression/base_modification_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/post_progression/base_modification_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen import R

class BaseModificationModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(BaseModificationModel, self).__init__(properties=properties, commands=commands)

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)

    def getImageResName(self):
        return self._getString(1)

    def setImageResName(self, value):
        self._setString(1, value)

    def getTitleRes(self):
        return self._getResource(2)

    def setTitleRes(self, value):
        self._setResource(2, value)

    def getTooltipContentId(self):
        return self._getNumber(3)

    def setTooltipContentId(self, value):
        self._setNumber(3, value)

    def _initialize(self):
        super(BaseModificationModel, self)._initialize()
        self._addNumberProperty('id', 0)
        self._addStringProperty('imageResName', '')
        self._addResourceProperty('titleRes', R.invalid())
        self._addNumberProperty('tooltipContentId', 0)
