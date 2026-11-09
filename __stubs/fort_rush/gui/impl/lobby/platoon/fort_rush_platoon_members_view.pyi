# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/platoon/fort_rush_platoon_members_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.lobby.platoon.view.platoon_members_view import SquadMembersView as SquadMembersView
from helpers import i18n as i18n

class _PrebattleTypes(Enum):
    FORT_RUSH = 'fort_rush'

class FortRushPlatoonMembersView(SquadMembersView):
    _prebattleType = _PrebattleTypes.FORT_RUSH
    def _onLoading(self):
        ...
    def _onFindPlayers(self):
        ...
    def _getTitle(self):
        ...
    def _getWindowInfoTooltipHeaderAndBody(self):
        ...
