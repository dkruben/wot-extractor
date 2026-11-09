# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/battle_results/comp7_light_battle_results_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from functools import partial as partial
from comp7_light.gui.impl.gen.view_models.views.lobby.comp7_light_battle_results_view_model import Comp7LightBattleResultsViewModel as Comp7LightBattleResultsViewModel
from comp7_light.gui.impl.lobby.battle_results.comp7_light_flag_view import Comp7LightFlagWindow as Comp7LightFlagWindow
from comp7_light.gui.impl.lobby.battle_results.submodel_presenters.comp7_light_sub_presenter import Comp7LightBattleResultsSubPresenter as Comp7LightBattleResultsSubPresenter
from comp7_light.gui.impl.lobby.battle_results.missions_progress.progress_presenter_helpers import getComp7LightProgressionCategoriesPresenters as getComp7LightProgressionCategoriesPresenters
from comp7_core.gui.battle_results.components.comp7_core_components import checkIfDeserter as checkIfDeserter
from fairplay_violation_types import FairplayViolations as FairplayViolations
from frameworks.wulf import WindowFlags as WindowFlags
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.impl.gen import R as R
from gui.impl.lobby.battle_results.sounds import RANDOM_BATTLE_RESULTS_SOUND_SPACE as RANDOM_BATTLE_RESULTS_SOUND_SPACE
from gui.impl.lobby.battle_results.submodel_presenters.battle_achievements import BattleAchievementsSubPresenter as BattleAchievementsSubPresenter
from gui.impl.lobby.user_missions.hub.hub_view import DailyTabs as DailyTabs
from gui.impl.pub import WindowImpl as WindowImpl
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.lobby_state_machine.routable_view import IRoutableView as IRoutableView
from gui.lobby_state_machine.router import SubstateRouter as SubstateRouter
from gui.server_events.events_dispatcher import showDailyQuests as showDailyQuests
from gui.shared.view_helpers.blur_manager import ImmediateSceneBlurConfig as ImmediateSceneBlurConfig
from gui.sounds.ambients import BattleResultsEnv as BattleResultsEnv
from helpers import dependency as dependency
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.battle_results import IBattleResultsService as IBattleResultsService
from skeletons.gui.game_control import IBlurController as IBlurController
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from skeletons.gui.game_control import IBlurEffect as IBlurEffect

class Comp7LightBattleResultsWindow(WindowImpl):
    def __init__(self, layer, **kwargs):
        ...

# base nao representavel no stub: ViewComponent[...]
class Comp7LightBattleResultsView(IRoutableView):
    __battleResults: Any
    __blurCtrl: Any
    __connectionMgr: Any
    __hangarSpace: Any
    __localStorage = ''
    _COMMON_SOUND_SPACE = RANDOM_BATTLE_RESULTS_SOUND_SPACE
    __sound_env__ = BattleResultsEnv
    _POST_BATTLE_BLUR_SETTINGS_KEY = 'maximum'
    __arenaUniqueID: Any
    __subPresenter: Any
    __flagWindow: Any
    __router: Any
    __blur: Any
    def __init__(self, ctx, *args, **kwargs):
        ...
    @property
    def arenaUniqueID(self):
        ...
    @property
    def blur(self):
        ...
    @property
    def viewModel(self):
        ...
    def getRouterModel(self):
        ...
    def createContextMenu(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    @classmethod
    def getLocalStorage(cls):
        ...
    @classmethod
    def saveLocalStorage(cls, ctx):
        ...
    def _getChildComponents(self):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onClose(self):
        ...
    def _onOpenMissions(self):
        ...
    def __createFlagWindow(self):
        ...
