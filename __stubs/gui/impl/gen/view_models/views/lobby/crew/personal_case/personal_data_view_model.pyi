# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/personal_case/personal_data_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.crew.personal_case.personal_data_card_model import PersonalDataCardModel as PersonalDataCardModel

class PersonalDataViewModel(ViewModel):
    __slots__: tuple
    onCardSelected: Any
    onNewCardViewed: Any
    onResetFilters: Any
    def __init__(self, properties=2, commands=3):
        ...
    def getIsCardsLocked(self):
        ...
    def setIsCardsLocked(self, value):
        ...
    def getCardList(self):
        ...
    def setCardList(self, value):
        ...
    @staticmethod
    def getCardListType():
        ...
    def _initialize(self):
        ...
