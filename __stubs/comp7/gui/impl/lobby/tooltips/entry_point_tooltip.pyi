# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/tooltips/entry_point_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7_core.gui.impl.lobby.tooltips.entry_point_tooltip import Comp7CoreEntryPointTooltip as Comp7CoreEntryPointTooltip
from comp7.gui.impl.gen.view_models.views.lobby.enums import SeasonName as Comp7SeasonName
from comp7.gui.impl.gen.view_models.views.lobby.season_model import SeasonState as Comp7SeasonState
from comp7.gui.impl.gen.view_models.views.lobby.tooltips.entry_point_tooltip_model import EntryPointTooltipModel as EntryPointTooltipModel
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7Controller as IComp7Controller

class Comp7EntryPointTooltip(Comp7CoreEntryPointTooltip):
    __comp7Controller: Any
    def __init__(self, eventBanner):
        ...
    @property
    def _modeController(self):
        ...
    @property
    def _seasonStateClazz(self):
        ...
    @property
    def _seasonNameClazz(self):
        ...
    def _getEvents(self):
        ...
    def __onConfigChanged(self):
        ...
