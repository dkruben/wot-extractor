# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/tooltips/commander_bonus_additional_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.tooltips.crew_perks_additional_tooltip_model import CrewPerksAdditionalTooltipModel as CrewPerksAdditionalTooltipModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.gui_items.tankman_skill import COMMANDER_BONUS as COMMANDER_BONUS
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from items.components.skills_constants import SkillTypeName as SkillTypeName
ANIMATION_NAME = 'skillCommanderBonus'
DEF_COMMANDER_BONUS = 10

class CommanderBonusAdditionalTooltip(ViewImpl):
    _itemsCache: Any
    __slots__: tuple
    _tankman: Any
    def __init__(self, tankmanId):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _fillModel(self):
        ...
