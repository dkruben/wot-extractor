# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/gen/view_models/views/lobby/battle_results/comp7_light_team_stats_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import Array as Array
from comp7_light.gui.impl.gen.view_models.views.lobby.battle_results.comp7_light_player_model import Comp7LightPlayerModel as Comp7LightPlayerModel
from gui.impl.gen.view_models.views.lobby.battle_results.team_stats_model import TeamStatsModel as TeamStatsModel

class Comp7LightColumnType(Enum):
    SQUAD = 'squad'
    PLAYER = 'player'
    DAMAGE = 'damage'
    FRAG = 'frag'
    XP = 'xp'
    VEHICLE = 'tank'
    MEDAL = 'medal'
    PRESTIGEPOINTS = 'prestigePoints'

class Comp7LightTeamStatsModel(TeamStatsModel):
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
