# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/AccountBattleRoyaleTournamentComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattleRoyaleTournamentController as IBattleRoyaleTournamentController
import BattleRoyaleTournament as BattleRoyaleTournament
_logger: Any

class AccountBattleRoyaleTournamentComponent(BigWorld.StaticScriptComponent):
    __battleRoyaleTournamentController: Any
    def setParticipants(self, participants):
        ...
    def setTournamentToken(self, token):
        ...
    def tournamentJoin(self, tournamentID, callback=None):
        ...
    def tournamentLeave(self, callback=None):
        ...
    def tournamentReady(self, vehInvID, tournamentID, callback=None):
        ...
    def tournamentNotReady(self, tournamentID, callback=None):
        ...
    def tournamentForceStart(self, mapID, callback=None):
        ...
