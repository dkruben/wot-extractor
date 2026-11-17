# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/battle_session/legacy/permissions.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.prb_control import prb_getters as prb_getters
from gui.prb_control.entities.base.legacy.permissions import LegacyPermissions as LegacyPermissions
from gui.prb_control.entities.base.limits import TeamNoPlayersInBattle as TeamNoPlayersInBattle, MaxCount as MaxCount

class BattleSessionPermissions(LegacyPermissions):
    def canSendInvite(self):
        ...
    def canExitFromQueue(self):
        ...
    @classmethod
    def isCreator(cls, roles):
        ...
    def canAssignToTeam(self, team=1, isSelfAssignment=False):
        ...
    def _canAddPlayers(self):
        ...
