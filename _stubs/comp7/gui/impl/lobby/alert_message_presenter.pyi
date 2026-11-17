# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/alert_message_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import typing as typing
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from comp7.gui.impl.gen.view_models.views.lobby.alert_message_model import AlertMessageModel as AlertMessageModel, State as State
from comp7.gui.shared import event_dispatcher as comp7_events
from frameworks.wulf.view.array import fillIntsArray as fillIntsArray
from gui.impl import backport as backport
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.periodic_battles.models import PeriodType as PeriodType
from helpers import dependency as dependency
from math_common import round_py2_style_int as round_py2_style_int
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from typing import Any as Any

# base nao representavel no stub: ViewComponent[...]
class AlertMessagePresenter:
    __comp7Controller: _Any
    def __init__(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _getCallbacks(self):
        ...
    def _getEvents(self):
        ...
    def __onClick(self):
        ...
    def __getAlertState(self):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateAlertData(self, _=None, model=None):
        ...
