# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/tournaments/wci_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/lobby/tournaments/wci_view.py
from __future__ import absolute_import
from comp7.gui.impl.gen.view_models.views.lobby.tournaments.match_model import MatchStage
from comp7.gui.impl.lobby.tournaments.tournament_view import TournamentView
from helpers.ingame_tournament_helper import IngameTournamentType
from gui.impl.gen import R

class WciView(TournamentView):
    _TOURNAMENT_TYPE = IngameTournamentType.WCI
    _TOURNAMENT_VIEW = R.views.comp7.mono.lobby.tournaments.wci_view()
    _MATCH_ROUND_TO_MATCH_STAGE = {2: (MatchStage.UBSEMIFINALS), 
       1: (MatchStage.UBFINALS), 
       0: (MatchStage.GRANDFINALS), 
       (-4): (MatchStage.LBROUND1), 
       (-3): (MatchStage.LBROUND2), 
       (-2): (MatchStage.LBSEMIFINALS), 
       (-1): (MatchStage.LBFINALS)}
