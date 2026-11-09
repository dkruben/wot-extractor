# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/page/prebattle_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import constants as constants
from CurrentVehicle import g_currentVehicle as g_currentVehicle, g_currentPreviewVehicle as g_currentPreviewVehicle
from PlayerEvents import g_playerEvents as g_playerEvents
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import ACTIVE_TEST_PARTICIPATION_CONFIRMED as ACTIVE_TEST_PARTICIPATION_CONFIRMED
from adisp import adisp_process as adisp_process, adisp_async as adisp_async
from gui.Scaleform.daapi.view.lobby.header import battle_selector_items as battle_selector_items
from gui.impl.gen.view_models.views.lobby.page.header.prebattle_model import PrebattleModel as PrebattleModel
from gui.impl.lobby.common.vehicle_model_helpers import fillVehicleModel as fillVehicleModel
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.prb_control.dispatcher import g_prbLoader as g_prbLoader
from gui.prb_control.entities.base.ctx import PrbAction as PrbAction
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.prb_control.settings import REQUEST_TYPE as REQUEST_TYPE
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.event_dispatcher import showActiveTestConfirmDialog as showActiveTestConfirmDialog
from gui.shared.system_factory import collectBattleButtonManualControl as collectBattleButtonManualControl
from helpers import dependency as dependency
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from shared_utils import findFirst as findFirst
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.game_control import IPlatoonController as IPlatoonController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from wg_async import wg_async as wg_async, wg_await as wg_await
_logger: Any

# base nao representavel no stub: ViewComponent[...]
class PrebattlePresenter(IGlobalListener, CallbackDelayer):
    __lobbyContext: Any
    __platoonCtrl: Any
    __connectionMgr: Any
    __battleVehicleInvId: Any
    __arenaCreated: Any
    __enabled: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getListeners(self):
        ...
    def onPrbEntitySwitched(self):
        ...
    def onEnqueued(self, *args, **kwargs):
        ...
    def onDequeued(self, *args, **kwargs):
        ...
    def onEnqueueError(self, *args, **kwargs):
        ...
    def onArenaJoinFailure(self, *args, **kwargs):
        ...
    def onKickedFromQueue(self, *args, **kwargs):
        ...
    def onKickedFromArena(self, *args, **kwargs):
        ...
    def _onAction(self, event):
        ...
    # decorador original: @adisp_process
    def __startBattleHandler(self):
        ...
    def _onPlatoonMembersUpdate(self):
        ...
    def _onArenaCreated(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @wg_async
    def __processMMActiveTestConfirm(self, prbEntity, callback):
        ...
    def __onSetPrebattleCoolDown(self, event):
        ...
    def __onUpdatePrbControls(self, _):
        ...
    def __setVehicleInfo(self):
        ...
    def _onPrebattleUpdate(self):
        ...
    def __getBattleStatus(self):
        ...
    def __setStates(self):
        ...
    def __setBattleButtonAlwaysOn(self):
        ...
    def __onControlsDisable(self):
        ...
    def __onControlsEnable(self):
        ...
