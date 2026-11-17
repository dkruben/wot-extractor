# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_hints/battle_hints_overlap_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from logging import getLogger as getLogger
import typing as typing
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from helpers import dependency as dependency
from PlayerEvents import g_playerEvents as g_playerEvents
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.battle_hints.battle_hints_overlap_controller import IBattleHintsOverlapController as IBattleHintsOverlapController
from frameworks.wulf import WindowLayer as WindowLayer
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES as BATTLE_VIEW_ALIASES
from gui.Scaleform.daapi.view.battle.shared import SharedPage as SharedPage
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.battle_control.controllers.battle_hints.queues import BattleHint as BattleHint
_logger: Any
NEWBIE_SETTINGS: set
OVERLAP_SETTINGS: dict

class HintScope(str, Enum):
    NEWBIE = 'newbie'
    STORY_MODE = 'story_mode'
    LOCAL_STORY = 'local_story'

class BattleHintsOverlapController(IBattleHintsOverlapController):
    _appLoader: Any
    _sessionProvider: Any
    _hiddenViews: Any
    def __init__(self):
        ...
    def fini(self):
        ...
    def hintShown(self, battleHint):
        ...
    def hintHidden(self):
        ...
    def _onHintShown(self, battleHint):
        ...
    def _onEmptyHintsQueue(self):
        ...
    def _clear(self):
        ...
    def _getBattlePageView(self):
        ...

def addSettings(arenaBonusType, hintScope, views):
    ...
