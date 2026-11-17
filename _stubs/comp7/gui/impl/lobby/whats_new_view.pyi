# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/whats_new_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import SoundGroups as SoundGroups
from comp7.gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as COMP7_TOOLTIPS
from comp7.gui.impl.gen.view_models.views.lobby.enums import SeasonName as SeasonName
from comp7.gui.impl.gen.view_models.views.lobby.season_model import SeasonState as SeasonState
from comp7.gui.impl.gen.view_models.views.lobby.whats_new_view_model import WhatsNewViewModel as WhatsNewViewModel
from comp7.gui.impl.gen.view_models.views.lobby.year_model import YearState as YearState
from comp7.gui.impl.lobby.comp7_helpers.comp7_gui_helpers import updateComp7LastSeason as updateComp7LastSeason
from comp7_core.gui.impl.lobby.comp7_core_helpers import comp7_core_model_helpers as comp7_core_model_helpers
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags, WindowLayer as WindowLayer
from gui import GUI_SETTINGS as GUI_SETTINGS
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow
from gui.impl.backport.backport_tooltip import createTooltipData as createTooltipData
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel as VehicleModel
from gui.impl.lobby.common.vehicle_model_helpers import fillVehicleModel as fillVehicleModel
from gui.impl.lobby.tooltips.vehicle_role_descr_view import VehicleRolesTooltipView as VehicleRolesTooltipView
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.shared.event_dispatcher import showBrowserOverlayView as showBrowserOverlayView
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
SOUND_NAME = 'comp_7_whatsnew_appear'
RENTAL_VEHICLES_CDS: list

class WhatsNewView(ViewImpl, IGlobalListener):
    __slots__: tuple
    __settingsCore: Any
    __comp7Controller: Any
    __itemsCache: Any
    __eventsCache: Any
    def __init__(self, layoutID):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def _calendarDayTooltipID(self):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def onPrbEntitySwitched(self):
        ...
    def _finalize(self):
        ...
    def _onLoading(self, *_, **__):
        ...
    def _onLoaded(self):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    def __onStatusUpdated(self, status):
        ...
    def __onConfigChanged(self):
        ...
    def __onEventsSyncCompleted(self):
        ...
    def __onPollServerTime(self):
        ...
    def __updateData(self):
        ...
    def __setRentalVehicles(self, viewModel):
        ...
    def __onClose(self):
        ...
    def __onVideoOpen(self):
        ...
    @staticmethod
    def __playSound():
        ...
    @staticmethod
    def __getWhatsNewPageKey():
        ...

class WhatsNewViewWindow(LobbyNotificationWindow):
    __slots__: tuple
    def __init__(self, parent=None):
        ...
