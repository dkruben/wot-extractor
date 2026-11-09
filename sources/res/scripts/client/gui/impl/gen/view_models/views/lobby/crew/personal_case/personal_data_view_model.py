# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/personal_case/personal_data_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/personal_case/personal_data_view_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.crew.personal_case.personal_data_card_model import PersonalDataCardModel

class PersonalDataViewModel(ViewModel):
    __slots__ = ('onCardSelected', 'onNewCardViewed', 'onResetFilters')

    def __init__(self, properties=2, commands=3):
        super(PersonalDataViewModel, self).__init__(properties=properties, commands=commands)

    def getIsCardsLocked(self):
        return self._getBool(0)

    def setIsCardsLocked(self, value):
        self._setBool(0, value)

    def getCardList(self):
        return self._getArray(1)

    def setCardList(self, value):
        self._setArray(1, value)

    @staticmethod
    def getCardListType():
        return PersonalDataCardModel

    def _initialize(self):
        super(PersonalDataViewModel, self)._initialize()
        self._addBoolProperty('isCardsLocked', False)
        self._addArrayProperty('cardList', Array())
        self.onCardSelected = self._addCommand('onCardSelected')
        self.onNewCardViewed = self._addCommand('onNewCardViewed')
        self.onResetFilters = self._addCommand('onResetFilters')
