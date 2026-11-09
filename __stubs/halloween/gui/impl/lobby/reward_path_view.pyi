# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/reward_path_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow, createTooltipData as createTooltipData
from gui.impl.pub import WindowImpl as WindowImpl
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.shared.event_dispatcher import showVehicleHubOverview as showVehicleHubOverview
from halloween.gui.impl.gen.view_models.views.lobby.reward_path_item_view_model import RewardPathItemViewModel as RewardPathItemViewModel
from halloween.gui.impl.lobby.gsw_cards.key_card_presenter import KeyCardPresenter as KeyCardPresenter
from halloween.gui.impl.lobby.gsw_cards.quests_card_presenter import QuestsCardPresenter as QuestsCardPresenter
from halloween.gui.impl.lobby.hw_helpers import getArtefactState as getArtefactState, fillRewards as fillRewards, fillGiftVehicleModel as fillGiftVehicleModel
from halloween.gui.impl.lobby.base_view import SwitcherPresenter as SwitcherPresenter
from halloween.gui.impl.lobby.tooltips.event_mission_tooltip import MissionsTooltip as MissionsTooltip
from halloween.gui.impl.lobby.tooltips.vehicle_tooltip import VehicleTooltipView as VehicleTooltipView
from halloween.gui.sounds import playSound as playSound
from halloween.gui.sounds.sound_constants import REWARD_PATH_EXIT as REWARD_PATH_EXIT, REWARD_PATH_ENTER as REWARD_PATH_ENTER
from halloween.skeletons.halloween_controller import IHalloweenController as IHalloweenController
from halloween.skeletons.halloween_twitch_con_controller import IHalloweenTwitchConController as IHalloweenTwitchConController
from halloween.uilogging.loggers import HWMetricsLogger as HWMetricsLogger
from halloween.uilogging.logging_constants import HWLogKeys as HWLogKeys
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle
from frameworks.wulf import WindowFlags as WindowFlags
from gui.impl.gen import R as R
from gui.shared import g_eventBus as g_eventBus, events as events
from halloween.gui.impl.gen.view_models.views.lobby.reward_path_view_model import RewardPathViewModel as RewardPathViewModel
from halloween.gui.impl.lobby.widgets.crew_members_flag import CrewMembersFlag as CrewMembersFlag
from halloween.gui.shared.event_dispatcher import showTwitchConExchangeView as showTwitchConExchangeView, showMetaIntroView as showMetaIntroView
from halloween.skeletons.halloween_artefacts_controller import IHalloweenArtefactsController as IHalloweenArtefactsController
from helpers import dependency as dependency
from halloween.gui.game_control.halloween_artefacts_controller import Artefact as Artefact
_R_BACKPORT_TOOLTIP: Any

# base nao representavel no stub: ViewComponent[...]
class RewardPathView:
    _hwController: Any
    _hwArtefactsCtrl: Any
    _hwTwitchConCtrl: Any
    _MAX_BONUSES_IN_VIEW = 3
    __bonusCache: Any
    __idGen: Any
    __uiLogger: Any
    def __init__(self, *args, **kwargs):
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
    def _onLoaded(self, *args, **kwargs):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __goToMission(self, args):
        ...
    def __goToCrewSelect(self):
        ...
    def __fillArtefacts(self):
        ...
    def __fillGiftVehicle(self):
        ...
    def __onPreview(self):
        ...
    def __onClose(self):
        ...
    def __onViewLoaded(self):
        ...
    def __getArtefactsIDsWithReceivedCert(self):
        ...

class RewardPathWindow(WindowImpl):
    def __init__(self, layer, *args, **kwargs):
        ...
