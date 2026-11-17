# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/hangar/ammunition_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from PlayerEvents import g_playerEvents as g_playerEvents
from account_helpers.settings_core.settings_constants import OnceOnlyHints as OnceOnlyHints
from adisp import adisp_process as adisp_process, adisp_async as adisp_async
from constants import ROLE_TYPE as ROLE_TYPE
from gui import makeHtmlString as makeHtmlString
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.daapi.view.lobby.customization.shared import CustomizationTabs as CustomizationTabs
from gui.Scaleform.daapi.view.lobby.customization.shared import getItemTypesAvailableForVehicle as getItemTypesAvailableForVehicle
from gui.Scaleform.daapi.view.meta.AmmunitionPanelMeta import AmmunitionPanelMeta as AmmunitionPanelMeta
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.lobby.tank_setup.dialogs.main_content.main_contents import NeedRepairMainContent as NeedRepairMainContent
from gui.impl.lobby.tank_setup.dialogs.need_repair import NeedRepair as NeedRepair
from gui.limited_ui.lui_rules_storage import LUI_RULES as LUI_RULES
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.shared import event_dispatcher as shared_events
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from gui.shared.gui_items.gui_item_economics import getVehicleShellsLayoutPrice as getVehicleShellsLayoutPrice, getVehicleConsumablesLayoutPrice as getVehicleConsumablesLayoutPrice
from gui.shared.gui_items.items_actions import factory as ItemsActionsFactory
from gui.shared.gui_items.items_actions.actions import VehicleRepairAction as VehicleRepairAction, BuyAndInstallShells as BuyAndInstallShells, BuyAndInstallConsumables as BuyAndInstallConsumables, VehicleAutoFillLayoutAction as VehicleAutoFillLayoutAction
from gui.shared.gui_items.vehicle_helpers import getRoleMessage as getRoleMessage
from helpers import dependency as dependency, int2roman as int2roman
from renewable_subscription_common.schema import renewableSubscriptionsConfigSchema as renewableSubscriptionsConfigSchema
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.game_control import ILimitedUIController as ILimitedUIController
from skeletons.gui.shared import IItemsCache as IItemsCache
from uilogging.customization_3d_objects.logger import CustomizationAmmunitionPanelLogger as CustomizationAmmunitionPanelLogger
from uilogging.customization_3d_objects.logging_constants import CustomizationButtons as CustomizationButtons, CustomizationViewKeys as CustomizationViewKeys

class AmmunitionPanel(AmmunitionPanelMeta, IGlobalListener):
    __slots__: tuple
    __itemsCache: Any
    __service: Any
    __limitedUIController: Any
    __settingsCore: Any
    __hangarMessage: Any
    __uiCustomizationLogger: Any
    def __init__(self):
        ...
    def update(self):
        ...
    # decorador original: @adisp_process
    def showRepairDialog(self):
        ...
    def showCustomization(self):
        ...
    def toRentContinue(self):
        ...
    def showChangeNation(self):
        ...
    def showEasyTankEquip(self):
        ...
    def showModuleInfo(self, itemCD):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _update(self, onlyMoneyUpdate=False):
        ...
    def __inventoryUpdateCallBack(self, *args):
        ...
    def _onConfigModelUpdated(self, gpKey):
        ...
    def __applyCustomizationNewCounter(self, vehicle):
        ...
    @staticmethod
    def __filterAvailableCustomizations(item, vehicle):
        ...
    def __moneyUpdateCallback(self, *_):
        ...
    def __updateMaintenanceWarning(self, vehicle):
        ...
    def __highlightEasyTankEquip(self, vehicle):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def __tryAutoResupplyShells(self, callback=None):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def __tryAutoResupplyConsumables(self, callback=None):
        ...
    def __tryAutoResupplyShellsAndConsumables(self):
        ...
