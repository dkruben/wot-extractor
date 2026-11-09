# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/elite_window/elite_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import SoundGroups as SoundGroups
from account_helpers.settings_core.settings_constants import OnceOnlyHints as OnceOnlyHints
from frameworks.wulf import ViewSettings as ViewSettings
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.impl import backport as backport
from gui.impl.auxiliary.vehicle_helper import fillVehicleInfo as fillVehicleInfo
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.elite_window.elite_view_model import EliteViewModel as EliteViewModel, WindowType as WindowType
from gui.prestige.prestige_helpers import hasVehiclePrestige as hasVehiclePrestige, fillPrestigeEmblemModel as fillPrestigeEmblemModel, getVehiclePrestige as getVehiclePrestige
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.shared import events as events, g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.event_dispatcher import showVehPostProgressionView as showVehPostProgressionView, showVehicleHubVehSkillTreePrestige as showVehicleHubVehSkillTreePrestige
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.veh_post_progression.sounds import Sounds as Sounds
from helpers import dependency as dependency
from shared_utils import first as first
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from skeletons.gui.shared import IItemsCache as IItemsCache

class EliteView(ViewImpl):
    __itemsCache: Any
    __guiLoader: Any
    __settingsCore: Any
    __slots__: tuple
    __vehicle: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, vehicleCD, *args, **kwargs):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def _finalize(self):
        ...
    def __onClose(self):
        ...
    def __onGoToProgression(self):
        ...
    def __markAsVisitedHintInResearch(self):
        ...
    def __onSyncCompleted(self, reason, diff):
        ...
    def __isSkillTreeProgression(self):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateWindowType(self, model=None):
        ...

class EliteWindow(LobbyNotificationWindow):
    __slots__: tuple
    def __init__(self, vehicleCD):
        ...
