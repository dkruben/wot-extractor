# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/tooltips/vehicle_tooltip_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from battle_royale.gui.impl.gen.view_models.views.lobby.tooltips.vehicle_tooltip_view_model import VehicleTooltipViewModel as VehicleTooltipViewModel
from frameworks.wulf import ViewSettings as ViewSettings
from gui.doc_loaders.battle_royale_settings_loader import getVehicleProperties as getVehicleProperties
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.tooltips.vehicle import StatusBlockConstructor as StatusBlockConstructor
from gui.shared.tooltips.contexts import InventoryContext as InventoryContext
from gui.Scaleform.daapi.view.common.battle_royale import br_helpers as br_helpers
from battle_royale.gui.impl.lobby.br_helpers.utils import setEventInfo as setEventInfo
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController
from battle_royale.gui.impl.gen.view_models.views.lobby.enums import CoinType as CoinType
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle

class VehicleTooltipView(ViewImpl):
    __brController: Any
    __context: Any
    __vehicle: Any
    def __init__(self, intCD):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __fillStats(self, model):
        ...
    def __fillModel(self, model):
        ...
    def __fillStatus(self, vehicle, model):
        ...
