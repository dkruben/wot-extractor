# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/hangar/ResearchPanel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.Scaleform.genConsts.RESEARCH_COUNTER_STATES import RESEARCH_COUNTER_STATES as RESEARCH_COUNTER_STATES
from gui.veh_post_progression.helpers import needToShowCounter as needToShowCounter
from items.battle_royale import isBattleRoyale as isBattleRoyale
from constants import IGR_TYPE as IGR_TYPE
from debug_utils import LOG_ERROR as LOG_ERROR
from gui import makeHtmlString as makeHtmlString
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.daapi.view.lobby.vehicle_compare.formatters import resolveStateTooltip as resolveStateTooltip
from gui.Scaleform.daapi.view.meta.ResearchPanelMeta import ResearchPanelMeta as ResearchPanelMeta
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.Scaleform.locale.VEH_COMPARE import VEH_COMPARE as VEH_COMPARE
from gui.shared import event_dispatcher as shared_events
from gui.shared.formatters import text_styles as text_styles
from gui.shared.formatters.time_formatters import getTimeLeftStr as getTimeLeftStr
from gui.shared.tutorial_helper import getTutorialGlobalStorage as getTutorialGlobalStorage
from gui.shared.utils.module_upd_available_helper import getResearchInfo as getResearchInfo
from gui.veh_post_progression.models.ext_money import ExtendedMoney as ExtendedMoney
from helpers import i18n as i18n, dependency as dependency
from nation_change.nation_change_helpers import iterVehiclesWithNationGroupInOrder as iterVehiclesWithNationGroupInOrder
from skeletons.gui.game_control import IVehicleComparisonBasket as IVehicleComparisonBasket, IIGRController as IIGRController
from skeletons.gui.shared import IItemsCache as IItemsCache
from tutorial.control.context import GLOBAL_FLAG as GLOBAL_FLAG
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle

class ResearchPanel(ResearchPanelMeta):
    itemsCache: Any
    comparisonBasket: Any
    igrCtrl: Any
    __isNavigationEnabled: Any
    def __init__(self):
        ...
    def _populate(self):
        ...
    def __onBlueprintsSettingsChanged(self, diff):
        ...
    def __onUpdateBlueprints(self, _):
        ...
    def _dispose(self):
        ...
    def setNavigationEnabled(self, isEnabled):
        ...
    def goToResearch(self):
        ...
    def goToPostProgression(self):
        ...
    def addVehToCompare(self):
        ...
    def onCurrentVehicleChanged(self):
        ...
    def __onIgrTypeChanged(self, *args):
        ...
    def __updateVehIGRStatus(self):
        ...
    def __updateModuleUpdateAvailable(self):
        ...
    def onVehicleTypeXPChanged(self, xps):
        ...
    def onVehicleBecomeElite(self, elite):
        ...
    def __onCompareBasketChanged(self, changedData):
        ...
    def __getVehCompareData(self, vehicle):
        ...
    def __getVehPostProgressionData(self, vehicle):
        ...
