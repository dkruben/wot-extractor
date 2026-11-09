# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/pet_system/tooltips/pet_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from frameworks.wulf import ViewSettings as ViewSettings, Array as Array
from frameworks.wulf.view.array import fillStringsArray as fillStringsArray
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.pet_system.tooltips.pet_tooltip_model import PetTooltipModel as PetTooltipModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.pet_system.pet_item_helper import PromoPetItem as PromoPetItem
from gui.pet_system.requester import INVALID_PET_ID as INVALID_PET_ID
_logger: Any

class PetTooltip(ViewImpl):
    petID: Any
    def __init__(self, petID=..., *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
