# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/reward_selection_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
from adisp import adisp_process as adisp_process
from frameworks.wulf import WindowFlags as WindowFlags, ViewSettings as ViewSettings
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow, createTooltipData as createTooltipData
from gui.impl.gen import R as R
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.server_events.awards_formatters import AWARDS_SIZES as AWARDS_SIZES
from gui.server_events.recruit_helper import getRecruitInfo as getRecruitInfo
from halloween.gui.impl.gen.view_models.views.lobby.reward_selection_view_model import RewardSelectionViewModel as RewardSelectionViewModel, GenderEnum as GenderEnum
from halloween.gui.impl.gen.view_models.views.lobby.reward_view_model import RewardViewModel as RewardViewModel
from halloween.gui.impl.lobby.base_view import BaseView as BaseView
from halloween.gui.impl.lobby.hw_helpers import getImgName as getImgName, HalloweenBonusesAwardsComposer as HalloweenBonusesAwardsComposer
from halloween.gui.impl.lobby.hw_helpers.bonuses_formatters import getHWTwitchAwardFormatter as getHWTwitchAwardFormatter
from halloween.skeletons.halloween_artefacts_controller import IHalloweenArtefactsController as IHalloweenArtefactsController
from halloween.skeletons.halloween_twitch_con_controller import IHalloweenTwitchConController as IHalloweenTwitchConController
from helpers import dependency as dependency
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from skeletons.gui.impl import IGuiLoader as IGuiLoader
_R_BACKPORT_TOOLTIP: Any

class RewardSelectionView(BaseView):
    _MAX_BONUSES_IN_VIEW = 1
    _guiLoader: Any
    _hwArtifactsCtrl: Any
    _hwTwitchCtrl: Any
    __bonusCache: Any
    __idGen: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTip(self, event):
        ...
    def _getEvents(self):
        ...
    def __onClose(self):
        ...
    def __onClaim(self, args):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __fillViewModel(self):
        ...
    # decorador original: @adisp_process
    def __processSelection(self, data):
        ...

class RewardSelectionWindow(LobbyNotificationWindow):
    _args: Any
    def __init__(self, layoutID, parent=None):
        ...
    def isParamsEqual(self, *args):
        ...
