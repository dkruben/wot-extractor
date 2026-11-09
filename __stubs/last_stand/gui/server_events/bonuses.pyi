# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/server_events/bonuses.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.server_events.bonuses import TokensBonus as TokensBonus
from last_stand_common.last_stand_constants import BoostersSettings as BoostersSettings, ProgressPointsSettings as ProgressPointsSettings

class BoosterTokenBonus(TokensBonus):
    def __init__(self, name, value, isCompensation=False, ctx=None):
        ...
    def isShowInGUI(self):
        ...

class ProgressPointTokenBonus(TokensBonus):
    def __init__(self, name, value, isCompensation=False, ctx=None):
        ...
    def isShowInGUI(self):
        ...

def boosterTokenChecker(tokenID):
    ...
def progressPointTokenChecker(tokenID):
    ...
