# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/page/fight_start.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from CurrentVehicle import g_currentVehicle as g_currentVehicle, g_currentPreviewVehicle as g_currentPreviewVehicle
from constants import PREBATTLE_TYPE as PREBATTLE_TYPE
from gui.Scaleform.daapi.view.lobby.header.helpers.fight_btn_tooltips import getEpicBattlesOnlyVehicleTooltipData as getEpicBattlesOnlyVehicleTooltipData, getPreviewTooltipData as getPreviewTooltipData
from gui.impl.gen.view_models.views.lobby.page.header.fight_start_model import FightStartModel as FightStartModel
from gui.impl.lobby.common.lobby_header_utils import findExtensionTooltip as findExtensionTooltip
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.prb_control.entities.base.listener import IPrbListener as IPrbListener
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from helpers import dependency as dependency
from skeletons.gui.game_control import IPlatoonController as IPlatoonController, IHangarGuiController as IHangarGuiController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.lobby_state_machine.states import LobbyStateFlags as LobbyStateFlags

# base nao representavel no stub: ViewComponent[...]
class FightStartPresenter(IPrbListener):
    __lobbyContext: Any
    __platoonCtrl: Any
    __hangarGuiCtrl: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getListeners(self):
        ...
    def __onUpdatePrbControls(self, _):
        ...
    def __createTooltipText(self):
        ...
    def _onFightButtonUpdate(self):
        ...

def isNotPBSPreview():
    ...
