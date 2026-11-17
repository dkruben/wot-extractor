# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/impl/lobby/tooltips/battle_ability_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewvalues as viewvalues
from frameworks.wulf import ViewSettings as ViewSettings
from frontline.gui.frontline_helpers import AbilitiesTemplates as AbilitiesTemplates
from frontline.gui.impl.gen.view_models.views.lobby.tooltips.battle_ability_tooltip_levels_model import BattleAbilityTooltipLevelsModel as BattleAbilityTooltipLevelsModel
from frontline.gui.impl.gen.view_models.views.lobby.tooltips.battle_ability_tooltip_param_model import BattleAbilityTooltipParamModel as BattleAbilityTooltipParamModel
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.game_control.epic_meta_game_ctrl import EpicMetaGameSkill as EpicMetaGameSkill
from gui.impl.backport.backport_tooltip import DecoratedTooltipWindow as DecoratedTooltipWindow
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.tooltips import ToolTipBaseData as ToolTipBaseData
from helpers import dependency as dependency
from frontline.gui.impl.gen.view_models.views.lobby.tooltips.battle_ability_tooltip_model import BattleAbilityTooltipModel as BattleAbilityTooltipModel
from frontline.gui.frontline_helpers import getSkillParams as getSkillParams
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController
from skeletons.gui.shared import IItemsCache as IItemsCache
TEMPLATES: Any

class BattleAbilityTooltipView(ViewImpl):
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
    @staticmethod
    def __fillDetailsSkillLevels(levels, characteristics, skillData):
        ...

class BattleAbilityTooltipData(ToolTipBaseData):
    def __init__(self, context):
        ...
    @staticmethod
    def getDisplayableData(intCD, *args, **kwargs):
        ...
