# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/uilogging/player_satisfaction_rating/loggers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import json as json
import logging as logging
from enum import Enum as Enum
from typing import TYPE_CHECKING as TYPE_CHECKING
import BigWorld as BigWorld
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from uilogging.base.logger import MetricsLogger as MetricsLogger
from uilogging.player_satisfaction_rating.logging_constants import FEATURE as FEATURE, NO_MIN_VIEW_TIME as NO_MIN_VIEW_TIME, POST_BATTLE_CM_ACTION_TO_PLAYER_SATISFACTION_CM_ACTION as POST_BATTLE_CM_ACTION_TO_PLAYER_SATISFACTION_CM_ACTION, PlayerSatisfactionRatingLogActions as PlayerSatisfactionRatingLogActions, MIN_VIEW_TIME as MIN_VIEW_TIME, PlayerSatisfactionRatingKeys as PlayerSatisfactionRatingKeys, PlayerSatisfactionRatingCMActions as PlayerSatisfactionRatingCMActions, PlayerSatisfactionRatingInfoKeys as PlayerSatisfactionRatingInfoKeys, PlayerSatisfationRatingInviteSource as PlayerSatisfationRatingInviteSource, ARENA_PERIOD_TO_KEY as ARENA_PERIOD_TO_KEY, PlayerSatisfactionRatingRadialMenuActions as PlayerSatisfactionRatingRadialMenuActions, RADIAL_MENU_ACTIONS_TO_LOGGING_ACTIONS as RADIAL_MENU_ACTIONS_TO_LOGGING_ACTIONS
from wotdecorators import noexcept as noexcept
from gui.Scaleform.daapi.view.lobby.lobby_constants import USER as USER
from uilogging.types import ParentScreenType as ParentScreenType, ItemType as ItemType
from typing import Optional as Optional, Any as Any, Union as Union
_logger: _Any

class PlayerSatisfactionRatingViewLogger(MetricsLogger):
    __slots__: tuple
    _item: _Any
    _viewParent: _Any
    __minViewTime: _Any
    def __init__(self, parent, item, minViewTime=...):
        ...
    def onViewInitialize(self):
        ...
    # decorador original: @noexcept
    def onViewFinalize(self, itemState=None, additionalInfo=None):
        ...

class PostBattleContextMenuLogger(PlayerSatisfactionRatingViewLogger):
    __slots__: tuple
    _contextMenuAction: _Any
    def __init__(self):
        ...
    def setContextMenuAction(self, optionId):
        ...
    def onViewFinalize(self, **kwargs):
        ...

class BattleTeamStatsViewLogger(PlayerSatisfactionRatingViewLogger):
    _sessionProvider: _Any
    def __init__(self):
        ...
    # decorador original: @noexcept
    def onViewFinalize(self, **kwargs):
        ...

class InviteToPlatoonLogger(MetricsLogger):
    _sessionProvider: _Any
    def __init__(self):
        ...
    # decorador original: @noexcept
    def logPlatoonInvite(self, source):
        ...
    def _serializeShortAdditionalInfo(self):
        ...

class InBattleContextMenuLogger(PlayerSatisfactionRatingViewLogger):
    __slots__: tuple
    _sessionProvider: _Any
    _contextMenuAction: _Any
    def __init__(self):
        ...
    def setContextMenuAction(self, action):
        ...
    def onViewFinalize(self, **kwargs):
        ...

class RadialMenuLogger(PlayerSatisfactionRatingViewLogger):
    __slots__: tuple
    _sessionProvider: _Any
    _radialMenuAction: _Any
    def __init__(self):
        ...
    def setRadialMenuAction(self, action):
        ...
    def onViewFinalize(self, **kwargs):
        ...

class KeyboardShortcutLogger(MetricsLogger):
    _sessionProvider: _Any
    def __init__(self):
        ...
    def logKeyboardShortcutAction(self, action):
        ...

class BattleResponseLogger(PlayerSatisfactionRatingViewLogger):
    __slots__: tuple
    _sessionProvider: _Any
    _response: _Any
    def __init__(self):
        ...
    def setResponse(self, action):
        ...
    def onViewFinalize(self, **kwargs):
        ...

def _serializeAdditionalInfo(sessionProvider):
    ...
