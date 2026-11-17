# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/battle_control/controllers/repositories.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7_core.gui.battle_control.controllers.appearance_cache_ctrls.comp7_appearance_cache_ctrl import Comp7AppearanceCacheController as Comp7AppearanceCacheController
from comp7_core.gui.battle_control.controllers.comp7_vehicle_ban_ctrl import Comp7VehicleBanController as Comp7VehicleBanController
from comp7_core.gui.battle_control.controllers.comp7_voip_ctrl import Comp7VOIPController as Comp7VOIPController
from comp7_core.gui.battle_control.controllers.sound_ctrls.comp7_battle_sounds import Comp7BattleSoundController as Comp7BattleSoundController
from gui.battle_control.controllers.prebattle_setup_ctrl import PrebattleSetupController as PrebattleSetupController
from gui.battle_control.controllers.repositories import ClassicControllersRepository as ClassicControllersRepository
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7Controller as IComp7Controller

class Comp7ControllerRepository(ClassicControllersRepository):
    __slots__: tuple
    __comp7Controller: Any
    @classmethod
    def create(cls, setup):
        ...
    @staticmethod
    def _getAppearanceCacheController(setup):
        ...
