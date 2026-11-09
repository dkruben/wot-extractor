# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/feature/fun_random_event_banner_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from account_helpers.AccountSettings import AccountSettings as AccountSettings, FUN_RANDOM_BANNER_LAST_VISITED_SEASON_BORDER as FUN_RANDOM_BANNER_LAST_VISITED_SEASON_BORDER, FUN_RANDOM_BANNER_LAST_VISIBLE_PROGRESSION_NAME as FUN_RANDOM_BANNER_LAST_VISIBLE_PROGRESSION_NAME
from adisp import adisp_process as adisp_process
from fun_random.gui.feature.fun_constants import FunSubModesState as FunSubModesState
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin as FunAssetPacksMixin, FunSubModesWatcher as FunSubModesWatcher, FunProgressionWatcher as FunProgressionWatcher
from skeletons.gui.game_control import IFunRandomController as IFunRandomController
from fun_random.gui.impl.lobby.tooltips.fun_random_entry_point_tooltip_view import FunRandomEntryPointTooltipView as FunRandomEntryPointTooltipView
from fun_random.gui.impl.lobby.common.fun_view_helpers import getFunRandomEventState as getFunRandomEventState
from gui.Scaleform.genConsts.FUNRANDOM_ALIASES import FUNRANDOM_ALIASES as FUNRANDOM_ALIASES
from gui.impl import backport as backport
from gui.impl.gen.view_models.views.lobby.user_missions.constants.event_banner_state import EventBannerState as EventBannerState
from gui.impl.lobby.user_missions.hangar_widget.event_banners.event_banners_container import EventBannersContainer as EventBannersContainer
from gui.impl.lobby.user_missions.hangar_widget.event_banners.standard_event_banner import StandardEventBanner as StandardEventBanner
from gui.impl.lobby.user_missions.hangar_widget.services import IEventsService as IEventsService
from helpers import dependency as dependency, time_utils as time_utils
from typing import Optional as Optional
from frameworks.wulf import View as View, ViewEvent as ViewEvent

class FunRandomEventBannerView(StandardEventBanner, FunProgressionWatcher, FunAssetPacksMixin, FunSubModesWatcher):
    NAME = FUNRANDOM_ALIASES.FUN_RANDOM_ENTRY_POINT
    __eventsService: Any
    __state: Any
    __timerValue: Any
    __eventStartDate: Any
    __eventEndDate: Any
    __playAppearAnim: Any
    def __init__(self):
        ...
    @property
    def isMode(self):
        ...
    @property
    def title(self):
        ...
    @property
    def introDescription(self):
        ...
    @property
    def inProgressDescription(self):
        ...
    @property
    def iconsPath(self):
        ...
    @property
    def videosPath(self):
        ...
    @property
    def borderColor(self):
        ...
    @property
    def bannerState(self):
        ...
    @property
    def eventStartDate(self):
        ...
    @property
    def eventEndDate(self):
        ...
    @property
    def playAppearAnim(self):
        ...
    @property
    def timerValue(self):
        ...
    def prepare(self):
        ...
    def createToolTipContent(self, event):
        ...
    def onClick(self):
        ...
    def onAppear(self):
        ...
    def onDisappear(self):
        ...
    def __onUpdate(self, *args):
        ...
    # decorador original: @adisp_process
    def __onSelectFunRandom(self):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def isFunRandomEntryPointAvailable(funRandomCtrl=None):
    ...
