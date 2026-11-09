# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/account_dashboard/features/header_feature.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import BigWorld as BigWorld
from WeakMethod import WeakMethodProxy as WeakMethodProxy
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.clans.settings import getClanRoleName as getClanRoleName
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.lobby.account_completion.tooltips.hangar_tooltip_view import HangarTooltipView as HangarTooltipView
from gui.impl.lobby.account_dashboard.features.base import FeatureItem as FeatureItem
from gui.impl.lobby.tooltips.clans import ClanShortInfoTooltipContent as ClanShortInfoTooltipContent
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.platform.base.statuses.constants import StatusTypes as StatusTypes
from gui.shared import event_dispatcher as event_dispatcher
from gui.shared.event_dispatcher import showSteamConfirmEmailOverlay as showSteamConfirmEmailOverlay, showSteamAddEmailOverlay as showSteamAddEmailOverlay
from gui.shared.view_helpers.emblems import EmblemSize as EmblemSize, getClanEmblemURL as getClanEmblemURL
from helpers import dependency as dependency
from skeletons.gui.game_control import IBadgesController as IBadgesController, ISteamCompletionController as ISteamCompletionController, IPlatoonController as IPlatoonController
from skeletons.gui.platform.wgnp_controllers import IWGNPSteamAccRequestController as IWGNPSteamAccRequestController
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.web import IWebController as IWebController
from wg_async import wg_async as wg_async, wg_await as wg_await
from gui.impl.gen.view_models.views.lobby.account_dashboard.header_model import HeaderModel as HeaderModel
from gui.platform.wgnp.steam_account.statuses import SteamAccEmailStatus as SteamAccEmailStatus
_logger: Any

class HeaderFeature(FeatureItem):
    __itemsCache: Any
    __webCtrl: Any
    __badgesController: Any
    __wgnpSteamAccCtrl: Any
    __steamRegistrationCtrl: Any
    __platoonCtrl: Any
    __notConfirmedEmail: Any
    __isDestroyed: Any
    __confirmationWindow: Any
    _tooltipModelFactories: Any
    def __init__(self, viewModel):
        ...
    def initialize(self, *args, **kwargs):
        ...
    def finalize(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _fillModel(self, model):
        ...
    # decorador original: @replaceNoneKwargsModel
    def _setEmailConfirmed(self, status=None, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def _setEmailActionNeeded(self, status=None, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def _updateClanInfo(self, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def _updateBadges(self, model=None):
        ...
    def __createHangarTooltipView(self):
        ...
    def __onClanInfoChanged(self, _):
        ...
    def __onBadgesChanged(self):
        ...
    @staticmethod
    def __setBadge(setter, badge):
        ...
    @staticmethod
    def __onShowBadges():
        ...
    def __onAccountInfoButtonClick(self):
        ...
    def __onEmailButtonClicked(self):
        ...
    # decorador original: @wg_async
    def __askEmailStatus(self):
        ...
