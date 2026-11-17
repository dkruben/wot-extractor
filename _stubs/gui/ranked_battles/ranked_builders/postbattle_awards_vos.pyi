# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/ranked_battles/ranked_builders/postbattle_awards_vos.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import namedtuple as namedtuple
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.ranked_battles.ranked_builders import shared_vos as shared_vos
from gui.ranked_battles.ranked_helpers import getBonusBattlesIncome as getBonusBattlesIncome, isQualificationQuestID as isQualificationQuestID, getQualificationBattlesCountFromID as getQualificationBattlesCountFromID
from gui.Scaleform.genConsts.RANKEDBATTLES_ALIASES import RANKEDBATTLES_ALIASES as RANKEDBATTLES_ALIASES
from gui.shared.formatters import text_styles as text_styles, icons as icons
from gui.shared.utils.functions import makeTooltip as makeTooltip
from gui.ranked_battles.ranked_models import Rank as Rank, PostBattleRankInfo as PostBattleRankInfo
AwardBlock: Any

def getVOsSequence(awardBlocks, ranks, rankedInfo):
    ...
def _getRankCongVO(awardBlock, rank):
    ...
def _getQualificationQuestCongVO(awardBlock):
    ...
def _getQualificationCongVO(awardBlock, ranks, rankedInfo):
    ...
def _getDivisionCongVO(awardBlock, ranks, rankedInfo):
    ...
def _getLeagueCongVO(rankedInfo):
    ...
def _getQualificationVO(division, newDivision):
    ...
def _getDivisionVO(division, newDivision):
    ...
def _getBonusBattleFields(stepsBonus, efficiencyBonus, isDaily):
    ...
def _getBonusBattlesDiffLabel(bonusBattlesDiff):
    ...
def _getBonusBattlesTooltip(stepsBonus, efficiencyBonus, isDaily):
    ...
def _getBlockVO(state, subTitle='', rankVO=None, qualificationVO=None, divisionVO=None, awards=None, bonusBattleText='', bonusBattleTooltip=''):
    ...
