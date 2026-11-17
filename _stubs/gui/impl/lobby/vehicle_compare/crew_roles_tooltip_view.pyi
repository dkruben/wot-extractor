# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/vehicle_compare/crew_roles_tooltip_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.vehicle_compare.tooltips.crew_roles_tooltip_view_model import CrewRolesTooltipViewModel as CrewRolesTooltipViewModel
from gui.impl.gen.view_models.views.lobby.vehicle_compare.tooltips.crew_member_model import CrewMemberModel as CrewMemberModel
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache

class CrewRolesTooltipView(ViewImpl):
    _itemsCache: Any
    __slots__: tuple
    __vehicle: Any
    def __init__(self, vehicle):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
