# wot-extractor: STUB (.pyi) gerado a partir de sources/res/open_bundle/scripts/client/open_bundle/gui/impl/lobby/notifications/special_rewards_notification.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
from gui.customization.constants import CustomizationModes as CustomizationModes, CustomizationModeSource as CustomizationModeSource
from helpers import dependency as dependency
from gui.Scaleform.daapi.view.lobby.customization.shared import isC11nEnabled as isC11nEnabled, CustomizationTabs as CustomizationTabs
from gui.Scaleform.daapi.view.lobby.storage.storage_helpers import getVehicleCDForStyle as getVehicleCDForStyle
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.gf_notifications.notification_base import NotificationBase as NotificationBase
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.shared.event_dispatcher import showHangar as showHangar, showStylePreview as showStylePreview, selectVehicleInHangar as selectVehicleInHangar
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from open_bundle.gui.impl.gen.view_models.views.lobby.notifications.special_rewards_notification_model import SpecialRewardsNotificationModel as SpecialRewardsNotificationModel
from open_bundle.helpers.bonuses.bonus_packers import findVehicleCD as findVehicleCD, packBonusModelAndTooltipData as packBonusModelAndTooltipData, composeBonuses as composeBonuses, sortBonuses as sortBonuses
from open_bundle.helpers.bonuses.bonuses_constants import ATTACHMENTS_TOKEN_NAME as ATTACHMENTS_TOKEN_NAME
from open_bundle.skeletons.open_bundle_controller import IOpenBundleController as IOpenBundleController
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.shared import IItemsCache as IItemsCache

class SpecialRewardsNotification(NotificationBase):
    __itemsCache: Any
    __openBundle: Any
    __c11nService: Any
    __allRewards: Any
    def __init__(self, resId, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def bundleID(self):
        ...
    @property
    def cellRewards(self):
        ...
    def _getCallbacks(self):
        ...
    def _getEvents(self):
        ...
    def _update(self):
        ...
    def _canNavigate(self):
        ...
    def __getAllRewards(self):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __fillBonuses(self, model=None):
        ...
    def __onInventoryUpdate(self, *_):
        ...
    # decorador original: @args2params(...)
    def __onShowReward(self, bonusType, bonusId):
        ...
    def __selectVehicle(self, vehicleCD):
        ...
