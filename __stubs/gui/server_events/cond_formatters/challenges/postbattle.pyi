# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/server_events/cond_formatters/challenges/postbattle.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import logging as logging
from constants import ATTACK_REASON as ATTACK_REASON
from dossiers2.custom.records import DB_ID_TO_RECORD as DB_ID_TO_RECORD
from gui.impl import backport as backport
from gui.server_events.cond_formatters import TOP_RANGE_LOWEST as TOP_RANGE_LOWEST
from gui.server_events.cond_formatters.challenges.constants import CHALLENGES_BATTLE_RESULT_ICONS as CHALLENGES_BATTLE_RESULT_ICONS, CONDITION_TEXT_RES as CONDITION_TEXT_RES, DEFAULT_CONDITION_TITLE_TEXT_RES as DEFAULT_CONDITION_TITLE_TEXT_RES, DEFAULT_CONDITION_TEXT_RES as DEFAULT_CONDITION_TEXT_RES, ACHIEVEMENT_TEXT_RES as ACHIEVEMENT_TEXT_RES, ConditionIcon as ConditionIcon, TextResKey as TextResKey, TemplateParam as TemplateParam
from gui.server_events.cond_formatters.challenges.helpers import packDescriptionField as packDescriptionField, packTitleField as packTitleField, getRelationValue as getRelationValue
from gui.server_events.cond_formatters.formatters import SimpleMissionsFormatter as SimpleMissionsFormatter, MissionsBattleConditionsFormatter as MissionsBattleConditionsFormatter
from gui.shared.utils.functions import replaceHyphenToUnderscore as replaceHyphenToUnderscore
from shared_utils import first as first
from helpers import time_utils as time_utils
from gui.server_events.conditions import _Condition as _Condition, _VehsListCondition as _VehsListCondition, BattleResults as BattleResults, Achievements as Achievements
from gui.server_events.cond_formatters import FormattableField as FormattableField
from frameworks.wulf import PyResAccessor as PyResAccessor
_logger: Any

class ChallengePostBattleConditionsFormatter(MissionsBattleConditionsFormatter):
    def __init__(self):
        ...

class ChallengeDefaultFormatter(SimpleMissionsFormatter):
    @classmethod
    def _getTitle(cls, condition):
        ...
    def _getDescription(self, condition):
        ...
    @classmethod
    def _getIconKey(cls, condition=None):
        ...

class ChallengeVehicleListFormatter(ChallengeDefaultFormatter):
    @classmethod
    def _getLabelRes(cls, condition):
        ...
    def _getDescription(self, condition):
        ...

class ChallengeVehicleDamageFormatter(ChallengeVehicleListFormatter):
    @classmethod
    def _getLabelRes(cls, condition):
        ...
    @classmethod
    def _getIconKey(cls, condition=None):
        ...
    @classmethod
    def _getTitle(cls, condition):
        ...

class ChallengeVehicleKillsFormatter(ChallengeVehicleListFormatter):
    @classmethod
    def _getLabelRes(cls, condition):
        ...
    @classmethod
    def _getIconKey(cls, condition=None):
        ...
    @classmethod
    def _getTitle(cls, condition):
        ...

class ChallengeBattleResultsFormatter(ChallengeDefaultFormatter):
    @classmethod
    def _getTitle(cls, condition):
        ...
    def _getDescription(self, condition):
        ...
    @classmethod
    def _getIconKey(cls, condition=None):
        ...
    @staticmethod
    def _processAggregatedKeys(keys):
        ...

class ChallengeAchievementsFormatter(SimpleMissionsFormatter):
    @classmethod
    def _getTitle(cls, condition):
        ...
    def _getDescription(self, condition):
        ...
    @classmethod
    def _getIconKey(cls, condition=None):
        ...
