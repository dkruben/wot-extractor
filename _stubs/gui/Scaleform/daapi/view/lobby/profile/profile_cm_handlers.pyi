# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/profile/profile_cm_handlers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity as EventSystemEntity
from gui.Scaleform.framework.managers.context_menu import AbstractContextMenuHandler as AbstractContextMenuHandler
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.shared import event_dispatcher as shared_events
from helpers import dependency as dependency
from skeletons.gui.game_control import IVehicleComparisonBasket as IVehicleComparisonBasket
from skeletons.gui.shared import IItemsCache as IItemsCache

class PROFILE(object):
    VEHICLE_COMPARE = 'profileVehicleCompare'
    VEHICLE_INFO = 'profileVehicleInfo'

class ProfileVehicleCMHandler(AbstractContextMenuHandler, EventSystemEntity):
    itemsCache: Any
    comparisonBasket: Any
    __vehCD: Any
    def __init__(self, cmProxy, ctx=None):
        ...
    def compareVehicle(self):
        ...
    def showVehicleInfo(self):
        ...
    def _generateOptions(self, ctx=None):
        ...
    def _initFlashValues(self, ctx):
        ...
