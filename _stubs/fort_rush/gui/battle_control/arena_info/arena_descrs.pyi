# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/battle_control/arena_info/arena_descrs.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.battle_control.arena_info.arena_descrs import ArenaDescriptionWithInvitation as ArenaDescriptionWithInvitation
from gui.battle_control.arena_info.settings import DEFAULT_SCREEN_MAP_IMAGE_RES_PATH as DEFAULT_SCREEN_MAP_IMAGE_RES_PATH
from gui.impl import backport as backport
from gui.impl.gen import R as R
_BATTLE_LOADING_TEXT_RES = R.strings.fort_rush.battleLoading
_FORT_RUSH_LOADING_SCREEN_ICONS: dict

class FortRushArenaDescription(ArenaDescriptionWithInvitation):
    def getDescriptionString(self, isInBattle=True):
        ...
    def getWinString(self, isInBattle=True):
        ...
    def getBattleTypeIconPath(self, sizeFolder='c_136x136'):
        ...
    def getScreenIcon(self):
        ...
