# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/ranked_battles/ranked_builders/shared_vos.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from gui.Scaleform.genConsts.RANKEDBATTLES_ALIASES import RANKEDBATTLES_ALIASES as RANKEDBATTLES_ALIASES
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.ranked_battles import ranked_formatters as ranked_formatters
from gui.ranked_battles.ranked_helpers import getShieldSizeByRankSize as getShieldSizeByRankSize, makeStatTooltip as makeStatTooltip
from gui.shared.formatters import text_styles as text_styles, icons as icons
from gui.ranked_battles.ranked_models import Division as Division, Rank as Rank
_logger: Any
__ANIMATION_DATA_FIELDS: list

def buildRankVO(rank, isEnabled=False, hasTooltip=False, shieldStatus=None, shieldAnimated=False, showUnburnable=False, imageSize=...):
    ...
def buildRankTooltipVO(rank, imageSize):
    ...
def getDivisionVO(division):
    ...
def getEfficiencyVO(currentSeasonEfficiency, currentSeasonEfficiencyDiff):
    ...
def getRatingVO(rating):
    ...
def getStatVO(value, statKey, iconKey, tooltipKey):
    ...
def _getShieldVO(imageSize, shieldStatus, shieldAnimated):
    ...
def _getUnburnableVO(imageSize):
    ...
def _getUnburnableIcon(rank, imageSize):
    ...
