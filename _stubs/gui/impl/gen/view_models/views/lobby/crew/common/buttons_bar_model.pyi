# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/common/buttons_bar_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.crew.common.crew_books_button_model import CrewBooksButtonModel as CrewBooksButtonModel
from gui.impl.gen.view_models.views.lobby.crew.common.crew_operations_button_model import CrewOperationsButtonModel as CrewOperationsButtonModel
from gui.impl.gen.view_models.views.lobby.crew.common.toggle_button_model import ToggleButtonModel as ToggleButtonModel

class ButtonsBarModel(ViewModel):
    __slots__: tuple
    onCrewBooksClick: Any
    onAcceleratedTrainingClick: Any
    onWotPlusClick: Any
    def __init__(self, properties=5, commands=3):
        ...
    @property
    def crewOperations(self):
        ...
    @staticmethod
    def getCrewOperationsType():
        ...
    @property
    def crewBooks(self):
        ...
    @staticmethod
    def getCrewBooksType():
        ...
    @property
    def acceleratedTraining(self):
        ...
    @staticmethod
    def getAcceleratedTrainingType():
        ...
    @property
    def wotPlus(self):
        ...
    @staticmethod
    def getWotPlusType():
        ...
    def getIsVisible(self):
        ...
    def setIsVisible(self, value):
        ...
    def _initialize(self):
        ...
