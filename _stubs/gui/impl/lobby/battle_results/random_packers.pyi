# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_results/random_packers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.battle_results import stored_sorting as stored_sorting
from gui.battle_results.presenters.packers.team.team_stats_packer import TeamStats as TeamStats, TeamAchievementsPacker as TeamAchievementsPacker
from gui.battle_results.presenters.packers.user_info import AccountInfo as AccountInfo, PlayerInfo as PlayerInfo, UserStatus as UserStatus
from gui.impl.gen.view_models.views.lobby.battle_results.random.random_player_model import RandomPlayerModel as RandomPlayerModel
from gui.impl.gen.view_models.views.lobby.battle_results.random.random_team_stats_model import RandomColumnType as RandomColumnType
from gui.impl.gen.view_models.views.lobby.battle_results.team_stats_model import SortingOrder as SortingOrder
from gui.shared.system_factory import collectBattleResultsStatsSorting as collectBattleResultsStatsSorting
from gui.battle_results.stats_ctrl import BattleResults as BattleResults
from gui.impl.gen.view_models.views.lobby.battle_results.random.random_team_stats_model import RandomTeamStatsModel as RandomTeamStatsModel

class RandomPlayerInfo(PlayerInfo):
    __slots__: tuple
    @classmethod
    def packModel(cls, model, battleResults, vehicleSumInfo):
        ...
    @classmethod
    def _packAccountInfo(cls, model, battleResults, vehicleSumInfo):
        ...

class RandomUserStatus(UserStatus):
    _USER_INFO_PACKER = AccountInfo

class RandomTeamEfficiency(TeamStats):
    _PLAYER_MODEL_CLS = RandomPlayerModel
    _PLAYER_INFO_PACKER = RandomPlayerInfo
    @classmethod
    def packModel(cls, model, battleResults):
        ...
    @classmethod
    def _packSortingParams(cls, model, battleResults):
        ...
