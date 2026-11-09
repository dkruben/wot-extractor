# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/battle_results/comp7_player_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from comp7.gui.impl.gen.view_models.views.lobby.enums import Division as Division, Rank as Rank
from comp7.gui.impl.gen.view_models.views.lobby.battle_results.comp7_stats_efficiency_model import Comp7StatsEfficiencyModel as Comp7StatsEfficiencyModel
from gui.impl.gen.view_models.views.lobby.battle_results.random.random_player_model import RandomPlayerModel as RandomPlayerModel

class Comp7PlayerModel(RandomPlayerModel):
    __slots__: tuple
    NO_PLATOON_SQUAD_INDEX = 0
    SUPER_PLATOON_SQUAD_INDEX = -1
    def __init__(self, properties=17, commands=0):
        ...
    @property
    def efficiencyValues(self):
        ...
    @staticmethod
    def getEfficiencyValuesType():
        ...
    def getIsQualification(self):
        ...
    def setIsQualification(self, value):
        ...
    def getRank(self):
        ...
    def setRank(self, value):
        ...
    def getDivision(self):
        ...
    def setDivision(self, value):
        ...
    def _initialize(self):
        ...
