# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/tournaments/match_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel
from comp7.gui.impl.gen.view_models.views.lobby.tournaments.team_model import TeamModel as TeamModel

class MatchState(Enum):
    NOTSTARTED = 'notStarted'
    COMPLETED = 'completed'
    LIVE = 'live'

class MatchStage(Enum):
    ROUNDROBIN = 'roundRobin'
    UBSEMIFINALS = 'UBSemifinals'
    UBFINALS = 'UBFinals'
    LBROUND1 = 'LBRound1'
    LBROUND2 = 'LBRound2'
    LBSEMIFINALS = 'LBSemifinals'
    LBFINALS = 'LBFinals'
    GRANDFINALS = 'grandFinals'

class MatchModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=8, commands=0):
        ...
    @property
    def team1(self):
        ...
    @staticmethod
    def getTeam1Type():
        ...
    @property
    def team2(self):
        ...
    @staticmethod
    def getTeam2Type():
        ...
    def getStartOfMatchTimestamp(self):
        ...
    def setStartOfMatchTimestamp(self, value):
        ...
    def getMatchStage(self):
        ...
    def setMatchStage(self, value):
        ...
    def getBestOf(self):
        ...
    def setBestOf(self, value):
        ...
    def getPhase(self):
        ...
    def setPhase(self, value):
        ...
    def getRound(self):
        ...
    def setRound(self, value):
        ...
    def getMatchState(self):
        ...
    def setMatchState(self, value):
        ...
    def _initialize(self):
        ...
