# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/mapbox/mapbox_progression_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from wg_async import wg_async as wg_async, wg_await as wg_await
from constants import QUEUE_TYPE as QUEUE_TYPE
from frameworks.wulf import ViewSettings as ViewSettings, ViewFlags as ViewFlags, WindowStatus as WindowStatus
from frameworks.wulf.gui_constants import ViewStatus as ViewStatus, WindowLayer as WindowLayer
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.mapbox.mapbox_progression_model import MapboxProgressionModel as MapboxProgressionModel
from gui.impl.gen.view_models.views.lobby.mapbox.progression_reward_model import ProgressionRewardModel as ProgressionRewardModel
from gui.impl.gen.view_models.views.lobby.mapbox.map_model import MapModel as MapModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.mapbox.mapbox_bonus_packers import getMapboxBonusPacker as getMapboxBonusPacker, packMapboxRewardModelAndTooltip as packMapboxRewardModelAndTooltip
from gui.mapbox.mapbox_helpers import getMapboxRewardTooltip as getMapboxRewardTooltip, prepareProgressionData as prepareProgressionData, SPECIAL_CARDS as SPECIAL_CARDS
from gui.prb_control.ctrl_events import g_prbCtrlEvents as g_prbCtrlEvents
from gui.prb_control.settings import SELECTOR_BATTLE_TYPES as SELECTOR_BATTLE_TYPES
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.meta.MissionsMapboxViewMeta import MissionsMapboxViewMeta as MissionsMapboxViewMeta
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor as InjectComponentAdaptor
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.server_events import IEventsCache as IEventsCache
from gui.shared.event_dispatcher import showHangar as showHangar, showMapboxIntro as showMapboxIntro, showBrowserOverlayView as showBrowserOverlayView
from gui.shared.formatters.time_formatters import getTillTimeByResource as getTillTimeByResource
from gui.shared.utils import SelectorBattleTypesUtils as SelectorBattleTypesUtils
from gui.shared.utils.scheduled_notifications import PeriodicNotifier as PeriodicNotifier
from helpers import dependency as dependency, time_utils as time_utils
from skeletons.gui.game_control import IMapboxController as IMapboxController
from skeletons.gui.impl import IGuiLoader as IGuiLoader
_logger: Any

class MapboxProgressionsComponent(InjectComponentAdaptor, MissionsMapboxViewMeta):
    __slots__: tuple
    def markVisited(self):
        ...
    def _makeInjectView(self):
        ...

class MapboxProgressionView(ViewImpl):
    __slots__: tuple
    __mapboxController: Any
    __eventsCache: Any
    __gui: Any
    __notifier: Any
    __showViewCallback: Any
    __tooltips: Any
    def __init__(self, showViewCallback, flags=...):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTip(self, event):
        ...
    # decorador original: @wg_async
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    def __onAnimationEnded(self, *args):
        ...
    def __onWindowStatusChanged(self, _, newState):
        ...
    def __onClose(self):
        ...
    def __onPreQueueJoined(self, prbType):
        ...
    def __onSelectMapboxBattle(self):
        ...
    def __onProgressionDataUpdated(self):
        ...
    def __onShowInfo(self):
        ...
    def __onSurveyCompleted(self, mapId):
        ...
    def __onRemoveBubble(self, args):
        ...
    def __doRemoveBubble(self, name):
        ...
    def __onShowSurvey(self, args):
        ...
    def __onSettingsUpdated(self):
        ...
    def __updateProgressionData(self, progression=None):
        ...
    def __packRewards(self, rewards, packer, rewardModelsList, tooltipsList=None):
        ...
    def __fillMaps(self, model, progressionData, actualSeason):
        ...
    def __getDeltaTime(self):
        ...
    def __getInfoPageUrl(self):
        ...
    def __setErrorStatus(self):
        ...
    def __updateProgressionAlert(self, endTime=None):
        ...
