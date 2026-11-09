# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/gen/view_models/views/lobby/platoon/comp7_light_window_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/impl/gen/view_models/views/lobby/platoon/comp7_light_window_model.py
from frameworks.wulf import Array
from comp7_light.gui.impl.gen.view_models.views.lobby.platoon.comp7_light_header_model import Comp7LightHeaderModel
from comp7_light.gui.impl.gen.view_models.views.lobby.platoon.comp7_light_slot_model import Comp7LightSlotModel
from gui.impl.gen.view_models.views.lobby.platoon.members_window_model import MembersWindowModel

class Comp7LightWindowModel(MembersWindowModel):
    __slots__ = ()

    def __init__(self, properties=19, commands=3):
        super(Comp7LightWindowModel, self).__init__(properties=properties, commands=commands)

    @property
    def header(self):
        return self._getViewModel(17)

    @staticmethod
    def getHeaderType():
        return Comp7LightHeaderModel

    def getSlots(self):
        return self._getArray(18)

    def setSlots(self, value):
        self._setArray(18, value)

    @staticmethod
    def getSlotsType():
        return Comp7LightSlotModel

    def _initialize(self):
        super(Comp7LightWindowModel, self)._initialize()
        self._addViewModelProperty('header', Comp7LightHeaderModel())
        self._addArrayProperty('slots', Array())
