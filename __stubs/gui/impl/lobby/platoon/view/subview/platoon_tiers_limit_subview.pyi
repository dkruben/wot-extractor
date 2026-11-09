# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/platoon/view/subview/platoon_tiers_limit_subview.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from account_helpers.settings_core.settings_constants import GAME as GAME
from constants import Configs as Configs
from frameworks.wulf import ViewEvent as ViewEvent, View as View
from gui.impl.pub.view_impl import ViewImpl as ViewImpl
from frameworks.wulf import ViewSettings as ViewSettings
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.game_control import IPlatoonController as IPlatoonController
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.platoon.tiers_limit_model import TiersLimitModel as TiersLimitModel
from gui.shared.formatters.ranges import toRomanRangeString as toRomanRangeString
from gui.impl.lobby.platoon.platoon_helpers import convertTierFilterToList as convertTierFilterToList
from gui.impl.lobby.platoon.tooltip.platoon_alert_tooltip import AlertTooltip as AlertTooltip
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from gui.impl import backport as backport
_logger: Any
_strButtons = R.strings.platoon.buttons

class TiersLimitSubview(ViewImpl):
    __platoonCtrl: Any
    __lobbyContext: Any
    __settingsCore: Any
    __isShowingSettings: Any
    __showSettingsCallback: Any
    __searchFlags: Any
    __tiersString: Any
    __isExpanded: Any
    def __init__(self):
        ...
    def resetState(self):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def hideSettings(self):
        ...
    def setShowCallback(self, func):
        ...
    def update(self, *args):
        ...
    def _finalize(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    def __onServerSettingsChange(self, diff):
        ...
    def __updateViewModel(self):
        ...
    def __onSettingsChanged(self, diff):
        ...
    def __updateTierFilterString(self):
        ...
    def __onReset(self):
        ...
    def __onShow(self):
        ...
    def __onMembersUpdate(self):
        ...
    def __updateSettingsButtonIsPressedState(self):
        ...
