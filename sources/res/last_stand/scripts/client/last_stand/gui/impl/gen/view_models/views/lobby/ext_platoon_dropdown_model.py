# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/impl/gen/view_models/views/lobby/ext_platoon_dropdown_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/impl/gen/view_models/views/lobby/ext_platoon_dropdown_model.py
from gui.impl.gen.view_models.views.lobby.platoon.platoon_dropdown_model import PlatoonDropdownModel

class ExtPlatoonDropdownModel(PlatoonDropdownModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=1):
        super(ExtPlatoonDropdownModel, self).__init__(properties=properties, commands=commands)

    def getSelectedDifficulty(self):
        return self._getNumber(10)

    def setSelectedDifficulty(self, value):
        self._setNumber(10, value)

    def _initialize(self):
        super(ExtPlatoonDropdownModel, self)._initialize()
        self._addNumberProperty('selectedDifficulty', 1)
