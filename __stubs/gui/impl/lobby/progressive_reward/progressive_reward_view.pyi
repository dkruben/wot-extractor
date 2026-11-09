# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/progressive_reward/progressive_reward_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.impl.auxiliary.rewards_helper import fillStepsModel as fillStepsModel
from gui.impl.gen.view_models.views.lobby.progressive_reward.progressive_reward_view_model import ProgressiveRewardViewModel as ProgressiveRewardViewModel
from gui.impl.lobby.progressive_reward.progressive_award_sounds import setSoundState as setSoundState, ProgressiveRewardSoundEvents as ProgressiveRewardSoundEvents
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyWindow as LobbyWindow
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
_logger: Any

class ProgressiveRewardView(ViewImpl):
    _eventsCache: Any
    _lobbyContext: Any
    __slots__: tuple
    def __init__(self, contentResId, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __onWindowClose(self, _=None):
        ...
    def __onDestroy(self, _=None):
        ...
    def __onSyncCompleted(self, *_):
        ...
    def __update(self):
        ...
    def __onServerSettingsChange(self, diff):
        ...

class ProgressiveRewardWindow(LobbyWindow):
    __slots__: tuple
    def __init__(self, contentResId, *args, **kwargs):
        ...
