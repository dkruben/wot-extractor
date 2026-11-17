# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/tooltips/vehicle_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.lobby.hangar.presenters.crew_presenter import setCrewSlots as setCrewSlots
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from gui.shared.utils.functions import replaceHyphenToUnderscore as replaceHyphenToUnderscore
from halloween.gui.impl.gen.view_models.views.lobby.tooltips.vehicle_tooltip_model import VehicleTooltipModel as VehicleTooltipModel
from halloween.gui.impl.lobby.hw_helpers import isDailyKeyQuestCompleted as isDailyKeyQuestCompleted, getVehicleState as getVehicleState
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache

class VehicleTooltipView(ViewImpl):
    __slots__: tuple
    __itemsCache: Any
    __vehicle: Any
    def __init__(self, vehicleCD, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
