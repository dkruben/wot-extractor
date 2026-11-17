# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/vehicles_data_providers/ls_vehicle_daily_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.impl.gen import R as R
from helpers import dependency as dependency
from gui.impl import backport as backport
import BigWorld as BigWorld
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from gui.impl.lobby.hangar.base.hangar_interfaces import IVehicleFilter as IVehicleFilter
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.server_events.event_items import ServerEventAbstract as ServerEventAbstract
from last_stand.gui.impl.gen.view_models.views.lobby.widgets.vehicle_daily_model import VehicleDailyModel as VehicleDailyModel
from last_stand.gui.impl.gen.view_models.views.lobby.widgets.vehicles_daily_model import VehiclesDailyModel as VehiclesDailyModel
from last_stand.gui.impl.lobby.ls_helpers import getQuestDescription as getQuestDescription
from last_stand.gui.impl.lobby.tooltips.simple_format_tooltip import SimpleFormatTooltipView as SimpleFormatTooltipView
from last_stand_common import last_stand_constants as last_stand_constants
from last_stand_common.last_stand_constants import LS_VEHILCE_DAILY_QUEST as LS_VEHILCE_DAILY_QUEST
from last_stand.skeletons.ls_quests_ui_cache import ILSQuestsUICache as ILSQuestsUICache
from skeletons.gui.shared import IItemsCache as IItemsCache
from future.utils import viewvalues as viewvalues, viewitems as viewitems

# base nao representavel no stub: ViewComponent[...]
class LSVehiclesDailyPresenter:
    __itemsCache: Any
    questsCache: Any
    _vehiclesComponent: Any
    __quest: Any
    __vehicleDailyCompleted: Any
    def __init__(self, vehiclesComponent):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def account(self):
        ...
    def __getDailyModel(self, vehCD):
        ...
    def __fillVehicles(self):
        ...
    def __onSyncQuestCompleted(self):
        ...
    def __updateCompletedVehicles(self):
        ...
    def __getDailyQuest(self):
        ...
    def __onUpdateVehiclesProgress(self, diff):
        ...
