# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/common/tutorial/descriptions_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/common/tutorial/descriptions_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.tutorial.view_description_model import ViewDescriptionModel

class DescriptionsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(DescriptionsModel, self).__init__(properties=properties, commands=commands)

    def getViews(self):
        return self._getArray(0)

    def setViews(self, value):
        self._setArray(0, value)

    @staticmethod
    def getViewsType():
        return ViewDescriptionModel

    def _initialize(self):
        super(DescriptionsModel, self)._initialize()
        self._addArrayProperty('views', Array())
