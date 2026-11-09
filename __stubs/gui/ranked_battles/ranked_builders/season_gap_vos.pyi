# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/ranked_battles/ranked_builders/season_gap_vos.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
import logging as logging
import typing as typing
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles, icons as icons
from gui.ranked_battles.ranked_builders import shared_vos as shared_vos
from gui.ranked_battles import ranked_formatters as ranked_formatters
from gui.ranked_battles.constants import SeasonGapStates as SeasonGapStates, ZERO_RANK_ID as ZERO_RANK_ID, ZERO_DIVISION_ID as ZERO_DIVISION_ID
from gui.ranked_battles.ranked_helpers.web_season_provider import UNDEFINED_LEAGUE_ID as UNDEFINED_LEAGUE_ID
from gui.Scaleform.genConsts.RANKEDBATTLES_ALIASES import RANKEDBATTLES_ALIASES as RANKEDBATTLES_ALIASES
_logger: Any
StateBlock: Any
_DATA_VOS_BUILDERS: dict

def _buildWaitingVO(_):
    ...
def _buildLeaguesVO(stateBlock):
    ...
def _buildDivisionVO(stateBlock):
    ...
def _buildNotInSeasonVO(stateBlock):
    ...
def _buildQualificationVO(stateBlock):
    ...
def getDataVO(stateBlock):
    ...
def getEfficiencyVO(currentSeasonEfficiency):
    ...
def getRatingVO(rating, isMastered):
    ...
def _getDataVO(state, leagueID=..., divisionID=..., rankID=..., disabled=False, title='', descr='', btnLabel='', btnVisible=False, sprinterImg=''):
    ...
def _addAlertIcon(description):
    ...
