# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/impl/lobby/tooltips/battle_ability_alt_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.game_control.epic_meta_game_ctrl import EpicMetaGameSkill as EpicMetaGameSkill
from gui.impl.backport.backport_tooltip import DecoratedTooltipWindow as DecoratedTooltipWindow
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.tooltips import ToolTipBaseData as ToolTipBaseData
from gui.shared.tooltips.advanced import MODULE_MOVIES as MODULE_MOVIES
from helpers import dependency as dependency
from frontline.gui.impl.gen.view_models.views.lobby.tooltips.battle_ability_alt_tooltip_model import BattleAbilityAltTooltipModel as BattleAbilityAltTooltipModel
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController
from skeletons.gui.shared import IItemsCache as IItemsCache

class BattleAbilityAltTooltipView(ViewImpl):
    _slots__: tuple
    __epicController: Any
    __itemsCache: Any
    intCD: Any
    __epicSkills: Any
    def __init__(self, intCD, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...

class BattleAbilityAltTooltipData(ToolTipBaseData):
    def __init__(self, context):
        ...
    @staticmethod
    def getDisplayableData(intCD, *args, **kwargs):
        ...
