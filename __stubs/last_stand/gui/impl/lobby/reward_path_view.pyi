# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/reward_path_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow, createTooltipData as createTooltipData
from gui.impl.pub import WindowImpl as WindowImpl
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from last_stand.gui.impl.gen.view_models.views.lobby.reward_path_artefact_view_model import RewardPathArtefactViewModel as RewardPathArtefactViewModel
from last_stand.gui.impl.lobby.base_view import SwitcherPresenter as SwitcherPresenter
from last_stand.gui.impl.lobby.gsw_cards.quests_card_presenter import QuestsCardPresenter as QuestsCardPresenter
from last_stand.gui.impl.lobby.ls_helpers import fillRewards as fillRewards
from last_stand.gui.impl.lobby.tooltips.additional_data_tooltip import AdditionalDataTooltipView as AdditionalDataTooltipView
from last_stand.gui.impl.lobby.tooltips.booster_tooltip import BoosterTooltipView as BoosterTooltipView
from last_stand.gui.impl.lobby.tooltips.points_tooltip import PointsTooltipView as PointsTooltipView
from last_stand.gui.impl.lobby.widgets.bundle_card import BundleCard as BundleCard
from last_stand.gui.sounds import playSound as playSound
from last_stand.gui.sounds.sound_constants import REWARD_PATH_EXIT as REWARD_PATH_EXIT, REWARD_PATH_ENTER as REWARD_PATH_ENTER
from last_stand.skeletons.difficulty_level_controller import IDifficultyLevelController as IDifficultyLevelController
from last_stand.skeletons.ls_controller import ILSController as ILSController
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from frameworks.wulf import WindowFlags as WindowFlags
from gui.impl.gen import R as R
from gui.shared import g_eventBus as g_eventBus, events as events
from last_stand.gui.impl.gen.view_models.views.lobby.reward_path_view_model import RewardPathViewModel as RewardPathViewModel
from last_stand.gui.shared.event_dispatcher import showMetaIntroView as showMetaIntroView
from last_stand.skeletons.ls_artefacts_controller import ILSArtefactsController as ILSArtefactsController
from helpers import dependency as dependency
from last_stand.gui.game_control.ls_artefacts_controller import Artefact as Artefact
from frameworks.wulf import ViewEvent as ViewEvent, View as View
_R_BACKPORT_TOOLTIP: Any

# base nao representavel no stub: ViewComponent[...]
class RewardPathView:
    lsCtrl: Any
    lsArtefactsCtrl: Any
    difficultyCtrl: Any
    _MAX_BONUSES_IN_VIEW = 6
    __bonusCache: Any
    __openFromQuestCard: Any
    __idGen: Any
    def __init__(self, ctx, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getChildComponents(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __fillItems(self):
        ...
    def __fillArtefacts(self, tx):
        ...
    def __onClose(self):
        ...
    def __onViewLoaded(self):
        ...
    def __onPointsUpdated(self):
        ...
    def __onArtefactStatusUpdated(self, *args):
        ...

class RewardPathWindow(WindowImpl):
    def __init__(self, layer, *args, **kwargs):
        ...
