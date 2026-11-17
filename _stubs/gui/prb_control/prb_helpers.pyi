# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/prb_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from future.utils import viewvalues as viewvalues
from gui.shared.badges import buildBadge as buildBadge
from gui.shared.gui_items.badge import BadgeLayouts as BadgeLayouts
from gui.shared.system_factory import collectModeNameKwargsByPrbType as collectModeNameKwargsByPrbType, collectModeNameKwargsByQueueType as collectModeNameKwargsByQueueType
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.game_control import IPlatoonController as IPlatoonController
from constants import MIN_VEHICLE_LEVEL as MIN_VEHICLE_LEVEL, MAX_VEHICLE_LEVEL as MAX_VEHICLE_LEVEL
from gui.impl.lobby.platoon.platoon_config import PREBATTLE_TYPE_TO_VEH_CRITERIA as PREBATTLE_TYPE_TO_VEH_CRITERIA
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
_logger: Any

class BadgesHelper(object):
    __badges: Any
    __prefixBadgeID: Any
    __badgesRawData: Any
    def __init__(self, badges=None):
        ...
    def getBadge(self):
        ...
    def __getBadgeID(self):
        ...
    def __getSelectedBadges(self):
        ...
    def __getBadgeExtraInfo(self):
        ...

class IVehicleAutoSearchHelper(object):
    @classmethod
    def getVehiclesLevelsChecker(cls):
        ...

class DefaultVehicleAutoSearchHelper(IVehicleAutoSearchHelper):
    platoonCtrl: Any
    itemsCache: Any
    @classmethod
    def getVehiclesLevelsChecker(cls):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def _findFirstPrefixBadge(selectedBadges, itemsCache=None):
    ...
def getModeNameKwargs(entityType, isQueue=True):
    ...
