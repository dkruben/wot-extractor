# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/cyberSport/CyberSportIntroView.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from helpers import dependency as dependency
from helpers.i18n import makeString as _ms
from account_helpers.AccountSettings import SELECTED_INTRO_VEHICLES_FIELD as SELECTED_INTRO_VEHICLES_FIELD
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.shared import events as events
from gui.shared.gui_items.Vehicle import VEHICLE_CLASS_NAME as _VCN
from gui.shared.events import CSVehicleSelectEvent as CSVehicleSelectEvent
from gui.shared.event_bus import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.formatters import text_styles as text_styles
from gui.Scaleform.daapi.view.lobby.rally.vo_converters import makeIntroVehicleVO as makeIntroVehicleVO
from gui.Scaleform.daapi.view.meta.CyberSportIntroMeta import CyberSportIntroMeta as CyberSportIntroMeta
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.Scaleform.locale.CYBERSPORT import CYBERSPORT as CYBERSPORT
from gui.Scaleform.genConsts.CYBER_SPORT_ALIASES import CYBER_SPORT_ALIASES as CYBER_SPORT_ALIASES
from nation_change.nation_change_helpers import iterVehTypeCDsInNationGroup as iterVehTypeCDsInNationGroup
from nation_change_helpers.client_nation_change_helper import getValidVehicleCDForNationChange as getValidVehicleCDForNationChange
from skeletons.gui.shared import IItemsCache as IItemsCache
_ACCEPTED_VEH_TYPES: tuple

class _IntroViewVO(object):
    __data: Any
    def __init__(self):
        ...
    def getData(self):
        ...
    def showCreateButton(self, label, tooltip, enabled=True):
        ...
    def moveToTheUnitByCreateButton(self):
        ...
    def needAddPlayers(self):
        ...
    def fillDefault(self):
        ...

class CyberSportIntroView(CyberSportIntroMeta):
    itemsCache: Any
    _currentVehCD: Any
    def showSelectorPopup(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __checkSelectedVehicles(self):
        ...
    def __onCacheResync(self, reason, diff):
        ...
    def __updateSelectedVehicles(self, event):
        ...
    def __setSelectedVehicle(self, vehIntCD):
        ...
    def __updateAutoSearchVehicle(self, vehsIntCD):
        ...
    def __getSelectedVehicles(self):
        ...
