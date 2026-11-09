# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/schedule_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7.gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as COMP7_TOOLTIPS
from comp7.gui.impl.gen.view_models.views.lobby.enums import SeasonName as SeasonName
from comp7.gui.impl.gen.view_models.views.lobby.schedule_info_model import ScheduleInfoModel as ScheduleInfoModel
from comp7.gui.impl.gen.view_models.views.lobby.season_model import SeasonState as SeasonState
from comp7.gui.impl.gen.view_models.views.lobby.year_model import YearState as YearState
from comp7_core.gui.impl.lobby.comp7_core_helpers import comp7_core_model_helpers as comp7_core_model_helpers
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7Controller as IComp7Controller

# base nao representavel no stub: ViewComponent[...]
class SchedulePresenter(IGlobalListener):
    __comp7Controller: Any
    def __init__(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    @property
    def viewModel(self):
        ...
    def __onScheduleUpdated(self):
        ...
