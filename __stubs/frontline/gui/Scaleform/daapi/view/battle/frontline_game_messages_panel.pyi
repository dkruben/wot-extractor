# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/frontline_game_messages_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BattleReplay as BattleReplay
from ReservesEvents import randomReservesEvents as randomReservesEvents
from gui.Scaleform.daapi.view.meta.GameMessagesPanelMeta import GameMessagesPanelMeta as GameMessagesPanelMeta
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.Scaleform.locale.EPIC_BATTLE import EPIC_BATTLE as EPIC_BATTLE
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control.controllers.battle_hints.controller import BattleHintComponent as BattleHintComponent
from gui.battle_control.controllers.battle_hints.queues import BattleHintQueueParams as BattleHintQueueParams
from gui.Scaleform.genConsts.GAME_MESSAGES_CONSTS import GAME_MESSAGES_CONSTS as GAME_MESSAGES_CONSTS
from gui.Scaleform.daapi.view.battle.shared.game_messages_panel import PlayerMessageData as PlayerMessageData
from gui.battle_results.components.common import makeEpicBattleFinishResultLabel as makeEpicBattleFinishResultLabel
from hints.battle.schemas.base import ClientHintModel as ClientHintModel

class FrontlineMessagePanel(BattleHintComponent, GameMessagesPanelMeta):
    sessionProvider: Any
    __blockNewMessages: Any
    def __init__(self):
        ...
    def sendEndGameMessage(self, winningTeam, reason):
        ...
    def onMessageStarted(self, msgType, modificator, id_):
        ...
    def onMessagePhaseStarted(self, msgType, modificator, msgID):
        ...
    def onMessageEnded(self, msgType, msgID):
        ...
    def onMessageHiding(self, msgType, msgID):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _showHint(self, model, params):
        ...
    def _hideHint(self):
        ...
    def __onIngameMessageReady(self, msg):
        ...
