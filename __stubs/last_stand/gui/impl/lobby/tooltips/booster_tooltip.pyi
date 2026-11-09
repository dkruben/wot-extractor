# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/tooltips/booster_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from last_stand.gui.impl.gen.view_models.views.lobby.tooltips.booster_tooltip_model import BoosterTooltipModel as BoosterTooltipModel
from last_stand.gui.impl.lobby.ls_helpers import getBoosterFactorsParam as getBoosterFactorsParam
from last_stand_common.last_stand_constants import BoostersSettings as BoostersSettings
from skeletons.gui.server_events import IEventsCache as IEventsCache

class BoosterTooltipView(ViewImpl):
    eventsCache: Any
    __boosterName: Any
    def __init__(self, boosterName='', layoutID=...):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
