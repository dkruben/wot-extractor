# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/AccountBattleRoyaleComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BattleRoyaleConstants as brc
import AccountCommands as AccountCommands
from BaseAccountExtensionComponent import BaseAccountExtensionComponent as BaseAccountExtensionComponent
from battle_royale.gui.constants import BattleRoyaleSubMode as BattleRoyaleSubMode
from battle_royale.gui.prb_control.entities.regular.pre_queue.entity import BRQueueCtx as BRQueueCtx
from PlayerEvents import g_playerEvents as events
from constants import QUEUE_TYPE as QUEUE_TYPE
_logger: Any

class AccountBattleRoyaleComponent(BaseAccountExtensionComponent):
    def setBrCoin(self, amount, callback=None):
        ...
    def enqueueBattleRoyale(self, ctx):
        ...
    def dequeueBattleRoyale(self):
        ...
