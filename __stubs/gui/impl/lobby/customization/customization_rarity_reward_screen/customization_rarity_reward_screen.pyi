# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/customization/customization_rarity_reward_screen/customization_rarity_reward_screen.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import SoundGroups as SoundGroups
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowLayer as WindowLayer, WindowFlags as WindowFlags
from gui.impl.gen.view_models.views.lobby.customization.customization_rarity_reward_screen_model import CustomizationRarityRewardScreenModel as CustomizationRarityRewardScreenModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyWindow as LobbyWindow
from gui.impl.gen import R as R
from gui.shared import events as events, g_eventBus as g_eventBus
from gui.shared.event_bus import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.event_dispatcher import showHangar as showHangar
from gui.shared.view_helpers.blur_manager import CachedBlur as CachedBlur
from gui.sounds.filters import switchHangarOverlaySoundFilter as switchHangarOverlaySoundFilter
from helpers import dependency as dependency
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from uilogging.customization_3d_objects.logger import CustomizationRarityRewardViewLogger as CustomizationRarityRewardViewLogger
from uilogging.customization_3d_objects.logging_constants import CustomizationButtons as CustomizationButtons, CustomizationViewKeys as CustomizationViewKeys

class CustomizationRarityRewardScreen(ViewImpl):
    __customizationService: Any
    __lobbyCtx: Any
    __hangarSpace: Any
    __slots__: tuple
    _REWARD_SOUND_ID = 'elements_cust_reward'
    _LAYOUT_ID: Any
    _MODEL = CustomizationRarityRewardScreenModel
    __element: Any
    __isFirstEntry: Any
    __uiLogger: Any
    __sound: Any
    def __init__(self, element, isFirstEntry):
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
    def __onVehicleChanged(self):
        ...
    def __onGoToExterior(self):
        ...
    def __onGoToGarage(self):
        ...
    def __isC11nEnabled(self):
        ...

class CustomizationRarityRewardWindow(LobbyWindow):
    __slots__: tuple
    _blur: Any
    def __init__(self, element, isFirstEntry):
        ...
    def _initialize(self):
        ...
    def _finalize(self):
        ...
