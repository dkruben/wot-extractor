# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/game_control/sounds_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import enum as enum
import typing as typing
import SoundGroups as SoundGroups
import WWISE as WWISE
from story_mode.gui.sound_constants import GAMEMODE_GROUP as GAMEMODE_GROUP, GAMEMODE_STATE as GAMEMODE_STATE
from story_mode_common.configs.story_mode_missions import SoundsModel as SoundsModel
from story_mode_common.configs.sounds_schema import SoundModel as SoundModel

class DefaultMusic(str, enum.Enum):
    start = 'ob_music_start'
    stop = 'ob_music_stop'

class DefaultAmbience(str, enum.Enum):
    start = 'sm_lobby_enter'
    stop = 'sm_lobby_exit'

class SoundsController(object):
    __musicStarted: Any
    __ambienceStarted: Any
    def __init__(self):
        ...
    def startMusicAndAmbience(self, soundSchema):
        ...
    def stopMusicAndAmbience(self):
        ...
    def startBattleMusic(self, soundSchema):
        ...
    def stopBattleMusic(self, soundSchema):
        ...
    def __startSound(self, currentSound, newSound):
        ...
    def _startMusic(self, music):
        ...
    def _startAmbience(self, ambience):
        ...
    @staticmethod
    def stopSound(sound):
        ...
    @staticmethod
    def setStateIfProvided(group='', state=''):
        ...
