# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/spam_protection/battle_spam_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.battle_control.arena_info.interfaces import IBattleSpamController as IBattleSpamController
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.battle_control.controllers.spam_protection.cooldown_manager import SpamCooldownManager as SpamCooldownManager
from gui.battle_control.controllers.spam_protection.spam_constants import SpamEvents as SpamEvents, SPAM_COOLDOWNS as SPAM_COOLDOWNS

class BattleSpamController(IBattleSpamController):
    __cooldown: Any
    def __init__(self):
        ...
    def startControl(self, *args):
        ...
    def stopControl(self):
        ...
    def getControllerID(self):
        ...
    def filterAllyHitMessage(self, targetID):
        ...
    def filterAutoShootTracerSound(self, attackerID):
        ...
    def filterFullscreenEffects(self, attackerID):
        ...
    def filterMarkersHitState(self, targetID, stateKey):
        ...
    def __filterEvent(self, eventID, eventKey=None, adjustCooldown=True):
        ...
