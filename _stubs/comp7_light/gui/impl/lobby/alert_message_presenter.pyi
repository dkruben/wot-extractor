# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/alert_message_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7_light.gui.impl.gen.view_models.views.lobby.alert_message_model import AlertMessageModel as AlertMessageModel, State as State
from comp7_light.gui.shared import event_dispatcher as event_dispatcher
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7LightController as IComp7LightController

# base nao representavel no stub: ViewComponent[...]
class AlertMessagePresenter:
    __comp7LightController: Any
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
    def __updateAlertData(self, _=None):
        ...
