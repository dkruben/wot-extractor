# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/random/random_player_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import Array as Array
from gui.impl.gen.view_models.common.account_model import AccountModel as AccountModel
from gui.impl.gen.view_models.views.lobby.battle_results.player_model import PlayerModel as PlayerModel
from gui.impl.gen.view_models.views.lobby.battle_results.postbattle_achievement_model import PostbattleAchievementModel as PostbattleAchievementModel
from gui.impl.gen.view_models.views.lobby.battle_results.random.random_user_status_model import RandomUserStatusModel as RandomUserStatusModel

class RandomPlayerModel(PlayerModel):
    __slots__: tuple
    def __init__(self, properties=13, commands=0):
        ...
    @property
    def userNames(self):
        ...
    @staticmethod
    def getUserNamesType():
        ...
    @property
    def userStatus(self):
        ...
    @staticmethod
    def getUserStatusType():
        ...
    def getPrebattleID(self):
        ...
    def setPrebattleID(self, value):
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
