# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/messenger/formatters/service_channel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from future.utils import viewitems as viewitems, viewvalues as viewvalues
from constants import AUTO_MAINTENANCE_RESULT as AUTO_MAINTENANCE_RESULT, AUTO_MAINTENANCE_TYPE as AUTO_MAINTENANCE_TYPE
from last_stand_common.last_stand_constants import ArtefactsSettings as ArtefactsSettings, ProgressPointsSettings as ProgressPointsSettings
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from messenger import g_settings as g_settings
from messenger.formatters.service_channel import ServiceChannelFormatter as ServiceChannelFormatter, BattleResultsFormatter as BattleResultsFormatter, _getRaresAchievementsStrings as _getRaresAchievementsStrings, AutoMaintenanceFormatter as AutoMaintenanceFormatter
from messenger.formatters.service_channel_helpers import MessageData as MessageData
from dossiers2.custom.records import DB_ID_TO_RECORD as DB_ID_TO_RECORD
from dossiers2.ui.layouts import IGNORED_BY_BATTLE_RESULTS as IGNORED_BY_BATTLE_RESULTS
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as ACHIEVEMENT_BLOCK, BADGES_BLOCK as BADGES_BLOCK
from gui.shared.gui_items.dossier.factories import getAchievementFactory as getAchievementFactory
from gui.shared.money import Currency as Currency
from gui.shared.formatters import getBWFormatter as getBWFormatter

class LSProgressPointsFormatter(ServiceChannelFormatter):
    _MSG_KEY = 'lsProgressPointsMessage'
    def format(self, message, *args):
        ...
    def _getMessage(self, isAdded, delta):
        ...

class LSBattleResultsFormatter(BattleResultsFormatter):
    R_SERVICE_CHANNEL_MESSAGES = R.strings.last_stand_system_messages.serviceChannelMessages
    _battleResultKeys: dict
    def _prepareFormatData(self, message):
        ...
    @staticmethod
    def _getBattleTypeDescr(data):
        ...
    @staticmethod
    def _getDifficultyLevel(bonusType):
        ...
    def _getTemplateName(self, data):
        ...
    def __makeBattleResultString(self, lsPhase, lsPhasesCount, isWinner, bonusType):
        ...
    def __makeArtefactString(self, artefacts):
        ...
    def __makeAchievementsAndBadgesStrings(self, battleResults):
        ...

class LSAutoMaintenanceFormatter(AutoMaintenanceFormatter):
    _overriddenMessages: dict
