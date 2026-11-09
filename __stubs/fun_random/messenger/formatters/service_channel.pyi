# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/messenger/formatters/service_channel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from fun_random.gui.feature.fun_constants import FunNotificationType as FunNotificationType
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin as FunAssetPacksMixin, FunProgressionWatcher as FunProgressionWatcher, FunSubModesWatcher as FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasActiveProgression as hasActiveProgression, hasSpecifiedSubModes as hasSpecifiedSubModes
from fun_random.notification.decorators import FunRandomNewSubModesMessageDecorator as FunRandomNewSubModesMessageDecorator
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.limited_ui.lui_rules_storage import LUI_RULES as LUI_RULES
from gui.shared.notifications import NotificationPriorityLevel as NotificationPriorityLevel
from helpers import dependency as dependency
from messenger import g_settings as g_settings
from messenger.formatters.service_channel import ServiceChannelFormatter as ServiceChannelFormatter
from messenger.formatters.service_channel_helpers import MessageData as MessageData
from skeletons.gui.game_control import ILimitedUIController as ILimitedUIController
from fun_random.gui.feature.models.notifications import FunNotification as FunNotification
_logger: Any
_INFO_HEADER_TEMPLATE = 'InformationHeaderSysMessage'
_NEW_SUB_MODES_TEMPLATE = 'FunRandomNewSubModes'
_WARNING_HEADER_TEMPLATE = 'WarningHeaderSysMessage'

class FunRandomNotificationsFormatter(ServiceChannelFormatter, FunAssetPacksMixin, FunProgressionWatcher, FunSubModesWatcher):
    __limitedUIController: Any
    __DECORATOR: dict
    __LIMITED_UI: dict
    __PRIORITY: dict
    __TEMPLATE: dict
    def canBeEmpty(self):
        ...
    def format(self, message, *_):
        ...
    @classmethod
    def _getSubModesText(cls, subModesIDs, multipleTextRes, singleTextRes):
        ...
    def _getMessageText(self, notificationType, message):
        ...
    # decorador original: @hasActiveProgression(...)
    def _formatNewProgression(self):
        ...
    # decorador original: @hasSpecifiedSubModes(...)
    def _formatNewSubModes(self, subModesIDs, isNewProgression):
        ...
    # decorador original: @hasSpecifiedSubModes(...)
    def _formatStopSubModes(self, subModesIDs, isNewProgression):
        ...
    # decorador original: @hasSpecifiedSubModes(...)
    def _formatSwitchOnSubModes(self, subModesIDs):
        ...
    # decorador original: @hasSpecifiedSubModes(...)
    def _formatSwitchOffSubModes(self, subModesIDs):
        ...
    def _formatStopAllSubModes(self):
        ...
    def __addProgressionPath(self, textRes, isNewProgression):
        ...
