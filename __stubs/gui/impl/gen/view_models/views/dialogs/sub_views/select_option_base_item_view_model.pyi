# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/dialogs/sub_views/select_option_base_item_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.dialogs.dialog_template_generic_tooltip_view_model import DialogTemplateGenericTooltipViewModel as DialogTemplateGenericTooltipViewModel

class ComponentType(Enum):
    BASE = 'base'
    MONEY = 'money'
    DEMOUNT_KIT = 'demountKit'
    MAP = 'map'

class SelectOptionBaseItemViewModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=4, commands=0):
        ...
    @property
    def tooltip(self):
        ...
    @staticmethod
    def getTooltipType():
        ...
    def getComponentType(self):
        ...
    def setComponentType(self, value):
        ...
    def getIsDisabled(self):
        ...
    def setIsDisabled(self, value):
        ...
    def getIcon(self):
        ...
    def setIcon(self, value):
        ...
    def _initialize(self):
        ...
