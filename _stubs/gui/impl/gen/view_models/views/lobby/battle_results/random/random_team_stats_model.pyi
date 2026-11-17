# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/random/random_team_stats_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import Array as Array
from gui.impl.gen.view_models.views.lobby.battle_results.random.random_player_model import RandomPlayerModel as RandomPlayerModel
from gui.impl.gen.view_models.views.lobby.battle_results.team_stats_model import TeamStatsModel as TeamStatsModel

class RandomColumnType(Enum):
    SQUAD = 'squad'
    PLAYER = 'player'
    DAMAGE = 'damage'
    FRAG = 'frag'
    XP = 'xp'
    VEHICLE = 'tank'
    MEDAL = 'medal'

class RandomTeamStatsModel(TeamStatsModel):
    __slots__: tuple
    def __init__(self, properties=8, commands=1):
        ...
    def getAllies(self):
        ...
    def setAllies(self, value):
        ...
    @staticmethod
    def getAlliesType():
        ...
    def getEnemies(self):
        ...
    def setEnemies(self, value):
        ...
    @staticmethod
    def getEnemiesType():
        ...
    def getSortingColumn(self):
        ...
    def setSortingColumn(self, value):
        ...
    def _initialize(self):
        ...
