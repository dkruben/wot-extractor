# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/prestige/global_onboarding_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowFlags as WindowFlags, WindowLayer as WindowLayer
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.prestige.global_onboarding_view_model import GlobalOnboardingViewModel as GlobalOnboardingViewModel
from gui.impl.gen.view_models.views.lobby.prestige.prestige_vehicle_model import PrestigeVehicleModel as PrestigeVehicleModel
from gui.impl.lobby.common.vehicle_model_helpers import fillVehicleModel as fillVehicleModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.prestige.prestige_helpers import fillPrestigeEmblemModel as fillPrestigeEmblemModel, isOnboardingViewed as isOnboardingViewed, setOnboardingViewed as setOnboardingViewed, showPrestigeVehicleStats as showPrestigeVehicleStats
from gui.sounds.filters import switchHangarOverlaySoundFilter as switchHangarOverlaySoundFilter
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle

class GlobalOnboardingView(ViewImpl):
    __slots__: tuple
    __itemsCache: Any
    __lobbyContext: Any
    __settingsCore: Any
    _VEHICLE_PRESTIGE_TOP_COUNT = 3
    __topPrestigeVehIntCD: Any
    def __init__(self, layoutID):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __updateModel(self):
        ...
    def __saveSettings(self):
        ...
    def __onClose(self):
        ...

class GlobalOnboardingWindow(LobbyNotificationWindow):
    __slots__: tuple
    def __init__(self, parent=None):
        ...
