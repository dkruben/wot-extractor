# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/user_missions/hangar_widget/event_banners/comp7_tournament_event_banner.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7.gui.impl.lobby.tooltips.entry_point_tooltip_tournament import Comp7TournamentEntryPointTooltip as Comp7TournamentEntryPointTooltip
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.user_missions.constants.event_banner_state import EventBannerState as EventBannerState
from gui.impl.lobby.user_missions.hangar_widget.event_banners.event_banners_container import EventBannersContainer as EventBannersContainer
from gui.impl.lobby.user_missions.hangar_widget.event_banners.standard_event_banner import StandardEventBanner as StandardEventBanner
from gui.prb_control import prbEntityProperty as prbEntityProperty
from helpers import dependency as dependency
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from helpers.ingame_tournament_helper import IngameTournamentState as IngameTournamentState, IngameTournamentType as IngameTournamentType
from helpers.time_utils import ONE_MINUTE as ONE_MINUTE, getCurrentLocalServerTimestamp as getCurrentLocalServerTimestamp
from skeletons.gui.game_control import IIngameTournamentController as IIngameTournamentController

class Comp7TournamentEventBanner(StandardEventBanner):
    _TOURNAMENT_TYPE = None
    _BORDER_COLOR = '#FFCF5F'
    __tournamentStateBannerStateMap: dict
    __tournamentStateDescriptionMap: dict
    __tournamentController: Any
    __state: Any
    __nextMatchDate: Any
    __tournamentStartDate: Any
    __tournamentEndDate: Any
    __callbackDelayer: Any
    def __init__(self):
        ...
    @property
    def isMode(self):
        ...
    @property
    def bannerState(self):
        ...
    @property
    def borderColor(self):
        ...
    @property
    def timerText(self):
        ...
    @property
    def timerValue(self):
        ...
    @property
    def showTimerBeforeEventEnd(self):
        ...
    @property
    def eventStartDate(self):
        ...
    @property
    def eventEndDate(self):
        ...
    @property
    def introDescription(self):
        ...
    @property
    def inProgressDescription(self):
        ...
    # decorador original: @prbEntityProperty
    @classmethod
    def prbEntity(cls):
        ...
    @classmethod
    def isTournamentEntryPointAvailable(cls):
        ...
    def onAppear(self):
        ...
    def onDisappear(self):
        ...
    def prepare(self):
        ...
    def onClick(self):
        ...
    def createToolTipContent(self, event):
        ...
    def __onTournamentEntryPointUpdated(self):
        ...
    def __updateEntryPointData(self):
        ...
    def __updateTimerValue(self):
        ...
