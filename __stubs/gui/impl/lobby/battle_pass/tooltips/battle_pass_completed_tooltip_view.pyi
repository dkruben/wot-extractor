# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_pass/tooltips/battle_pass_completed_tooltip_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from frameworks.wulf import ViewSettings as ViewSettings
from gui.battle_pass.battle_pass_helpers import getChapterType as getChapterType, getReceivedTankmenCount as getReceivedTankmenCount, getTankmenShopPackages as getTankmenShopPackages
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.battle_pass.tooltips.battle_pass_completed_tooltip_view_model import BattlePassCompletedTooltipViewModel as BattlePassCompletedTooltipViewModel, ChapterType as ChapterType
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattlePassController as IBattlePassController

class BattlePassCompletedTooltipView(ViewImpl):
    __battlePass: Any
    __slots__: tuple
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __isAvailableTankmen(self, shopPackages):
        ...
