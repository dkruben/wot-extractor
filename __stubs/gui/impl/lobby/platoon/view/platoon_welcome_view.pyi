# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/platoon/view/platoon_welcome_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from gui.impl.lobby.platoon.platoon_helpers import getPlatoonBonusState as getPlatoonBonusState, BonusState as BonusState
from helpers import dependency as dependency
from gui.impl import backport as backport
from gui.impl.gen import R as R
from skeletons.gui.game_control import IPlatoonController as IPlatoonController
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.lobby.platoon.view.platoon_search_view import SearchView as SearchView
from gui.impl.gen.view_models.views.lobby.platoon.platoon_dropdown_model import PlatoonDropdownModel as PlatoonDropdownModel
from gui.impl.lobby.platoon.view.subview.platoon_tiers_filter_subview import TiersFilterSubview as TiersFilterSubview
from gui.impl.lobby.platoon.view.subview.platoon_tiers_limit_subview import TiersLimitSubview as TiersLimitSubview
from gui.impl.lobby.premacc.squad_bonus_tooltip_content import SquadBonusTooltipContent as SquadBonusTooltipContent
from gui.shared.events import PlatoonDropdownEvent as PlatoonDropdownEvent
from constants import QUEUE_TYPE as QUEUE_TYPE, Configs as Configs
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from gui.impl.lobby.platoon.tooltip.platoon_alert_tooltip import AlertTooltip as AlertTooltip
from gui.shared import g_eventBus as g_eventBus
from gui.prb_control.settings import REQUEST_TYPE as REQUEST_TYPE
_logger: Any
strButtons = R.strings.platoon.buttons

class WelcomeView(ViewImpl):
    __platoonCtrl: Any
    __lobbyContext: Any
    _layoutID: Any
    __tiersLimitSubview: Any
    __tiersFilterSubview: Any
    __prbEntityType: Any
    def __init__(self, layoutID=None):
        ...
    @property
    def _viewModelClass(self):
        ...
    def getPrbEntityType(self):
        ...
    def _finalize(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def update(self, updateTiersLimitSubview=True):
        ...
    def hideSettings(self):
        ...
    def _initButtons(self):
        ...
    def _addListeners(self):
        ...
    def _removeListeners(self):
        ...
    def _onOutsideClick(self):
        ...
    def __updateFindButton(self, *args):
        ...
    def __onServerSettingsChange(self, diff):
        ...
    def __showSettingsCallback(self, state):
        ...
    def __onCreate(self):
        ...
    def _onFind(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _setBattleTypeRelatedProps(self):
        ...
    def __onAvailableTiersForSearchChanged(self):
        ...
