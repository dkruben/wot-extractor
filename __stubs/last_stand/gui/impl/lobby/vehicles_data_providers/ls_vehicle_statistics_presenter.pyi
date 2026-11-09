# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/vehicles_data_providers/ls_vehicle_statistics_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import logging as logging
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from gui.impl.gen import R as R
from gui.impl.lobby.battle_pass.tooltips.vehicle_points_tooltip_view import VehiclePointsTooltipView as VehiclePointsTooltipView
from gui.impl.gen.view_models.views.lobby.hangar.sub_views.vehicle_statistic_model import VehicleStatisticModel as VehicleStatisticModel
from gui.impl.gen.view_models.views.lobby.hangar.sub_views.vehicle_statistics_model import VehicleStatisticsModel as VehicleStatisticsModel
from gui.impl.pub.tooltip_window import SimpleTooltipContent as SimpleTooltipContent
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.prb_control.ctrl_events import g_prbCtrlEvents as g_prbCtrlEvents
from gui.prestige.prestige_helpers import mapGradeIDToUI as mapGradeIDToUI, getCurrentGrade as getCurrentGrade, getVehiclePrestigeMap as getVehiclePrestigeMap, DEFAULT_PRESTIGE as DEFAULT_PRESTIGE
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from helpers import dependency as dependency
from last_stand.gui.impl.lobby.ls_helpers import getLSVehicleStatus as getLSVehicleStatus
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.game_control import IPlatoonController as IPlatoonController, IBattlePassController as IBattlePassController, IRentalsController as IRentalsController
from gui.impl.lobby.hangar.base.hangar_interfaces import IVehicleFilter as IVehicleFilter, IAccountStyles as IAccountStyles
from gui.shared.gui_items.dossier.stats import AccountRandomStatsBlock as AccountRandomStatsBlock
_logger: Any

# base nao representavel no stub: ViewComponent[...]
class LSVehiclesStatisticsPresenter:
    __itemsCache: Any
    __platoonCtrl: Any
    __battlePass: Any
    __rentalsCtrl: Any
    _vehiclesComponent: Any
    __accountStyles: Any
    def __init__(self, vehiclesComponent, accountStyles):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __onBPVehiclesPointsUpdated(self, updates):
        ...
    def __fillVehicles(self):
        ...
    def __onVehicleClientStateChanged(self, vehicles=None):
        ...
    def __onPlatoonMembersUpdate(self):
        ...
    def _getMaxBpScore(self, vehicle):
        ...
    def _getDailyXPFactor(self, vehicle):
        ...
    def __onUpdateVehicles(self, diff):
        ...
    def __convertToStatisticsModel(self, vehicle, accountRandomStats, prestigeLevel):
        ...
    def __updateVehicles(self, vehicles):
        ...
    @staticmethod
    def __getVehicleStatus(vehicle):
        ...
