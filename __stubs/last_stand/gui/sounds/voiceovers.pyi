# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/sounds/voiceovers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from helpers import dependency as dependency
from last_stand.gui.sounds import playSound as playSound
from last_stand.skeletons.difficulty_level_controller import IDifficultyLevelController as IDifficultyLevelController
from last_stand.gui.ls_account_settings import isSoundPlayed as isSoundPlayed, setSoundPlayed as setSoundPlayed
from gui.battle_control.avatar_getter import getSoundNotifications as getSoundNotifications
from gui.IngameSoundNotifications import LOG_VO as LOG_VO

class Voiceover(object):
    _difficultyCtrl: Any
    _standardVoiceover: Any
    _expositionVoiceover: Any
    _useNotificationSystem: Any
    _aliveOnly: Any
    def __init__(self, standardVoiceover, expositionVoiceover=None, useNotificationSystem=True, aliveOnly=False):
        ...
    def play(self):
        ...
