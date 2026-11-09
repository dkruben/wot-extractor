# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/flag/flag_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.battle_results.postbattle_achievement_model import PostbattleAchievementModel as PostbattleAchievementModel
from gui.impl.gen.view_models.views.lobby.common.router_model import RouterModel as RouterModel

class FlagViewModel(ViewModel):
    __slots__: tuple
    WIN = 'win'
    DRAW = 'tie'
    LOSE = 'lose'
    def __init__(self, properties=3, commands=0):
        ...
    @property
    def router(self):
        ...
    @staticmethod
    def getRouterType():
        ...
    def getWinStatus(self):
        ...
    def setWinStatus(self, value):
        ...
    def getAchievements(self):
        ...
    def setAchievements(self, value):
        ...
    @staticmethod
    def getAchievementsType():
        ...
    def _initialize(self):
        ...
