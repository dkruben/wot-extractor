# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/StoryModeAccountComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import AccountCommands as AccountCommands
from BaseAccountExtensionComponent import BaseAccountExtensionComponent as BaseAccountExtensionComponent
from PlayerEvents import g_playerEvents as g_playerEvents
from constants import QUEUE_TYPE as QUEUE_TYPE
from helpers import dependency as dependency
from story_mode.skeletons.story_mode_controller import IStoryModeController as IStoryModeController

class StoryModeAccountComponent(BaseAccountExtensionComponent):
    _storyModeCtrl: Any
    def enqueueBattle(self):
        ...
    def dequeueBattle(self):
        ...
