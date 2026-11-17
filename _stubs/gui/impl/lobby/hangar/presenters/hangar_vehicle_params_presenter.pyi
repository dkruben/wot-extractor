# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/presenters/hangar_vehicle_params_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.gen import R as R
from gui.impl.lobby.hangar.sub_views.vehicle_params_view import CurrentVehicleParamsPresenter as CurrentVehicleParamsPresenter
from gui.shared.items_parameters import params_helper as params_helper
from helpers import dependency as dependency
from skeletons.gui.game_control import ILoadoutController as ILoadoutController

class HangarVehicleParamsPresenter(CurrentVehicleParamsPresenter):
    __loadoutController: Any
    __interactor: Any
    __vehicleAfterInstall: Any
    def __init__(self):
        ...
    def updateModel(self):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def _isExtraParamEnabled(self):
        ...
    def _isAdditionalValueEnabled(self):
        ...
    def _getAdvancedParamTooltip(self):
        ...
    def _getVehicle(self):
        ...
    def _getDefaultVehicle(self):
        ...
    def _getComparator(self):
        ...
    def __onItemUpdated(self, _):
        ...
    def __onInteractorUpdated(self):
        ...
