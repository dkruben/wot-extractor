# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/pet_system/tooltips/pet_storage_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.pet_system.tooltips.pet_storage_tooltip_model import PetStorageTooltipModel as PetStorageTooltipModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.pet_system.bonus_helper import BonusItem as BonusItem
from gui.pet_system.pet_item_helper import PetItem as PetItem
from helpers import dependency as dependency
from skeletons.gui.pet_system import IPetSystemController as IPetSystemController

class PetStorageTooltip(ViewImpl):
    __petController: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self):
        ...
