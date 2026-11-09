# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/stage_reward_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import WWISE as WWISE
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.impl.backport import createTooltipData as createTooltipData, BackportTooltipWindow as BackportTooltipWindow
from gui.impl.gen import R as R
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from last_stand.gui.impl.gen.view_models.views.lobby.stage_reward_view_model import StageRewardViewModel as StageRewardViewModel
from last_stand.gui.impl.lobby.base_view import BaseView as BaseView
from last_stand.gui.impl.lobby.ls_helpers import fillRewards as fillRewards
from last_stand.gui.impl.lobby.tooltips.booster_tooltip import BoosterTooltipView as BoosterTooltipView
from last_stand.gui.sounds import playSound as playSound
from last_stand.gui.sounds.sound_constants import RewardState as RewardState, REWARD_WINDOW_ENTER as REWARD_WINDOW_ENTER, REWARD_WINDOW_EXIT as REWARD_WINDOW_EXIT
from last_stand.skeletons.ls_artefacts_controller import ILSArtefactsController as ILSArtefactsController
from helpers import dependency as dependency
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from last_stand.skeletons.ls_difficulty_missions_controller import ILSDifficultyMissionsController as ILSDifficultyMissionsController
from frameworks.wulf import ViewEvent as ViewEvent, View as View
_R_BACKPORT_TOOLTIP: Any

class StageRewardView(BaseView):
    lsArtifactsCtrl: Any
    lsDifficultyMissionsCtrl: Any
    _MAX_BONUSES_IN_VIEW = 12
    __idGen: Any
    __resourceID: Any
    __isReward: Any
    __bonusCache: Any
    def __init__(self, resourceID, isReward):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __onClose(self):
        ...
    def __fillViewModel(self):
        ...

class StageRewardWindow(LobbyNotificationWindow):
    __args: Any
    def __init__(self, resourceID, isReward=False, parent=None):
        ...
    def isParamsEqual(self, *args):
        ...
