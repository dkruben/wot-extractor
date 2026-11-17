# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/tooltips/skills_efficiency_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.tooltips.skills_efficiency_tooltip_model import SkillsEfficiencyTooltipModel as SkillsEfficiencyTooltipModel
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from items.tankmen import MAX_SKILLS_EFFICIENCY_XP as MAX_SKILLS_EFFICIENCY_XP
from skeletons.gui.shared import IItemsCache as IItemsCache

class SkillsEfficiencyTooltip(ViewImpl):
    __slots__: tuple
    itemsCache: Any
    tankmanID: Any
    isShowDiscount: Any
    skillEfficiency: Any
    def __init__(self, tankmanID, skillEfficiency=0, isShowDiscount=False, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _fillModel(self):
        ...
