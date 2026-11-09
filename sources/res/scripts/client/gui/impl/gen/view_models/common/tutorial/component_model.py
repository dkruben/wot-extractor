# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/common/tutorial/component_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/common/tutorial/component_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.tutorial.rect_model import RectModel

class ComponentModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ComponentModel, self).__init__(properties=properties, commands=commands)

    @property
    def rect(self):
        return self._getViewModel(0)

    @staticmethod
    def getRectType():
        return RectModel

    def getViewId(self):
        return self._getString(1)

    def setViewId(self, value):
        self._setString(1, value)

    def getComponentId(self):
        return self._getString(2)

    def setComponentId(self, value):
        self._setString(2, value)

    def _initialize(self):
        super(ComponentModel, self)._initialize()
        self._addViewModelProperty('rect', RectModel())
        self._addStringProperty('viewId', '')
        self._addStringProperty('componentId', '')
