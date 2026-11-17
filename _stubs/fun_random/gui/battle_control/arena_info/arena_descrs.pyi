# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/battle_control/arena_info/arena_descrs.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.battle_control.arena_info.arena_descrs import ArenaDescriptionWithInvitation as ArenaDescriptionWithInvitation
from gui.impl import backport as backport
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin as FunAssetPacksMixin, FunSubModesWatcher as FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasBattleSubMode as hasBattleSubMode

class FunRandomArenaDescription(ArenaDescriptionWithInvitation, FunAssetPacksMixin, FunSubModesWatcher):
    def getBattleTypeIconPath(self, sizeFolder='c_136x136'):
        ...
    def getDescriptionString(self, isInBattle=True):
        ...
    # decorador original: @hasBattleSubMode(...)
    def __getDescriptionString(self):
        ...
