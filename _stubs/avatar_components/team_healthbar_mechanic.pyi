# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/avatar_components/team_healthbar_mechanic.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as BONUS_CAPS

class TeamHealthbarMechanic(object):
    __enabled: Any
    __lastTeamHealthPercentage: Any
    def __init__(self):
        ...
    def handleKey(self, isDown, key, mods):
        ...
    def onBecomePlayer(self):
        ...
    def onBecomeNonPlayer(self):
        ...
    def updateTeamsHealthPercentage(self, teamsHealthPercentage):
        ...
    def getHealthPercentage(self):
        ...
