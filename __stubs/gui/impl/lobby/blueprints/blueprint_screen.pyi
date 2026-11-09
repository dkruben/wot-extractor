# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/blueprints/blueprint_screen.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import nations as nations
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import VEHICLES_WITH_BLUEPRINT_CONFIRM as VEHICLES_WITH_BLUEPRINT_CONFIRM, STORAGE_BLUEPRINTS_CAROUSEL_FILTER as STORAGE_BLUEPRINTS_CAROUSEL_FILTER
from adisp import adisp_process as adisp_process
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from wg_async import wg_async as wg_async, wg_await as wg_await
from blueprints.BlueprintTypes import BlueprintTypes as BlueprintTypes
from frameworks.wulf import ViewSettings as ViewSettings
from frameworks.wulf.gui_constants import ViewFlags as ViewFlags, ViewStatus as ViewStatus
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.daapi.view.lobby.techtree.techtree_dp import g_techTreeDP as g_techTreeDP
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.backport import createTooltipData as createTooltipData, BackportTooltipWindow as BackportTooltipWindow
from gui.impl.dialogs import dialogs as dialogs
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.blueprints.blueprint_screen_model import BlueprintScreenModel as BlueprintScreenModel
from gui.impl.gen.view_models.views.lobby.blueprints.blueprint_screen_scheme_item_model import BlueprintScreenSchemeItemModel as BlueprintScreenSchemeItemModel
from gui.impl.gen.view_models.views.lobby.blueprints.blueprint_screen_tooltips import BlueprintScreenTooltips as BlueprintScreenTooltips
from gui.impl.gen.view_models.views.lobby.blueprints.blueprint_value_price import BlueprintValuePrice as BlueprintValuePrice
from gui.impl.lobby.blueprints import getBlueprintTooltipData as getBlueprintTooltipData
from gui.impl.lobby.blueprints.fragments_balance_content import FragmentsBalanceContent as FragmentsBalanceContent
from gui.impl.pub import ViewImpl as ViewImpl
from gui.server_events.formatters import DISCOUNT_TYPE as DISCOUNT_TYPE
from gui.shared import event_dispatcher as event_dispatcher
from gui.shared.gui_items.items_actions import factory as factory
from gui.shared.gui_items.items_actions.actions import UnlockItemActionWithResult as UnlockItemActionWithResult
from gui.shared.utils.functions import getVehTypeIconName as getVehTypeIconName
from gui.shared.utils.requesters.blueprints_requester import SPECIAL_BLUEPRINT_LEVEL as SPECIAL_BLUEPRINT_LEVEL, getNationalFragmentCD as getNationalFragmentCD
from helpers import dependency as dependency, int2roman as int2roman
from helpers.blueprint_generator import g_blueprintGenerator as g_blueprintGenerator
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.shared import IItemsCache as IItemsCache

class BlueprintScreen(ViewImpl):
    __itemsCache: Any
    __connectionMgr: Any
    __slots__: tuple
    __vehicle: Any
    __xpCost: Any
    __fullXpCost: Any
    __discount: Any
    __convertedIndexes: Any
    __accountSettings: Any
    def __init__(self, viewKey, viewModelClazz=..., ctx=None):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTip(self, event):
        ...
    def _initialize(self):
        ...
    def _finalize(self):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    # decorador original: @wg_async
    def __onGoToConversionScreen(self, args):
        ...
    # decorador original: @wg_async
    def __onGoToAllConversion(self, _=None):
        ...
    def __onCloseAction(self):
        ...
    def __onSubmitUnavailableConfirm(self):
        ...
    def __onOpenVehicleViewBtnClicked(self):
        ...
    # decorador original: @adisp_process
    def __onResearchVehicle(self, _=None):
        ...
    def __onBlueprintsSettingsChanged(self, diff):
        ...
    def __onUpdateBlueprints(self, _):
        ...
    def __onUnlockVehicle(self, unlocks):
        ...
    def __onUpdateXP(self, _):
        ...
    def __checkIsVehicleAvailable(self):
        ...
    def __updateConversionData(self, model):
        ...
    def __updateResearchPrice(self):
        ...
    def __isConversionAvailable(self):
        ...
    def __getLayout(self):
        ...
    def __getConvertedIndexes(self, layout=None):
        ...
    def __updateLayout(self, model, layout):
        ...
    def __getTooltipData(self, ttId, itemCD):
        ...
