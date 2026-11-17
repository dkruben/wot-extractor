# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/marathon/marathon_reward_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from account_helpers import AccountSettings as AccountSettings
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.marathon.marathon_reward_view_model import MarathonRewardViewModel as MarathonRewardViewModel
from gui.impl.lobby.marathon.marathon_reward_sounds import MarathonVideos as MarathonVideos, onVideoStart as onVideoStart, onVideoDone as onVideoDone
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyWindow as LobbyWindow
from gui.server_events.events_dispatcher import showMissionsMarathon as showMissionsMarathon
from gui.shared.event_dispatcher import selectVehicleInHangar as selectVehicleInHangar
_logger: Any

class MarathonRewardView(ViewImpl):
    __slots__: tuple
    __congratsSourceId: Any
    __videoShownKey: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __onGoToVehicle(self, _=None):
        ...
    def __onViewRewards(self, _=None):
        ...
    def __onCloseWindow(self, _=None):
        ...
    def __onVideoStarted(self, _=None):
        ...
    def __onVideoStopped(self, _=None):
        ...

class MarathonRewardViewWindow(LobbyWindow):
    __slots__: tuple
    def __init__(self, *args, **kwargs):
        ...
