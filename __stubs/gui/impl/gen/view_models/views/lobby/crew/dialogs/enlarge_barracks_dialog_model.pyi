# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/dialogs/enlarge_barracks_dialog_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.gen.view_models.views.dialogs.dialog_template_view_model import DialogTemplateViewModel as DialogTemplateViewModel
from gui.impl.gen.view_models.views.dialogs.sub_views.currency_view_model import CurrencyViewModel as CurrencyViewModel
from gui.impl.gen.view_models.views.lobby.crew.dialogs.stepper_view_model import StepperViewModel as StepperViewModel

class EnlargeBarracksDialogModel(DialogTemplateViewModel):
    __slots__: tuple
    onBunksCountChange: Any
    def __init__(self, properties=10, commands=3):
        ...
    @property
    def stepper(self):
        ...
    @staticmethod
    def getStepperType():
        ...
    @property
    def currency(self):
        ...
    @staticmethod
    def getCurrencyType():
        ...
    def getFreeBunksCount(self):
        ...
    def setFreeBunksCount(self, value):
        ...
    def getAllBunksCount(self):
        ...
    def setAllBunksCount(self, value):
        ...
    def _initialize(self):
        ...
