# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/messenger/formatters/service_channel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from constants import AUTO_MAINTENANCE_RESULT as AUTO_MAINTENANCE_RESULT, AUTO_MAINTENANCE_TYPE as AUTO_MAINTENANCE_TYPE
from gui.shared.notifications import NotificationPriorityLevel as NotificationPriorityLevel
from halloween_common.halloween_constants import ArtefactsSettings as ArtefactsSettings
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from messenger import g_settings as g_settings
from messenger.formatters.service_channel import ServiceChannelFormatter as ServiceChannelFormatter, BattleResultsFormatter as BattleResultsFormatter, _getRaresAchievementsStrings as _getRaresAchievementsStrings, AutoMaintenanceFormatter as AutoMaintenanceFormatter, InvoiceReceivedFormatter as InvoiceReceivedFormatter
from messenger.formatters.service_channel_helpers import MessageData as MessageData
from gui.shared.gui_items.Vehicle import getUserName as getUserName
from items import vehicles as vehicles_core
from dossiers2.custom.records import DB_ID_TO_RECORD as DB_ID_TO_RECORD
from dossiers2.ui.layouts import IGNORED_BY_BATTLE_RESULTS as IGNORED_BY_BATTLE_RESULTS
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as ACHIEVEMENT_BLOCK, BADGES_BLOCK as BADGES_BLOCK
from gui.shared.gui_items.dossier.factories import getAchievementFactory as getAchievementFactory
from gui.shared.money import Currency as Currency
from gui.shared.formatters import getBWFormatter as getBWFormatter

class HWVehicleRentFormatter(ServiceChannelFormatter):
    _MSG_KEY = 'HWVehicleRentMessage'
    def format(self, message, *args):
        ...
    def _getMessage(self, intCD):
        ...

class HWArtefactKeysFormatter(ServiceChannelFormatter):
    _MSG_KEY = 'hwArtefactKeysMessage'
    def format(self, message, *args):
        ...
    def _getMessage(self, isAdded, delta):
        ...

class HWDifficultyLevelFormatter(ServiceChannelFormatter):
    _MSG_KEY = 'hwDifficultyRewardCongrats'
    def format(self, message, *args):
        ...
    def _getMessage(self, isAdded, delta):
        ...

class HalloweenBattleResultsFormatter(BattleResultsFormatter):
    R_SERVICE_CHANNEL_MESSAGES = R.strings.halloween_system_messages.serviceChannelMessages
    _battleResultKeys: dict
    def _prepareFormatData(self, message):
        ...
    @staticmethod
    def _getBattleTypeDescr(data):
        ...
    @staticmethod
    def _getDifficultyLevel(bonusType):
        ...
    def __makeBattleResultString(self, halloweenPhase, halloweenPhasesCount, isWinner):
        ...
    def __makeArtefactString(self, artefacts):
        ...
    def __makeAchievementsAndBadgesStrings(self, battleResults):
        ...

class HWAutoMaintenanceFormatter(AutoMaintenanceFormatter):
    _overriddenMessages: dict

class HWInvoiceReceivedLowPriorityFormatter(InvoiceReceivedFormatter):
    def _getGuiSettings(self, data, key=None, priorityLevel=None, messageType=None, messageSubtype=None, decorator=None):
        ...
