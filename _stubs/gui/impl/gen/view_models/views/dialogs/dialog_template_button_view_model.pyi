# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/dialogs/dialog_template_button_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.dialogs.dialog_template_generic_tooltip_view_model import DialogTemplateGenericTooltipViewModel as DialogTemplateGenericTooltipViewModel

class ButtonType(Enum):
    MAIN = 'main'
    PRIMARY = 'primary'
    PRIMARY_GREEN = 'primaryGreen'
    PRIMARY_RED = 'primaryRed'
    SECONDARY = 'secondary'
    GHOST = 'ghost'

class DialogTemplateButtonViewModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=5, commands=0):
        ...
    @property
    def tooltip(self):
        ...
    @staticmethod
    def getTooltipType():
        ...
    def getButtonID(self):
        ...
    def setButtonID(self, value):
        ...
    def getLabel(self):
        ...
    def setLabel(self, value):
        ...
    def getIsDisabled(self):
        ...
    def setIsDisabled(self, value):
        ...
    def getType(self):
        ...
    def setType(self, value):
        ...
    def _initialize(self):
        ...
