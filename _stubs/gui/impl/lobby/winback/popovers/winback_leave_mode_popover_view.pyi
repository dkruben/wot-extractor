# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/winback/popovers/winback_leave_mode_popover_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers.AccountSettings import Winback as Winback
from constants import WINBACK_BATTLE_TOKEN_DRAW_REASON as WINBACK_BATTLE_TOKEN_DRAW_REASON
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.winback.popovers.winback_leave_mode_popover_view_model import WinbackLeaveModePopoverViewModel as WinbackLeaveModePopoverViewModel
from gui.impl.lobby.winback.tooltips.mode_info_tooltip import ModeInfoTooltip as ModeInfoTooltip
from gui.impl.pub import PopOverViewImpl as PopOverViewImpl
from gui.shared import g_eventBus as g_eventBus
from gui.shared.events import ModeSelectorPopoverEvent as ModeSelectorPopoverEvent
from gui.winback.winback_helpers import leaveWinbackMode as leaveWinbackMode, selectRandom as selectRandom, setWinbackSetting as setWinbackSetting
from helpers import dependency as dependency
from skeletons.gui.game_control import IWinbackController as IWinbackController

class WinbackLeaveModePopoverView(PopOverViewImpl):
    __slots__: tuple
    _winbackController: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _onLoading(self):
        ...
    def _initialize(self):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def __onClick(self):
        ...
    def __updateBulletSetting(self):
        ...
