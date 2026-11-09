# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/quick_training/tips_list_component_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/quick_training/tips_list_component_model.py
from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.crew.common.info_tip_model import InfoTipModel
from gui.impl.gen.view_models.views.lobby.crew.components.component_base_model import ComponentBaseModel

class TipsListComponentModel(ComponentBaseModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(TipsListComponentModel, self).__init__(properties=properties, commands=commands)

    def getItems(self):
        return self._getArray(1)

    def setItems(self, value):
        self._setArray(1, value)

    @staticmethod
    def getItemsType():
        return InfoTipModel

    def _initialize(self):
        super(TipsListComponentModel, self)._initialize()
        self._addArrayProperty('items', Array())
