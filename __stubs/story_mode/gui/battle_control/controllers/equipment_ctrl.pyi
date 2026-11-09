# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/battle_control/controllers/equipment_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import SoundGroups as SoundGroups
from typing import Tuple as Tuple, Optional as Optional, TYPE_CHECKING as TYPE_CHECKING
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control.controllers.consumables import equipment_ctrl as equipment_ctrl
from gui.battle_control.controllers.consumables.equipment_ctrl import EquipmentsReplayPlayer as EquipmentsReplayPlayer
from story_mode.gui.story_mode_gui_constants import ABILITY_ON_COOLDOWN_ACTIVATION_ERROR_KEY as ABILITY_ON_COOLDOWN_ACTIVATION_ERROR_KEY
from story_mode.gui.sound_constants import ABILITY_CANT_ACTIVATE_SOUND as ABILITY_CANT_ACTIVATE_SOUND, ABILITY_ON_COOLDOWN_SOUND as ABILITY_ON_COOLDOWN_SOUND
from story_mode_common.story_mode_constants import RECON_ABILITY as RECON_ABILITY, EQUIPMENT_STAGES as STAGES
from Avatar import Avatar as Avatar

class StoryModeEquipmentsController(equipment_ctrl.EquipmentsController):
    def _doChangeSetting(self, item, entityName=None, avatar=None):
        ...

class StoryModeReplayEquipmentsController(EquipmentsReplayPlayer, StoryModeEquipmentsController):
    ...

def register():
    ...
