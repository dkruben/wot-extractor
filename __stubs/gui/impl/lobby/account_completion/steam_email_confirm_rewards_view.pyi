# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/account_completion/steam_email_confirm_rewards_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.battle_pass.sounds import BattlePassSounds as BattlePassSounds
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.account_completion.steam_email_confirm_rewards_view_model import SteamEmailConfirmRewardsViewModel as SteamEmailConfirmRewardsViewModel
from gui.impl.lobby.account_completion.utils.common import fillRewards as fillRewards
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.sounds.filters import States as States, StatesGroup as StatesGroup
from sound_gui_manager import CommonSoundSpaceSettings as CommonSoundSpaceSettings
from typing import Dict as Dict

class SteamEmailConfirmRewardsView(ViewImpl):
    __slots__: tuple
    _COMMON_SOUND_SPACE: Any
    __tooltips: Any
    def __init__(self, rewards):
        ...
    @property
    def viewModel(self):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    def getTooltipData(self, event):
        ...
    def _onLoading(self, rewards, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def __updateRewards(self, rewards, model):
        ...
    def __onClose(self):
        ...

class SteamEmailConfirmRewardsViewWindow(LobbyNotificationWindow):
    __slots__: tuple
    def __init__(self, rewards, parent=None):
        ...
