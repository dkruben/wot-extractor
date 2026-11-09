# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/server_events/bonuses.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.server_events.bonuses import TokensBonus as TokensBonus
from halloween.skeletons.halloween_twitch_con_controller import IHalloweenTwitchConController as IHalloweenTwitchConController
from helpers import dependency as dependency
from halloween_common.halloween_constants import HWStoryChoiceSettings as HWStoryChoiceSettings

class CerfTokenBonus(TokensBonus):
    def __init__(self, name, value, isCompensation=False, ctx=None):
        ...
    def isShowInGUI(self):
        ...

class FakeChoiceMedalTokenBonus(TokensBonus):
    def __init__(self, name, value, isCompensation=False, ctx=None):
        ...
    def isShowInGUI(self):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def cerfTokenChecker(tokenID, ctrl=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def fakeChoiceMedalTokenChecker(tokenID, ctrl=None):
    ...
