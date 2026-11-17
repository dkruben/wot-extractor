# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/tooltips/entry_point_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7_core.gui.impl.lobby.tooltips.entry_point_tooltip import Comp7CoreEntryPointTooltip as Comp7CoreEntryPointTooltip
from comp7_light.gui.impl.gen.view_models.views.lobby.enums import SeasonName as Comp7LightSeasonName
from comp7_light.gui.impl.gen.view_models.views.lobby.season_model import SeasonState as Comp7LightSeasonState
from comp7_light.gui.impl.gen.view_models.views.lobby.tooltips.entry_point_tooltip_model import EntryPointTooltipModel as EntryPointTooltipModel
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7LightController as IComp7LightController

class Comp7LightEntryPointTooltip(Comp7CoreEntryPointTooltip):
    __comp7LightController: Any
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
