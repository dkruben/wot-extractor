# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/vehicle_hub/sub_presenters/stats_sub_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
import logging as logging
from constants import SHELL_TYPES as SHELL_TYPES
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.backport import createTooltipData as createTooltipData
from gui.impl.gen.view_models.common.vehicle_mechanic_model import VehicleMechanicModel as VehicleMechanicModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.special_vehicle_param_model import SpecialVehicleParamModel as SpecialVehicleParamModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.special_shell_param_model import SpecialShellParamModel as SpecialShellParamModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.shell_model import ShellModel as ShellModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.stats_model import StatsModel as StatsModel
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.impl.lobby.common.vehicle_model_helpers import fillVehicleMechanicModel as fillVehicleMechanicModel, clearVehicleMechanicModel as clearVehicleMechanicModel
from gui.impl.lobby.hangar.sub_views.veh_param_helpers import formatParameterValue as formatParameterValue
from gui.impl.lobby.vehicle_hub.sub_presenters.sub_presenter_base import SubPresenterBase as SubPresenterBase
from gui.shared.gui_items import VEHICLE_ATTR_TO_KPI_NAME_MAP as VEHICLE_ATTR_TO_KPI_NAME_MAP, KPI as KPI
from gui.shared.items_parameters.formatters import getMeasureUnitsForParameter as getMeasureUnitsForParameter
from gui.shared.items_parameters.functions import getShellParamsSwitcherModifiedShells as getShellParamsSwitcherModifiedShells
from gui.shared.items_parameters.comparator import PARAM_STATE as PARAM_STATE
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from shared_utils import first as first
SUPPORTED_SHELL_TYPES: dict
_logger: Any

class StatsSubPresenter(SubPresenterBase):
    @property
    def viewModel(self):
        ...
    def initialize(self, vhCtx, *args, **kwargs):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    def getTooltipData(self, event):
        ...
    def __fillViewModelsArray(self, shellArrayModel, mechanic):
        ...
    def __getKpiName(self, paramName, kpiSign):
        ...
    def __fillModel(self, model, params):
        ...
