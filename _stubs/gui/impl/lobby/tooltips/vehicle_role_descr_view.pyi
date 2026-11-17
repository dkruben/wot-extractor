# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tooltips/vehicle_role_descr_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import ACTION_TYPE_TO_LABEL as ACTION_TYPE_TO_LABEL, ROLE_TYPE_TO_LABEL as ROLE_TYPE_TO_LABEL
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.gen.view_models.views.lobby.tooltips.roles_view_model import RolesViewModel as RolesViewModel
from gui.impl.gen.view_models.views.lobby.tooltips.role_action_model import RoleActionModel as RoleActionModel
from gui.prb_control.entities.base.listener import IPrbListener as IPrbListener
from frameworks.wulf import ViewSettings as ViewSettings
from helpers import dependency as dependency
from items.vehicles import getActionsByRole as getActionsByRole
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController
from skeletons.gui.shared import IItemsCache as IItemsCache

class VehicleRolesTooltipView(ViewImpl, IPrbListener):
    __rankedController: Any
    __itemsCache: Any
    def __init__(self, *args, **kwargs):
        ...
    def _onLoading(self, vehicleCD, *args, **kwargs):
        ...
