# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/battle_control/controllers/repository.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.battle_control.controllers import _ControllersRepository as _ControllersRepository, debug_ctrl as debug_ctrl, SharedControllersRepository as SharedControllersRepository
from gui.battle_control.controllers.battle_hints import controller as battle_hints_ctrl
from gui.battle_control.controllers.sound_ctrls.epic_battle_sounds import EpicShotsResultSoundsController as EpicShotsResultSoundsController
from gui.battle_control.controllers.vse_hud_settings_ctrl import vse_hud_settings_ctrl as vse_hud_settings_ctrl
from story_mode.gui.battle_control.controllers.appearance_cache_controller import AppearanceCacheController as AppearanceCacheController
from story_mode.gui.battle_control.controllers.messages_controller import StoryModeBattleMessagesPlayer as StoryModeBattleMessagesPlayer, StoryModeBattleMessagesController as StoryModeBattleMessagesController
from story_mode.gui.battle_control.controllers.settings_contoller import OverrideSettingsController as OverrideSettingsController

class StoryModeRepository(_ControllersRepository):
    __slots__: tuple
    @classmethod
    def create(cls, setup):
        ...

class OnboardingRepository(StoryModeRepository):
    __slots__: tuple
    @classmethod
    def create(cls, setup):
        ...

class StoryModeSharedRepository(SharedControllersRepository):
    __slots__: tuple
    @classmethod
    def getMessagesController(cls, setup):
        ...
