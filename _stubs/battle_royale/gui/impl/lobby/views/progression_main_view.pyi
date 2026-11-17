# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/progression_main_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from future.utils import viewvalues as viewvalues
from battle_royale.gui.impl.gen.view_models.views.lobby.views.progression.progression_main_view_model import ProgressionMainViewModel as ProgressionMainViewModel, MainViews as MainViews
from battle_royale.gui.impl.lobby.views.progression_view import ProgressionView as ProgressionView
from battle_royale.gui.sounds_constants import GENERAL_SOUND_SPACE as GENERAL_SOUND_SPACE
from battle_royale.gui.impl.lobby.tooltips.leaderboard_reward_tooltip_view import LeaderboardRewardTooltipView as LeaderboardRewardTooltipView
from frameworks.wulf import WindowFlags as WindowFlags, ViewSettings as ViewSettings
from frameworks.wulf.view.submodel_presenter import SubModelPresenter as SubModelPresenter
from gui.impl.lobby.common.tooltips.extended_text_tooltip import ExtendedTextTooltip as ExtendedTextTooltip
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl
from typing import Dict as Dict

class BattleRoyaleProgressionWindow(WindowImpl):
    def __init__(self, layer, **kwargs):
        ...

class BattleRoyaleProgressionMainView(ViewImpl):
    _COMMON_SOUND_SPACE = GENERAL_SOUND_SPACE
    __viewType: Any
    __ctx: Any
    __contentPresentersMap: Any
    def __init__(self, layoutId, *args, **kwargs):
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
