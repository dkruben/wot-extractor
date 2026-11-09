# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/battle_results/components/comp7_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7.gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as COMP7_TOOLTIPS
from comp7.gui.impl.gen.view_models.views.lobby.enums import SeasonName as SeasonName
from comp7.gui.impl.gen.view_models.views.lobby.qualification_battle import BattleState as BattleState
from comp7.gui.impl.lobby.comp7_helpers import comp7_shared as comp7_shared, comp7_i18n_helpers as comp7_i18n_helpers
from comp7_core.gui.impl.lobby.comp7_core_helpers import comp7_core_model_helpers as comp7_core_model_helpers
from comp7_core.gui.battle_results.components.comp7_core_components import checkIfDeserter as checkIfDeserter
from comp7_ranks_common import EXTRA_RANK_TAG as EXTRA_RANK_TAG
from fairplay_violation_types import FairplayViolations as FairplayViolations
from gui.Scaleform.genConsts.COMP7_CONSTS import COMP7_CONSTS as COMP7_CONSTS
from gui.battle_results.components import base as base
from gui.battle_results.settings import PLAYER_TEAM_RESULT as PLAYER_TEAM_RESULT
from gui.impl import backport as backport
from gui.impl.gen.resources import R as R
from gui.shared.formatters import text_styles as text_styles
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7Controller as IComp7Controller

class PrestigePointsBlock(base.StatsBlock):
    __slots__: tuple
    isVisible: Any
    value: Any
    label: Any
    tooltip: Any
    def __init__(self, meta=None, field='', *path):
        ...
    def setRecord(self, result, reusable, tooltip=...):
        ...

class TournamentRatingPointsBlock(PrestigePointsBlock):
    def setRecord(self, result, reusable):
        ...

class TrainingRatingPointsBlock(PrestigePointsBlock):
    isVisible: Any
    value: Any
    label: Any
    tooltip: Any
    def setRecord(self, result, reusable):
        ...

class IsDeserterFlag(base.StatsItem):
    def _convert(self, value, reusable):
        ...

class Comp7RankBlock(base.StatsBlock):
    __slots__: tuple
    __comp7Controller: Any
    linkage: Any
    title: Any
    descr: Any
    icon: Any
    ratingDiff: Any
    hasProgressBar: Any
    progressBegin: Any
    progressCurrent: Any
    progressTotal: Any
    ratingTotal: Any
    def __init__(self, meta=None, field='', *path):
        ...
    def setRecord(self, result, reusable):
        ...
    def __setQualificationData(self, avatarResults, reusable):
        ...
    def __setProgressionData(self, avatarResults):
        ...
    @classmethod
    def __getDescription(cls, achievedRating, division):
        ...
    @staticmethod
    def __getTitle(division, prevDivision):
        ...
    @staticmethod
    def __getRatingDiff(achievedRating):
        ...
    @staticmethod
    def __getQualificationTitle():
        ...
    @staticmethod
    def __getQualificationDescription(teamResult, isDeserter, battleNumber):
        ...
    @staticmethod
    def __getQualificationIcon(teamResult, isDeserter):
        ...

def isQualificationBattle(avatarResults):
    ...
def getFormattedRating(rating):
    ...
