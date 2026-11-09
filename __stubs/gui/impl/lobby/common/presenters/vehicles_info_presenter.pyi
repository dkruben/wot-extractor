# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/common/presenters/vehicles_info_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
import math as math
import typing as typing
from future.utils import itervalues as itervalues
from gui.game_control.veh_comparison_basket import isValidVehicleForComparing as isValidVehicleForComparing
from gui.impl.gen.view_models.views.lobby.hangar.sub_views.vehicles_info_model import VehiclesInfoModel as VehiclesInfoModel
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from helpers import dependency as dependency
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.game_control import IRentalsController as IRentalsController
from gui.shared.gui_items import Vehicle as Vehicle
from gui.impl.lobby.hangar.base.hangar_interfaces import IVehicleFilter as IVehicleFilter

# base nao representavel no stub: ViewComponent[...]
class VehiclesInfoPresenter:
    __rentalsCtrl: Any
    __customizationService: Any
    _vehiclesComponent: Any
    __vehiclesWithAttachments: Any
    def __init__(self, vehiclesComponent):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __fillVehicles(self):
        ...
    def _toModelItem(self, vehicle):
        ...
    def __setItem(self, model, vehicle):
        ...
    def __setupVehicles(self, vehicles):
        ...
    def __onUpdateVehicles(self, diff):
        ...
