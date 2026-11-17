# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/battleground/airdrops.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import AirdropType as AirdropType
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from arena_component_system.client_arena_component_system import ClientArenaComponent as ClientArenaComponent
from battleground.bot_drop_object import BotAirdrop as BotAirdrop
from battleground.loot_drop_object import PlaneLootAirdrop as PlaneLootAirdrop

class Airdrops(object):
    __sessionProvider: Any
    def scheduleLoot(self, dropID, position, serverTime):
        ...
    def scheduleBot(self, dropID, position, teamID, yawAxis, serverTime, airdropType=...):
        ...

class AirdropsComponent(ClientArenaComponent, Airdrops):
    def __init__(self, componentSystem):
        ...
