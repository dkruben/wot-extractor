# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/bonus_packers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import logging as logging
from typing import TYPE_CHECKING as TYPE_CHECKING
from gui.impl import backport as backport
from gui.impl.backport import createTooltipData as createTooltipData
from gui.impl.gen import R as R
from gui.impl.gen.view_models.common.missions.bonuses.token_bonus_model import TokenBonusModel as TokenBonusModel
from gui.shared.missions.packers.bonus import BonusUIPacker as BonusUIPacker, TokenBonusUIPacker as TokenBonusUIPacker, getDailyMissionsMapping as getDailyMissionsMapping
from gui.shared.utils.functions import makeTooltip as makeTooltip
from helpers import dependency as dependency
from fort_rush.skeletons.battle_controller import IFortRushBattleController as IFortRushBattleController
from gui.impl.backport.backport_tooltip import TooltipData as TooltipData
from gui.server_events.bonuses import TokensBonus as TokensBonus
from typing import Any as Any
_logger: _Any

class FortRushTokenBonusUIPacker(TokenBonusUIPacker):
    _FORT_RUSH_PROGRESSION_TOKEN_SOURCE = 'fort_rush_points'
    __ctrl: _Any
    @classmethod
    def _getTokenBonusType(cls, tokenID, complexToken):
        ...
    @classmethod
    def _getTokenBonusPackers(cls):
        ...
    @classmethod
    def _getTooltipsPackers(cls):
        ...
    @classmethod
    def __packProgressionToken(cls, model, bonus, complexToken, token):
        ...
    @classmethod
    def __getProgressionTokenTooltip(cls, *_):
        ...

def getFortRushMissionBonusPacker():
    ...
