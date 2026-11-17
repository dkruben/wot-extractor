# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/views/battle_result_view/battle_result_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_result_view.battle_results_tab_model import BattleResultsTabModel as BattleResultsTabModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_result_view.leaderboard_model import LeaderboardModel as LeaderboardModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_royale_event_model import BattleRoyaleEventModel as BattleRoyaleEventModel
from gui.impl.gen.view_models.views.battle_royale.battle_results.br_base_view_model import BrBaseViewModel as BrBaseViewModel

class BattleResultViewModel(BrBaseViewModel):
    __slots__: tuple
    def __init__(self, properties=6, commands=0):
        ...
    @property
    def personalResults(self):
        ...
    @staticmethod
    def getPersonalResultsType():
        ...
    @property
    def leaderboardLobbyModel(self):
        ...
    @staticmethod
    def getLeaderboardLobbyModelType():
        ...
    @property
    def eventInfo(self):
        ...
    @staticmethod
    def getEventInfoType():
        ...
    def getMapName(self):
        ...
    def setMapName(self, value):
        ...
    def _initialize(self):
        ...
