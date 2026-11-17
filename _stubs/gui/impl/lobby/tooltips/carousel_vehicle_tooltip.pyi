# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tooltips/carousel_vehicle_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import math as math
import typing as typing
from dossiers2.ui.achievements import MARK_ON_GUN_RECORD as MARK_ON_GUN_RECORD
from frameworks.wulf.view.array import fillIntsArray as fillIntsArray
from gui.battle_pass.battle_pass_helpers import getSupportedCurrentArenaBonusType as getSupportedCurrentArenaBonusType
from gui.impl import backport as backport
from gui.impl.auxiliary.tooltips.simple_tooltip import createSimpleTooltip as createSimpleTooltip
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.tooltips.carousel_vehicle_tooltip_model import CarouselVehicleTooltipModel as CarouselVehicleTooltipModel
from gui.impl.lobby.common.vehicle_model_helpers import fillVehicleMechanicsArray as fillVehicleMechanicsArray
from gui.impl.lobby.hangar.presenters.crew_presenter import setCrewSlots as setCrewSlots
from gui.impl.lobby.common.presenters.dynamic_economics_presenter import DynamicEconomicsPresenter as DynamicEconomicsPresenter
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.prb_control import prbEntityProperty as prbEntityProperty
from gui.prb_control.settings import PRE_QUEUE_RESTRICTION as PRE_QUEUE_RESTRICTION
from gui.prestige.prestige_helpers import mapGradeIDToUI as mapGradeIDToUI, getCurrentGrade as getCurrentGrade, getCurrentProgress as getCurrentProgress, getVehiclePrestige as getVehiclePrestige
from gui.shared.formatters.ranges import toRomanRangeString as toRomanRangeString
from gui.shared.gui_items.Vehicle import getTypeUserName as getTypeUserName
from gui.shared.gui_items.dossier.achievements import isMarkOfMasteryAchieved as isMarkOfMasteryAchieved
from helpers import dependency as dependency, time_utils as time_utils
from skeletons.gui.game_control import IBattlePassController as IBattlePassController, IWotPlusController as IWotPlusController, IRestBonusController as IRestBonusController
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from gui.impl.gen.view_models.views.lobby.tooltips.statistics_model import StatisticsModel as StatisticsModel
from gui.impl.gen.view_models.views.lobby.tooltips.earnings_model import EarningsModel as EarningsModel
from gui.impl.gen.view_models.views.lobby.tooltips.service_records_model import ServiceRecordsModel as ServiceRecordsModel
_logger: Any

# base nao representavel no stub: ViewComponent[...]
class CarouselVehicleTooltipView:
    LAYOUT_ID: Any
    _itemsCache: Any
    _battlePass: Any
    _wotPlusCtrl: Any
    _restBonusCtrl: Any
    _inventoryId: Any
    def __init__(self, inventoryId):
        ...
    @property
    def viewModel(self):
        ...
    def _getChildComponents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getVehicleStatus(self, vehicle):
        ...
    def _getDailyXPFactor(self, vehicle):
        ...
    def _getBpProgression(self, vehicleIntCD):
        ...
    def _getIsBpEntityValid(self):
        ...
    # decorador original: @prbEntityProperty
    def __prbEntity(self):
        ...
    def __getCurrentArenaBonusType(self):
        ...
    def __setStatistics(self, statisticsModel, vehicle):
        ...
    def __setEarnings(self, earningsModel, vehicle):
        ...
    def __setServiceRecords(self, serviceRecordsModel, vehicle):
        ...

def getUnsuitable2queueTooltip(parent, event, validationResult, resPath, **kwargs):
    ...
