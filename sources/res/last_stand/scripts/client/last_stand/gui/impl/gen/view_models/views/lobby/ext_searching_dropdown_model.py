# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/impl/gen/view_models/views/lobby/ext_searching_dropdown_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/impl/gen/view_models/views/lobby/ext_searching_dropdown_model.py
from gui.impl.gen.view_models.views.lobby.platoon.searching_dropdown_model import SearchingDropdownModel

class ExtSearchingDropdownModel(SearchingDropdownModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=1):
        super(ExtSearchingDropdownModel, self).__init__(properties=properties, commands=commands)

    def getSelectedDifficulty(self):
        return self._getNumber(7)

    def setSelectedDifficulty(self, value):
        self._setNumber(7, value)

    def _initialize(self):
        super(ExtSearchingDropdownModel, self)._initialize()
        self._addNumberProperty('selectedDifficulty', 1)
