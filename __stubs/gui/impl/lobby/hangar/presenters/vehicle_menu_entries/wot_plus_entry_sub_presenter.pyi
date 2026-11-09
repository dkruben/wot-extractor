# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/presenters/vehicle_menu_entries/wot_plus_entry_sub_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
from time import time as time
import typing as typing
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.Scaleform.genConsts.STORE_CONSTANTS import STORE_CONSTANTS as STORE_CONSTANTS
from gui.game_control.wot_plus.utils import ProBoostUtils as ProBoostUtils
from gui.impl.dialogs.dialogs import showProBoostSwitchDialog as showProBoostSwitchDialog, showProBoostConfirmDialog as showProBoostConfirmDialog
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.hangar.vehicle_menu_model import VehicleMenuModel as VehicleMenuModel
from gui.impl.lobby.dialogs.wot_plus.pro_boost_confirm_dialog import _ProBoostConfirmDialogParams as _ProBoostConfirmDialogParams
from gui.impl.lobby.dialogs.wot_plus.pro_boost_switch_dialog import _ProBoostSwitchDialogVehicleParams as _ProBoostSwitchDialogVehicleParams, _ProBoostSwitchDialogParams as _ProBoostSwitchDialogParams
from gui.impl.lobby.hangar.presenters.vehicle_menu_entries.base_menu_entry_sub_presenter import BaseMenuEntrySubPresenter as BaseMenuEntrySubPresenter, EntryStateWithReason as EntryStateWithReason
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.shared.gui_items.Vehicle import getIconShopResource as getIconShopResource
from gui.shared.utils.functions import replaceHyphenToUnderscore as replaceHyphenToUnderscore
from helpers import dependency as dependency, int2roman as int2roman
from items.vehicles import getItemByCompactDescr as getItemByCompactDescr
from renewable_subscription_common.settings_constants import PRO_BOOST_PDATA_KEY as PRO_BOOST_PDATA_KEY, RS_TIER as RS_TIER
from skeletons.gui.game_control import IWotPlusController as IWotPlusController
from skeletons.gui.shared import IItemsCache as IItemsCache
from wg_async import wg_await as wg_await, wg_async as wg_async
from typing import Any as Any, Dict as Dict, Generator as Generator
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle

class WotPlusEntrySubPresenter(BaseMenuEntrySubPresenter, IGlobalListener):
    __wotPlusCtrl: _Any
    __itemsCache: _Any
    def onPrbEntitySwitched(self):
        ...
    # decorador original: @wg_async
    def onNavigate(self):
        ...
    def _getEvents(self):
        ...
    def _getState(self):
        ...
    def __onProBoostDataChanged(self, data):
        ...
    def __getVehicleSwitchWindowParams(self, vehicle):
        ...
    def __getType48x48IconResource(self, vehicleType, isElite=False):
        ...
    def __onProBoostCooldownIsFinished(self, *args, **kwargs):
        ...
