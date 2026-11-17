# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/tooltips/fort_rush_progression_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from fort_rush.gui.impl.gen.view_models.tooltips.fort_rush_progression_tooltip_view_model import FortRushProgressionTooltipViewModel as FortRushProgressionTooltipViewModel
from fort_rush.skeletons.battle_controller import IFortRushBattleController as IFortRushBattleController
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.lobby.common.view_helpers import packBonusModelAndTooltipData as packBonusModelAndTooltipData
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.missions.packers.bonus import getDefaultBonusPacker as getDefaultBonusPacker
from helpers import dependency as dependency

class FortRushProgressionWidgetTooltipView(ViewImpl):
    __ctrl: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __updateViewModel(self):
        ...
