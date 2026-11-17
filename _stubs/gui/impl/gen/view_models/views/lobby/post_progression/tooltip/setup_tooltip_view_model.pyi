# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/post_progression/tooltip/setup_tooltip_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from gui.impl.gen.view_models.views.lobby.post_progression.tooltip.feature_tooltip_view_model import FeatureTooltipViewModel as FeatureTooltipViewModel

class SetupFeatureType(Enum):
    SHELLSCONSUMABLESSWITCH = 'shells_consumables_switch'
    OPTDEVBOOSTERSSWITCH = 'opt_dev_boosters_switch'

class SetupTooltipViewModel(FeatureTooltipViewModel):
    __slots__: tuple
    def __init__(self, properties=6, commands=0):
        ...
    def getIconName(self):
        ...
    def setIconName(self, value):
        ...
    def getType(self):
        ...
    def setType(self, value):
        ...
    def getIsLevelShown(self):
        ...
    def setIsLevelShown(self, value):
        ...
    def _initialize(self):
        ...
