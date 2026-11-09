# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/pet_system/tooltips/synergy_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.pet_system.tooltips.synergy_tooltip_model import SynergyTooltipModel as SynergyTooltipModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.pet_system.pet_ui_settings import PetUISettings as PetUISettings
from gui.pet_system.synergy_helper import SynergyItem as SynergyItem

class SynergyTooltip(ViewImpl):
    __petID: Any
    def __init__(self, petID, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
