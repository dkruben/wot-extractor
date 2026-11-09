# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/ranked_battles/ranked_builders/widget_vos.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
import logging as logging
import typing as typing
from gui.impl.gen import R as R
from gui.impl import backport as backport
from gui.ranked_battles.ranked_helpers import getBonusMultiplierLabel as getBonusMultiplierLabel
from gui.ranked_battles.ranked_builders import shared_vos as shared_vos
from gui.ranked_battles.ranked_models import Rank as Rank
from gui.Scaleform.genConsts.RANKEDBATTLES_ALIASES import RANKEDBATTLES_ALIASES as RANKEDBATTLES_ALIASES
from gui.shared.formatters import text_styles as text_styles
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
_logger: Any
QualAddVOs: Any
LeagueAddVOs: Any
StateBlock: Any
WidgetPreferences: Any
_NEUTRAL_SEQUENCE_STEPS: dict
_INCREASE_SEQUENCE_STEPS: dict
_INCREASE_SEQUENCE_NEW_STEPS: dict
_DECREASE_SEQUENCE_STEPS: dict
_DECREASE_SEQUENCE_NEW_STEPS: dict
_BONUS_STEPS: dict
_BLOCKS_VOS_BUILDERS: dict

class StepsStatesCollector(object):
    __slots__: tuple
    def getStates(self, rank):
        ...
    def _getSpecializedState(self, state):
        ...
    @staticmethod
    def __getBaseState(rank, step):
        ...

class CustomStepsStatesCollector(StepsStatesCollector):
    __slots__: tuple
    _resultState: Any
    def __init__(self, resultState):
        ...
    def _getSpecializedState(self, state):
        ...

class AcquiredStepsStatesCollector(CustomStepsStatesCollector):
    def _getSpecializedState(self, state):
        ...

class LostStepsStatesCollector(CustomStepsStatesCollector):
    def _getSpecializedState(self, state):
        ...

class _SequencePart(CONST_CONTAINER):
    NOT_IN_CHAIN = 0
    CHAIN_HEAD = 1
    CHAIN_MIDDLE = 2
    CHAIN_TAIL = 3

def getVOsSequence(preferences, stateBlocks, ranks):
    ...
def getQualAddVOs(battlesInQualification, totalQualificationBattles):
    ...
def getLeagueAdditionalVOs(currentEfficiency, currentEfficiencyDiff, currentRating, lastEfficiency=None, lastEfficiencyDiff=None, lastRating=None):
    ...
def _buildInitRankVO(preferences, stateBlock, sequenceState, ranks):
    ...
def _buildDecreaseRankVO(preferences, stateBlock, sequenceState, ranks):
    ...
def _buildIncreaseRankVO(preferences, stateBlock, sequenceState, ranks):
    ...
def _buildSameRankVO(preferences, stateBlock, sequenceState, ranks):
    ...
def _buildDivisionRecieveVO(preferences, stateBlock, sequenceState, ranks):
    ...
def _buildQualificationIdleVO(preferences, stateBlock, sequenceState, ranks):
    ...
def _buildQualificationRecieveVO(preferences, stateBlock, sequenceState, ranks):
    ...
def _buildLeagueRecieveVO(preferences, stateBlock, sequenceState, ranks):
    ...
def _buildLeagueUpdateVO(preferences, stateBlock, sequenceState, ranks):
    ...
def _getStepsVO(rank, preferences, statesCollector=...):
    ...
def _getRankVO(rank, preferences, isEnabled=False):
    ...
def _getQualificationVO(rank):
    ...
def _getDivisionVO(divisionID, newDivisionID):
    ...
def _getLeagueVO(leagueID, efficiencyVO, positionVO, title='', infoText=''):
    ...
def _getBlockVO(preferences, state, infoText='', nextInfoText='', rankLeftVO=None, rankRightVO=None, newRankVO=None, steps=None, newSteps=None, leagueVO=None, newLeagueVO=None, divisionVO=None, finalState=None):
    ...
def _getFinalState(preferences, state, rankLeftVO=None, rankRightVO=None, steps=None):
    ...
def _getBonusBattleState(state):
    ...
def _getBonusStepsLabel():
    ...
def _getInfoTexts(stateBlock):
    ...
def _updateShield(rankVO):
    ...
def _updateSteps(stepsVO):
    ...
