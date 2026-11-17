# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/customization/progressive_items_reward/progressive_items_upgrade_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import WWISE as WWISE
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from adisp import adisp_process as adisp_process
from frameworks.wulf import ViewSettings as ViewSettings
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.daapi.view.lobby.customization.shared import getItemInstalledCount as getItemInstalledCount
from gui.Scaleform.daapi.view.lobby.customization.sound_constants import SOUNDS as SOUNDS
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.customization.shared import isVehicleCanBeCustomized as isVehicleCanBeCustomized
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.customization.progressive_items_reward.progressive_items_reward_view_model import ProgressiveItemsRewardViewModel as ProgressiveItemsRewardViewModel
from gui.impl.lobby.customization.shared import goToC11nStyledMode as goToC11nStyledMode
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.processors.common import OutfitApplier as OutfitApplier
from gui.shared.image_helper import getTextureLinkByID as getTextureLinkByID
from helpers import dependency as dependency, int2roman as int2roman
from items.components.c11n_constants import SeasonType as SeasonType, UNBOUND_VEH_KEY as UNBOUND_VEH_KEY
from gui.shared.system_factory import collectCustomizationHangarDecorator as collectCustomizationHangarDecorator
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.shared import IItemsCache as IItemsCache
from soft_exception import SoftException as SoftException
from gui.impl.lobby.progressive_reward.progressive_award_sounds import ProgressiveRewardSoundEvents as ProgressiveRewardSoundEvents

class ProgressiveItemsUpgradeView(ViewImpl):
    __slots__: tuple
    __c11nService: Any
    __itemsCache: Any
    __item: Any
    __vehicle: Any
    __level: Any
    __itemsInNeedToUpgrade: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _onLoading(self, itemCD, vehicleCD, progressionLevel, showSecondButton):
        ...
    def _updateButtons(self, *_):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    def __onVisibleRouteChanged(self, routeInfo):
        ...
    def __setVehicleInfo(self, model):
        ...
    def __setItemInfo(self, model):
        ...
    def __getIcon(self, level):
        ...
    def __setButtons(self, model, showSecondButton=False):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateButtons(self, lock=False, model=None):
        ...
    def __getItemsInNeedToUpgrade(self):
        ...
    def __onOkClick(self):
        ...
    def __onWindowClose(self):
        ...
    def __onApplyClick(self):
        ...
    # decorador original: @adisp_process
    def __upgradeItems(self):
        ...
    def __resetItemNovelty(self):
        ...
    def __onShowC11nClick(self):
        ...

class ProgressiveItemsUpgradeWindow(LobbyNotificationWindow):
    __slots__: tuple
    def __init__(self, itemCD, vehicleCD, progressionLevel, showSecondButton):
        ...
