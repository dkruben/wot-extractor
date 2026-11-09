# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/battle_control/controllers/repositories.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frontline.gui.battle_control.controllers import frontline_respawn_ctrl as frontline_respawn_ctrl
from frontline.gui.battle_control.controllers.appearance_cache_ctrls.frontline_appearance_cache_ctrl import FLAppearanceCacheController as FLAppearanceCacheController
from gui.battle_control.controllers import battle_field_ctrl as battle_field_ctrl, debug_ctrl as debug_ctrl, dyn_squad_functional as dyn_squad_functional, progress_circle_ctrl as progress_circle_ctrl, epic_maps_ctrl as epic_maps_ctrl, epic_missions_ctrl as epic_missions_ctrl, game_notification_ctrl as game_notification_ctrl, epic_team_bases_ctrl as epic_team_bases_ctrl, perk_ctrl as perk_ctrl
from gui.battle_control.controllers.battle_hints import controller as battle_hints_ctrl
from gui.battle_control.controllers.repositories import _ControllersRepository as _ControllersRepository, registerBattleControllerRepo as registerBattleControllerRepo
from gui.battle_control.controllers.sound_ctrls.epic_battle_sounds import EpicShotsResultSoundsController as EpicShotsResultSoundsController
from constants import ARENA_GUI_TYPE as ARENA_GUI_TYPE

class FLControllersRepository(_ControllersRepository):
    __slots__: tuple
    @staticmethod
    def _getAppearanceCacheController(setup):
        ...
    @classmethod
    def create(cls, setup):
        ...

def registerFLBattleRepositories():
    ...
