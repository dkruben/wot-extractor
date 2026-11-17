# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/upgradable_device/UpgradeDeviceView.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from frameworks.wulf import Array as Array
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.impl import backport as backport
from gui.impl.dialogs.dialog_template import DialogTemplateView as DialogTemplateView
from gui.impl.dialogs.dialog_template_button import CancelButton as CancelButton, ConfirmButton as ConfirmButton
from gui.impl.gen import R as R
from gui.impl.gen.view_models.constants.item_highlight_types import ItemHighlightTypes as ItemHighlightTypes
from gui.impl.gen.view_models.views.lobby.tank_setup.device_upgrade_dialog_model import DeviceUpgradeDialogModel as DeviceUpgradeDialogModel
from gui.impl.gen.view_models.views.lobby.tank_setup.dialogs.main_content.kpi_item_model import KpiItemModel as KpiItemModel
from gui.impl.lobby.tank_setup.dialogs.dialog_helpers.balance import initBalance as initBalance
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
from gui.shared.event_dispatcher import showDeconstructionDeviceWindow as showDeconstructionDeviceWindow
from gui.shared.gui_items import getKpiValueString as getKpiValueString, GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.money import Currency as Currency
from gui.shared.tooltips.common import getSimpleTooltipFactory as getSimpleTooltipFactory
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from gui.Scaleform.genConsts.STORE_CONSTANTS import STORE_CONSTANTS as STORE_CONSTANTS
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.app_loader import IAppLoader as IAppLoader
_logger: Any

class UpgradableDeviceUpgradeConfirmView(DialogTemplateView):
    __slots__: tuple
    __itemsCache: Any
    __appLoader: Any
    VIEW_MODEL = DeviceUpgradeDialogModel
    LAYOUT_ID: Any
    __currentModule: Any
    __upgradePrice: Any
    __vehicle: Any
    __onDeconstructed: Any
    def __init__(self, currentModule, vehicle=None, onDeconstructed=None):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _setResult(self, result):
        ...
    def __canPurchaseUpgrade(self):
        ...
    def __canGetMoreCurrency(self):
        ...
    def __initBalance(self):
        ...
    def __setUpgradeCost(self):
        ...
    def __onMoneyUpdated(self, _):
        ...
    def __getConfirmButtonTxtRes(self):
        ...
    def __optDevicesUpdated(self, _, diff):
        ...
    def __updateUpgradeStatus(self):
        ...
    def __getSubmitTooltipFactory(self):
        ...
    def __isSubmitDisabled(self, canGetMoreCurrency=None):
        ...

def _fillDeviceInfo(modules, currentModule, viewModel):
    ...
def _getDowngradeInfo(result, device):
    ...
def _getUpgradeInfo(result, device):
    ...
