# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/platoon/view/subview/platoon_tiers_filter_subview.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from account_helpers.settings_core.settings_constants import GAME as GAME
from constants import MIN_VEHICLE_LEVEL as MIN_VEHICLE_LEVEL, MAX_VEHICLE_LEVEL as MAX_VEHICLE_LEVEL
from gui.impl.gen.view_models.views.lobby.platoon.settings_model import SettingsModel as SettingsModel, SearchFilterTypes as SearchFilterTypes
from gui.impl.gen.view_models.views.lobby.platoon.tier_button_model import TierButtonModel as TierButtonModel
from UnitBase import UnitAssemblerSearchFlags as UnitAssemblerSearchFlags, BitfieldHelper as BitfieldHelper
from helpers import dependency as dependency
from gui.impl.gen import R as R
from skeletons.gui.game_control import IPlatoonController as IPlatoonController
from skeletons.gui.shared import IItemsCache as IItemsCache
from frameworks.wulf.view.view_model import ViewModel as ViewModel
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from gui.impl.pub.view_impl import ViewImpl as ViewImpl, PopOverViewImpl as PopOverViewImpl
from frameworks.wulf import ViewSettings as ViewSettings
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
_logger: Any

class TiersFilterSubview(ViewImpl):
    __platoonCtrl: Any
    __itemsCache: Any
    __lobbyContext: Any
    __settingsCore: Any
    def __init__(self):
        ...
    def update(self, *args):
        ...
    @property
    def viewModel(self):
        ...
    def _finalize(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __updateTierSettings(self):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    def __onSettingsChanged(self, diff):
        ...
    def __updateVoiceChat(self):
        ...
    @staticmethod
    def __createTierButton(tierArray, tier, isTierAvailable, isSelected):
        ...
    def __isTierAvailable(self, tier):
        ...
    def __onSwitchTier(self, *args, **kwargs):
        ...
    def __onSwitchVoiceChat(self):
        ...

class SettingsPopover(PopOverViewImpl):
    def __init__(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
