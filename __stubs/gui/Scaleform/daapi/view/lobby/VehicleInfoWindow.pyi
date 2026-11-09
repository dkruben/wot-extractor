# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/VehicleInfoWindow.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from future.utils import lzip as lzip
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.Scaleform import MENU as MENU
from gui.Scaleform.daapi.view.meta.VehicleInfoMeta import VehicleInfoMeta as VehicleInfoMeta
from gui.shared.formatters import getRoleTextWithLabel as getRoleTextWithLabel
from gui.shared.items_parameters import formatters as formatters
from gui.shared.utils import AUTO_RELOAD_PROP_NAME as AUTO_RELOAD_PROP_NAME, TURBOSHAFT_ENGINE_POWER as TURBOSHAFT_ENGINE_POWER, TURBOSHAFT_SPEED_MODE_SPEED as TURBOSHAFT_SPEED_MODE_SPEED, TURBOSHAFT_SWITCH_TIME as TURBOSHAFT_SWITCH_TIME, TURBOSHAFT_INVISIBILITY_MOVING_FACTOR as TURBOSHAFT_INVISIBILITY_MOVING_FACTOR, TURBOSHAFT_INVISIBILITY_STILL_FACTOR as TURBOSHAFT_INVISIBILITY_STILL_FACTOR, ROCKET_ACCELERATION_ENGINE_POWER as ROCKET_ACCELERATION_ENGINE_POWER, ROCKET_ACCELERATION_SPEED_LIMITS as ROCKET_ACCELERATION_SPEED_LIMITS, ROCKET_ACCELERATION_REUSE_AND_DURATION as ROCKET_ACCELERATION_REUSE_AND_DURATION, DUAL_ACCURACY_COOLING_DELAY as DUAL_ACCURACY_COOLING_DELAY, SHOT_DISPERSION_ANGLE as SHOT_DISPERSION_ANGLE, AVG_DAMAGE_PER_SECOND as AVG_DAMAGE_PER_SECOND, CONTINUOUS_SHOTS_PER_MINUTE as CONTINUOUS_SHOTS_PER_MINUTE, TWIN_GUN_SWITCH_FIRE_MODE_TIME as TWIN_GUN_SWITCH_FIRE_MODE_TIME, TWIN_GUN_TOP_SPEED as TWIN_GUN_TOP_SPEED, RELOAD_TIME_SECS_PROP_NAME as RELOAD_TIME_SECS_PROP_NAME, TWIN_GUN_RELOAD_TIME as TWIN_GUN_RELOAD_TIME
from gui.shared.utils.role_presenter_helper import getRoleUserName as getRoleUserName
from helpers import i18n as i18n, dependency as dependency
from items.components.crew_skins_constants import NO_CREW_SKIN_ID as NO_CREW_SKIN_ID
from nation_change.nation_change_helpers import iterVehTypeCDsInNationGroup as iterVehTypeCDsInNationGroup
from nation_change_helpers.client_nation_change_helper import getChangeNationTooltip as getChangeNationTooltip
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.game_control import IVehicleComparisonBasket as IVehicleComparisonBasket
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from gui.shared.gui_items.items_actions import factory as ItemsActionsFactory
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import NATION_CHANGE_VIEWED as NATION_CHANGE_VIEWED
from account_helpers.settings_core.ServerSettingsManager import ServerSettingsManager as ServerSettingsManager

class _Highlight(object):
    __slots__: tuple
    __nonzero__: Any
    __highlight: Any
    __checker: Any
    def __init__(self, checker):
        ...
    def __bool__(self):
        ...

class VehicleInfoWindow(VehicleInfoMeta):
    _itemsCache: Any
    _comparisonBasket: Any
    _settingsCore: Any
    _lobbyContext: Any
    __OVERRIDED_PARAM_NAMES: tuple
    __vehicleCompactDescr: Any
    __highlightsMap: Any
    def __init__(self, ctx=None):
        ...
    def onCancelClick(self):
        ...
    def onWindowClose(self):
        ...
    def getVehicleInfo(self):
        ...
    def addToCompare(self):
        ...
    def changeNation(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __packParams(self, paramsList):
        ...
    def __updateCompareButtonState(self):
        ...
    def __onVehCompareBasketChanged(self, changedData):
        ...
    def __updateChangeNationButtonState(self):
        ...
    def __updateNationChangeBtn(self, *args, **kwargs):
        ...

def _highlightsMap(settings, vehicle=None):
    ...
