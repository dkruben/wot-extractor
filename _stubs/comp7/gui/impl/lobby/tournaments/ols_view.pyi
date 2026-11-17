# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/tournaments/ols_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7.gui.impl.gen.view_models.views.lobby.tournaments.match_model import MatchStage as MatchStage
from comp7.gui.impl.lobby.tournaments.tournament_view import TournamentView as TournamentView
from helpers.ingame_tournament_helper import IngameTournamentType as IngameTournamentType
from gui.impl.gen import R as R
from comp7.gui.shared import event_dispatcher as event_dispatcher

class OlsView(TournamentView):
    _TOURNAMENT_TYPE = IngameTournamentType.OLS
    _TOURNAMENT_VIEW: Any
    _MATCH_ROUND_TO_MATCH_STAGE: dict
    def _onGoToTokenStore(self):
        ...
