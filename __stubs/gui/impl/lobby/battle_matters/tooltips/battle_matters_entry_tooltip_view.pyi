# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_matters/tooltips/battle_matters_entry_tooltip_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.battle_pass.battle_pass_bonuses_packers import ExtendedItemBonusUIPacker as ExtendedItemBonusUIPacker
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.battle_matters.tooltips.battle_matters_entry_tooltip_view_model import BattleMattersEntryTooltipViewModel as BattleMattersEntryTooltipViewModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.missions.packers.bonus import getDefaultBonusPacker as getDefaultBonusPacker
from helpers import dependency as dependency
from skeletons.gui.battle_matters import IBattleMattersController as IBattleMattersController
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.impl.lobby.battle_matters.battle_matters_bonus_packer import BattleMattersEntitlementsBonusUIPacker as BattleMattersEntitlementsBonusUIPacker, bonusesSortKey as bonusesSortKey, battleMattersSortKey as battleMattersSortKey

class BattleMattersEntryTooltipView(ViewImpl):
    __slots__: tuple
    __battleMattersController: Any
    __itemsCache: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    @staticmethod
    def __getBonusBacker():
        ...
