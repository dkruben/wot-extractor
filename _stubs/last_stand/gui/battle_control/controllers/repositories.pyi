# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/battle_control/controllers/repositories.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from last_stand.skeletons.ls_controller import ILSController as ILSController
from gui.battle_control.controllers import battle_field_ctrl as battle_field_ctrl, debug_ctrl as debug_ctrl, team_bases_ctrl as team_bases_ctrl, default_maps_ctrl as default_maps_ctrl, perk_ctrl as perk_ctrl, personal_death_zones_gui_ctrl as personal_death_zones_gui_ctrl
from gui.battle_control.controllers.battle_hints import controller as battle_hints_ctrl
from gui.battle_control.controllers.repositories import ControllersRepositoryByBonuses as ControllersRepositoryByBonuses, SharedControllersRepository as SharedControllersRepository
from gui.battle_control.controllers.sound_ctrls.common import ShotsResultSoundController as ShotsResultSoundController
from last_stand.gui.battle_control.controllers import appearance_cache_ctrl as appearance_cache_ctrl
from last_stand.gui.battle_control.controllers import battle_gui_controller as battle_gui_controller
from last_stand.gui.battle_control.controllers import voip_ctrl as voip_ctrl
from last_stand.gui.battle_control.controllers.chat_cmd_ctrl import LSChatCommandsController as LSChatCommandsController
from helpers import dependency as dependency
from gui.battle_control import BattleSessionSetup as BattleSessionSetup
from gui.battle_control.controllers import _ControllersRepository as _ControllersRepository

class LastStandSharedControllersRepository(SharedControllersRepository):
    @classmethod
    def getChatCommandsController(cls, setup, feedback, ammo):
        ...

class LastStandControllerRepository(ControllersRepositoryByBonuses):
    __slots__: tuple
    _lsCtrl: Any
    @classmethod
    def create(cls, setup):
        ...
