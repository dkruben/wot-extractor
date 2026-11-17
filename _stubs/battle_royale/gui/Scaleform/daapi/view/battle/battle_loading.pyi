# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/battle/battle_loading.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.meta.BattleRoyaleLoadingMeta import BattleRoyaleLoadingMeta as BattleRoyaleLoadingMeta
from gui.impl import backport as backport
from gui.impl.gen.resources import R as R
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController

class BattleLoading(BattleRoyaleLoadingMeta):
    __battleRoyaleController: Any
    def _populate(self):
        ...
    def _formatTipTitle(self, tipTitleText):
        ...
    def _formatTipBody(self, tipBody):
        ...
    def _getBattleTypeIconPath(self, sizeFolder='c_136x136'):
        ...
    def _makeVisualTipVO(self, arenaDP, tip=None):
        ...
