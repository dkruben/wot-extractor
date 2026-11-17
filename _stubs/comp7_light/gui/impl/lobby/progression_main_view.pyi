# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/progression_main_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from future.utils import viewvalues as viewvalues
from comp7_light.gui.impl.gen.view_models.views.lobby.progression.progression_main_view_model import MainViews as MainViews, ProgressionMainViewModel as ProgressionMainViewModel
from comp7_light.gui.impl.lobby.progression_view import ProgressionView as ProgressionView
from comp7_light.gui.impl.lobby.tooltips.leaderboard_reward_tooltip import LeaderboardRewardTooltipView as LeaderboardRewardTooltipView
from comp7_light.gui.sounds_constants import GENERAL_SOUND_SPACE as GENERAL_SOUND_SPACE
from frameworks.wulf import ViewFlags as ViewFlags, WindowFlags as WindowFlags, ViewSettings as ViewSettings
from frameworks.wulf.view.submodel_presenter import SubModelPresenter as SubModelPresenter
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyWindow as LobbyWindow
from typing import Dict as Dict

class ProgressionMainView(ViewImpl):
    _COMMON_SOUND_SPACE = GENERAL_SOUND_SPACE
    __viewType: Any
    __ctx: Any
    __contentPresentersMap: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def currentPresenter(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def createToolTip(self, event):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def switchSubView(self, menuName):
        ...
    @property
    def __loadersMap(self):
        ...
    def loadProgression(self):
        ...

class ProgressionViewWindow(LobbyWindow):
    __slots__: tuple
    def __init__(self, parent=None):
        ...
