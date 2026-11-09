# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/platoon/searching_dropdown_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/platoon/searching_dropdown_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.platoon.button_model import ButtonModel

class SearchingDropdownModel(ViewModel):
    __slots__ = ('onOutsideClick', )

    def __init__(self, properties=7, commands=1):
        super(SearchingDropdownModel, self).__init__(properties=properties, commands=commands)

    @property
    def cancelSearch(self):
        return self._getViewModel(0)

    @staticmethod
    def getCancelSearchType():
        return ButtonModel

    def getBackgroundImage(self):
        return self._getString(1)

    def setBackgroundImage(self, value):
        self._setString(1, value)

    def getSeekers(self):
        return self._getNumber(2)

    def setSeekers(self, value):
        self._setNumber(2, value)

    def getSearchStartTime(self):
        return self._getNumber(3)

    def setSearchStartTime(self, value):
        self._setNumber(3, value)

    def getEstimatedTime(self):
        return self._getString(4)

    def setEstimatedTime(self, value):
        self._setString(4, value)

    def getHasXpBonus(self):
        return self._getBool(5)

    def setHasXpBonus(self, value):
        self._setBool(5, value)

    def getHasCreditsBonus(self):
        return self._getBool(6)

    def setHasCreditsBonus(self, value):
        self._setBool(6, value)

    def _initialize(self):
        super(SearchingDropdownModel, self)._initialize()
        self._addViewModelProperty('cancelSearch', ButtonModel())
        self._addStringProperty('backgroundImage', '')
        self._addNumberProperty('seekers', 0)
        self._addNumberProperty('searchStartTime', 0)
        self._addStringProperty('estimatedTime', '')
        self._addBoolProperty('hasXpBonus', False)
        self._addBoolProperty('hasCreditsBonus', False)
        self.onOutsideClick = self._addCommand('onOutsideClick')
