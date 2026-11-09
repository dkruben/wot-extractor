# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/battle_royale/battle_results/br_base_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.views.battle_royale.battle_results.leaderboard.leaderboard_model import LeaderboardModel as LeaderboardModel
from gui.impl.gen.view_models.views.battle_royale.battle_results.player_battle_type_status_model import PlayerBattleTypeStatusModel as PlayerBattleTypeStatusModel

class BrBaseViewModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=2, commands=0):
        ...
    @property
    def leaderboardModel(self):
        ...
    @staticmethod
    def getLeaderboardModelType():
        ...
    @property
    def playerBattleTypeStatus(self):
        ...
    @staticmethod
    def getPlayerBattleTypeStatusType():
        ...
    def _initialize(self):
        ...
