# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/battle_control/controllers/repository.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from battle_royale.gui.battle_control.controllers.battle_royale_voip_ctrl import BRVOIPController as BRVOIPController
from battle_royale.gui.battle_control.controllers.notification_manager import NotificationManager as NotificationManager
from gui.battle_control.controllers import battle_field_ctrl as battle_field_ctrl, debug_ctrl as debug_ctrl, default_maps_ctrl as default_maps_ctrl, perk_ctrl as perk_ctrl
from gui.battle_control.controllers.battle_hints import controller as battle_hints_ctrl
from gui.battle_control.controllers.repositories import _ControllersRepository as _ControllersRepository, registerBattleControllerRepo as registerBattleControllerRepo
from gui.battle_control.controllers.sound_ctrls.common import ShotsResultSoundController as ShotsResultSoundController
from battle_royale.gui.battle_control.controllers import spawn_ctrl as spawn_ctrl, vehicles_count_ctrl as vehicles_count_ctrl, radar_ctrl as radar_ctrl, progression_ctrl as progression_ctrl, death_ctrl as death_ctrl
from battle_royale.gui.battle_control.controllers.battle_royale_appearance_cache_ctrl import BattleRoyaleAppearanceCacheController as BattleRoyaleAppearanceCacheController
from constants import ARENA_GUI_TYPE as ARENA_GUI_TYPE

class BattleRoyaleControllersRepository(_ControllersRepository):
    __slots__: tuple
    @classmethod
    def create(cls, setup):
        ...

def registerBRBattleRepo():
    ...
