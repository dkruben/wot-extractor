# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/dialogs/wot_plus/subscription_award_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
from typing import TYPE_CHECKING as TYPE_CHECKING, List as List, Dict as Dict
import WWISE as WWISE
from chat_shared import SYS_MESSAGE_TYPE as SYS_MESSAGE_TYPE
from constants import IS_CHINA as IS_CHINA
from gui.Scaleform.daapi.view.lobby.wot_plus.sound_constants import SOUNDS as SOUNDS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.constants.date_time_formats import DateTimeFormatsEnum as DateTimeFormatsEnum
from gui.impl.gen.view_models.views.dialogs.mono_dialog_template_button_model import ButtonType as ButtonType
from gui.impl.gen.view_models.views.dialogs.mono_dialog_template_view_model import MonoDialogTemplateViewModel as MonoDialogTemplateViewModel
from gui.impl.gen.view_models.views.lobby.page.header.wot_plus_subscription_model import WotPlusPeriodicityEnum as WotPlusPeriodicityEnum
from gui.impl.lobby.dialogs.wot_plus.base_dialog import BaseDialog as BaseDialog
from gui.server_events.bonuses_wot_plus import getAvailableCoreBonuses as getAvailableCoreBonuses, getUniqueAvailableProBonuses as getUniqueAvailableProBonuses
from gui.shared.event_dispatcher import showWotPlusInfoPage as showWotPlusInfoPage
from gui.shared.formatters.date_time import getRegionalDateTime as getRegionalDateTime
from gui.shared.missions.packers.bonus import getDefaultBonusPacker as getDefaultBonusPacker
from helpers import dependency as dependency
from messenger.m_constants import SCH_CLIENT_MSG_TYPE as SCH_CLIENT_MSG_TYPE
from renewable_subscription_common.settings_constants import WotPlusTier as WotPlusTier, PRO_THRESHOLD_DAYS as PRO_THRESHOLD_DAYS
from renewable_subscription_common.settings_helpers import SubscriptionSettingsStorage as SubscriptionSettingsStorage
from skeletons.gui.game_control import IWotPlusController as IWotPlusController
from skeletons.gui.system_messages import ISystemMessages as ISystemMessages
from uilogging.wot_plus.logging_constants import WotPlusInfoPageSource as WotPlusInfoPageSource
from gui.server_events.bonuses import WoTPlusBonus as WoTPlusBonus
from gui.Scaleform.SystemMessagesInterface import SystemMessagesInterface as SystemMessagesInterface
from gui.game_control.wot_plus_controller import WotPlusController as WotPlusController
BG_IMAGE_RESOURCE_BY_TIER: dict
PERIODICITY_TO_RESOURCE: dict

class SubscriptionAwardDialog(BaseDialog):
    LAYOUT_ID: Any
    _systemMessages: Any
    _wotPlusCtrl: Any
    _unlockedTier: Any
    _storage: Any
    _expirationTime: Any
    _messageType: Any
    BACKGROUND_IMAGE: Any
    _periodicity: Any
    def __init__(self, unlockedTier, expirationTime, billingDays, messageType, *args, **kwargs):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _buildContentParams(self, unlockedTier):
        ...
    def _buildResourcesParams(self, unlockedTier):
        ...
    def __buildWotPlusCoreContent(self):
        ...
    def __buildWotPlusProContent(self):
        ...
    def __buildWotPlusCoreResources(self):
        ...
    def __buildWotPlusProResources(self):
        ...
    def __buildBenefits(self, benefitsList):
        ...
    def _setButtons(self):
        ...
    def _onInfo(self):
        ...
    def _sendNotificationsOnClose(self):
        ...
    def _onAction(self, event):
        ...
