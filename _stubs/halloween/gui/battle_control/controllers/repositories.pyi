# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/battle_control/controllers/repositories.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.battle_control.controllers import battle_field_ctrl as battle_field_ctrl, debug_ctrl as debug_ctrl, team_bases_ctrl as team_bases_ctrl, default_maps_ctrl as default_maps_ctrl, perk_ctrl as perk_ctrl
from gui.battle_control.controllers.battle_hints import controller as battle_hints_ctrl
from gui.battle_control.controllers.repositories import ControllersRepositoryByBonuses as ControllersRepositoryByBonuses, SharedControllersRepository as SharedControllersRepository
from gui.battle_control.controllers.sound_ctrls.common import ShotsResultSoundController as ShotsResultSoundController
from halloween.gui.battle_control.controllers import appearance_cache_ctrl as appearance_cache_ctrl
from halloween.gui.battle_control.controllers import battle_gui_controller as battle_gui_controller
from halloween.gui.battle_control.controllers import personal_death_zones_gui_ctrl as personal_death_zones_gui_ctrl
from halloween.gui.battle_control.controllers import arena_border_ctrl as arena_border_ctrl

class HalloweenControllerRepository(ControllersRepositoryByBonuses):
    __slots__: tuple
    @classmethod
    def create(cls, setup):
        ...

class HalloweenSharedControllersRepository(SharedControllersRepository):
    @classmethod
    def getArenaBorderController(cls):
        ...
