# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/lobby/header/battle_selector_items.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import QUEUE_TYPE as QUEUE_TYPE
from gui.Scaleform.daapi.view.lobby.header import battle_selector_items as battle_selector_items
from gui.shared.utils import SelectorBattleTypesUtils as selectorUtils
from story_mode.gui.story_mode_gui_constants import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME, SELECTOR_BATTLE_TYPES as SELECTOR_BATTLE_TYPES
from story_mode.skeletons.story_mode_controller import IStoryModeController as IStoryModeController
from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers import dependency as dependency

class _StoryModeItem(battle_selector_items.SelectorItem):
    storyModeCtrl: Any
    _isLocked: Any
    _isSelected: Any
    _isDisabled: Any
    def select(self):
        ...
    def isRandomBattle(self):
        ...
    def setLocked(self, value):
        ...
    def getSmallIcon(self):
        ...
    def getLargerIcon(self):
        ...
    def isShowEventIndication(self):
        ...
    def _update(self, state):
        ...

def addStoryModeType(items):
    ...
