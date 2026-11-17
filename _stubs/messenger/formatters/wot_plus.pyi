# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/formatters/wot_plus.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from constants import IS_CHINA as IS_CHINA
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.constants.date_time_formats import DateTimeFormatsEnum as DateTimeFormatsEnum
from gui.impl.gen.view_models.views.lobby.page.header.wot_plus_subscription_model import WotPlusPeriodicityEnum as WotPlusPeriodicityEnum
from gui.shared.formatters.date_time import getRegionalDateTime as getRegionalDateTime
from gui.shared.gui_items.Vehicle import getUserName as getUserName
from helpers import dependency as dependency
from items.vehicles import getVehicleType as getVehicleType
from messenger import g_settings as g_settings
from messenger.formatters.service_channel import GeneralFormatter as GeneralFormatter
from messenger.formatters.service_channel import ServiceChannelFormatter as ServiceChannelFormatter
from messenger.formatters.service_channel_helpers import MessageData as MessageData
from renewable_subscription_common.settings_constants import WotPlusTier as WotPlusTier, PRO_THRESHOLD_DAYS as PRO_THRESHOLD_DAYS
from skeletons.gui.game_control import IWotPlusController as IWotPlusController
from messenger.proto.bw.wrappers import ServiceChannelMessage as ServiceChannelMessage
from typing import Dict as Dict, Tuple as Tuple

class WotPlusUnlockedAwardFormatter(GeneralFormatter):
    def __init__(self):
        ...
    def format(self, message, *args):
        ...

class _WotPlusDateTimeFormatter(GeneralFormatter):
    _wotPlusCtrl: Any
    def _getConvertedDateTime(self, dTime):
        ...

class _WotPlusPeriodicityTimeFormatter(_WotPlusDateTimeFormatter):
    def _getPeriodicityMessageText(self, message):
        ...
    def getText(self, message, *args):
        ...

class WotPlusUnlockedFormatter(_WotPlusPeriodicityTimeFormatter):
    def __init__(self):
        ...
    def _getPeriodicityMessageText(self, _):
        ...

class WotPlusCoreUnlockedFormatter(_WotPlusPeriodicityTimeFormatter):
    def __init__(self):
        ...
    def _getPeriodicityMessageText(self, _):
        ...

class WotPlusProUnlockedFormatter(_WotPlusPeriodicityTimeFormatter):
    def __init__(self):
        ...
    def _getPeriodicityMessageText(self, message):
        ...

class WotPlusRenewedFormatter(_WotPlusPeriodicityTimeFormatter):
    def __init__(self):
        ...
    def getTitle(self, message, *args):
        ...
    def getText(self, message, *args):
        ...
    def _getPeriodicityMessageText(self, _):
        ...

class WotPlusUpgradeFormatter(_WotPlusPeriodicityTimeFormatter):
    def __init__(self):
        ...
    def getTitle(self, message, *args):
        ...
    def getText(self, message, *args):
        ...

class WotPlusExpiredFormatter(_WotPlusDateTimeFormatter):
    def __init__(self):
        ...
    def getTitle(self, message, *args):
        ...

class PassiveXpActivatedFormatter(GeneralFormatter):
    def __init__(self):
        ...
    def getText(self, message, *args):
        ...

class PassiveXpDeactivatedFormatter(GeneralFormatter):
    def __init__(self):
        ...
    def getText(self, message, *args):
        ...

class PassiveXpSwitchedFormatter(GeneralFormatter):
    def __init__(self):
        ...
    def getValues(self, message, *args):
        ...

class PassiveXpIncompatibleCrewFormatter(GeneralFormatter):
    def __init__(self):
        ...
    def getValues(self, message, *args):
        ...

class PassiveXPDeactivateDueToPostProgressionFormatter(GeneralFormatter):
    def __init__(self):
        ...
    def getValues(self, message, *args):
        ...

class ProBoostActivatedFormatter(GeneralFormatter):
    def __init__(self):
        ...
    def getValues(self, message, *args):
        ...

class ProBoostDeactivatedFormatter(GeneralFormatter):
    def __init__(self):
        ...
    def getValues(self, message, *args):
        ...

class ProBoostSwitchFormatter(GeneralFormatter):
    def __init__(self):
        ...
    def getValues(self, message, *args):
        ...

class WotPlusSwitchFormatter(ServiceChannelFormatter):
    def format(self, template, *args):
        ...

def getVehicleNameFromVehicleCD(message, messageDataKey):
    ...
