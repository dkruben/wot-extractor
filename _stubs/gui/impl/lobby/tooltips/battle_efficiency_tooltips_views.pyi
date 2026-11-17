# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tooltips/battle_efficiency_tooltips_views.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.battle_results.presenters.packers.tooltips.efficiency_tooltips import CriticalDamageTooltipPacker as CriticalDamageTooltipPacker
from gui.battle_results.presenters.wrappers import hasPresenter as hasPresenter
from gui.impl.gen.view_models.views.lobby.battle_results.tooltips.critical_damage_tooltip_model import CriticalDamageTooltipModel as CriticalDamageTooltipModel
from gui.impl.gen.view_models.views.lobby.battle_results.tooltips.efficiency_tooltip_model import EfficiencyTooltipModel as EfficiencyTooltipModel
from gui.impl.gen import R as R
from gui.impl.lobby.battle_results.tooltips_packers import BattleEfficiencyTooltipsPacker as BattleEfficiencyTooltipsPacker
from gui.impl.pub import ViewImpl as ViewImpl

class BattleResultsStatsTooltipView(ViewImpl):
    _TOOLTIPS_PACKER = BattleEfficiencyTooltipsPacker
    __efficiencyParam: Any
    __arenaUniqueID: Any
    __userName: Any
    def __init__(self, arenaUniqueID, paramType, userName):
        ...
    @property
    def arenaUniqueID(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    # decorador original: @hasPresenter(...)
    def __packContent(self, presenter=None):
        ...

class BattleResultsCriticalDamageTooltipView(ViewImpl):
    __efficiencyParam: Any
    __arenaUniqueID: Any
    __userName: Any
    def __init__(self, arenaUniqueID, paramType, userName):
        ...
    @property
    def arenaUniqueID(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    # decorador original: @hasPresenter(...)
    def __packContent(self, presenter=None):
        ...
