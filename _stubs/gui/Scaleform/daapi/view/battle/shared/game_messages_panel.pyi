# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/game_messages_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from collections import namedtuple as namedtuple
import BattleReplay as BattleReplay
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.Scaleform.daapi.view.meta.GameMessagesPanelMeta import GameMessagesPanelMeta as GameMessagesPanelMeta
from gui.Scaleform.genConsts.GAME_MESSAGES_CONSTS import GAME_MESSAGES_CONSTS as GAME_MESSAGES_CONSTS
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_results.components.common import makeRegularFinishResultLabel as makeRegularFinishResultLabel
from gui.shared.utils import toUpper as toUpper

# base nao representavel no stub: namedtuple(...)
class PlayerMessageData:
    def getDict(self):
        ...

class GameMessagesPanel(GameMessagesPanelMeta):
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _addMessage(self, msg):
        ...
    def onMessageStarted(self, msgType, modificator, msgID):
        ...
    def onMessagePhaseStarted(self, type, modificator, id):
        ...
    def onMessageEnded(self, msgType, msgID):
        ...
    def onMessageHiding(self, msgType, msgID):
        ...
    def sendEndGameMessage(self, winningTeam, reason):
        ...
    def _sendEndGameMessage(self, messageType, subTitle):
        ...
    def _getMessageType(self, winningTeam):
        ...
    def setFlashObject(self, movieClip, autoPopulate=True, setScript=True):
        ...
