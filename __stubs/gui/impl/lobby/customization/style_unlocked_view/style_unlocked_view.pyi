# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/customization/style_unlocked_view/style_unlocked_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import WWISE as WWISE
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from frameworks.wulf import ViewSettings as ViewSettings
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.customization.shared import isVehicleCanBeCustomized as isVehicleCanBeCustomized
from gui.impl import backport as backport
from gui.impl.gen.view_models.views.lobby.customization.style_unlocked_view.style_unlocked_view_model import StyleUnlockedViewModel as StyleUnlockedViewModel
from gui.impl.lobby.customization.shared import goToC11nStyledMode as goToC11nStyledMode
from gui.impl.lobby.progressive_reward.progressive_award_sounds import ProgressiveRewardSoundEvents as ProgressiveRewardSoundEvents
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.impl.gen import R as R
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.Scaleform.daapi.view.lobby.customization.sound_constants import SOUNDS as SOUNDS
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from helpers import dependency as dependency, int2roman as int2roman
from items.components.c11n_constants import UNBOUND_VEH_KEY as UNBOUND_VEH_KEY
from gui.shared.system_factory import collectCustomizationHangarDecorator as collectCustomizationHangarDecorator
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.shared import IItemsCache as IItemsCache
from soft_exception import SoftException as SoftException

class StyleUnlockedView(ViewImpl):
    c11nService: Any
    itemsCache: Any
    __vehicle: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _onLoading(self, vehicleCD):
        ...
    def _updateC11nButton(self, *_):
        ...
    def _addListeners(self):
        ...
    def _removeListeners(self):
        ...
    def __setVehicleInfo(self, model):
        ...
    def __onVisibleRouteChanged(self, routeInfo):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateC11nButton(self, lock=False, model=None):
        ...
    def __isCustEnabledForActiveVehicle(self):
        ...
    def __onOkClick(self):
        ...
    def __onAnimationSound(self):
        ...
    def __onShowC11nClick(self):
        ...

class StyleUnlockedWindow(LobbyNotificationWindow):
    def __init__(self, vehicleCD):
        ...
