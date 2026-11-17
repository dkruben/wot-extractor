# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/impl/lobby/presenters/alert_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frontline.gui.frontline_helpers import isHangarAvailable as isHangarAvailable, getFrontlineState as getFrontlineState
from frontline.gui.impl.gen.view_models.views.lobby.components.alert_message_model import AlertMessageModel as AlertMessageModel
from CurrentVehicle import g_currentVehicle as g_currentVehicle, g_currentPreviewVehicle as g_currentPreviewVehicle
from frontline.gui.impl.gen.view_models.views.lobby.views.frontline_const import FrontlineState as FrontlineState
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.event_dispatcher import showEpicBattlesPrimeTimeWindow as showEpicBattlesPrimeTimeWindow
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController
from skeletons.gui.shared import IItemsCache as IItemsCache

class AlertButtonAction(object):
    CHANGE_SERVER = 'change_Server'

# base nao representavel no stub: ViewComponent[...]
class AlertPresenter:
    __epicController: Any
    __itemsCache: Any
    _buttonType: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _getListeners(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _updateModel(self):
        ...
    def _onPrimeTimeStatusUpdated(self, *_):
        ...
    def __onInventoryUpdate(self, _, diff):
        ...
    def __onClick(self):
        ...
    def __onFightButtonUpdateEventHandler(self, _):
        ...
