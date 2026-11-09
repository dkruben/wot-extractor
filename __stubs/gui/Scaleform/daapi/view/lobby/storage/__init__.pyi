# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/storage/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import WindowLayer as WindowLayer
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.storage.customization.customization_cm_handlers import CustomizationCMHandler as CustomizationCMHandler
from gui.Scaleform.daapi.view.lobby.storage.customization.customization_view import StorageCategoryCustomizationView as StorageCategoryCustomizationView
from gui.Scaleform.daapi.view.common.filter_popover import StorageBlueprintsFilterPopover as StorageBlueprintsFilterPopover
from gui.Scaleform.daapi.view.lobby.storage.blueprints.blueprints_cm_handlers import BlueprintsCMHandler as BlueprintsCMHandler
from gui.Scaleform.daapi.view.lobby.storage.blueprints.blueprints_storage_view import StorageCategoryBlueprintsView as StorageCategoryBlueprintsView
from gui.Scaleform.daapi.view.lobby.storage.forsell.for_sell_view import StorageCategoryForSellView as StorageCategoryForSellView
from gui.Scaleform.daapi.view.lobby.storage.forsell.forsell_cm_handlers import ForSellCMHandler as ForSellCMHandler
from gui.Scaleform.daapi.view.lobby.storage.inhangar.all_vehicles_tab import AllVehiclesTabView as AllVehiclesTabView
from gui.Scaleform.daapi.view.lobby.storage.inhangar.in_hangar_view import StorageCategoryInHangarView as StorageCategoryInHangarView
from gui.Scaleform.daapi.view.lobby.storage.inhangar.in_hangar_view import StorageVehicleFilterPopover as StorageVehicleFilterPopover
from gui.Scaleform.daapi.view.lobby.storage.inhangar.inhangar_cm_handlers import VehiclesRegularCMHandler as VehiclesRegularCMHandler
from gui.Scaleform.daapi.view.lobby.storage.inhangar.inhangar_cm_handlers import VehiclesRestoreCMHandler as VehiclesRestoreCMHandler
from gui.Scaleform.daapi.view.lobby.storage.inhangar.inhangar_cm_handlers import VehiclesRentedCMHandler as VehiclesRentedCMHandler
from gui.Scaleform.daapi.view.lobby.storage.inhangar.rent_vehicles_tab import RentVehiclesTabView as RentVehiclesTabView
from gui.Scaleform.daapi.view.lobby.storage.inhangar.restore_vehicles_tab import RestoreVehiclesTabView as RestoreVehiclesTabView
from gui.Scaleform.daapi.view.lobby.storage.inventory.consumables_tab import ConsumablesTabView as ConsumablesTabView
from gui.Scaleform.daapi.view.lobby.storage.inventory.inventory_cm_handlers import ModulesShellsCMHandler as ModulesShellsCMHandler, ModulesShellsNoSaleCMHandler as ModulesShellsNoSaleCMHandler, DemountKitsCMHandler as DemountKitsCMHandler, RecertificationFormsCMHandler as RecertificationFormsCMHandler, MentoringLicensesCMHandler as MentoringLicensesCMHandler
from gui.Scaleform.daapi.view.lobby.storage.inventory.inventory_cm_handlers import EquipmentCMHandler as EquipmentCMHandler
from gui.Scaleform.daapi.view.lobby.storage.inventory.inventory_cm_handlers import BattleBoostersCMHandler as BattleBoostersCMHandler
from gui.Scaleform.daapi.view.lobby.storage.inventory.inventory_cm_handlers import OptionalDeviceCMHandler as OptionalDeviceCMHandler
from gui.Scaleform.daapi.view.lobby.storage.inventory.inventory_cm_handlers import OptionalModernizedDeviceCMHandler as OptionalModernizedDeviceCMHandler
from gui.Scaleform.daapi.view.lobby.storage.inventory.inventory_view import InventoryCategoryStorageView as InventoryCategoryStorageView
from gui.Scaleform.daapi.view.lobby.storage.inventory.modules_tab import ModulesTabView as ModulesTabView
from gui.Scaleform.daapi.view.lobby.storage.inventory.opt_devices_tab import OptDevicesTabView as OptDevicesTabView
from gui.Scaleform.daapi.view.lobby.storage.inventory.regular_items_tab import RegularItemsTabView as RegularItemsTabView
from gui.Scaleform.daapi.view.lobby.storage.inventory.select_vehicle_popover import VehicleSelectPopover as VehicleSelectPopover
from gui.Scaleform.daapi.view.lobby.storage.inventory.shells_tab import ShellsTabView as ShellsTabView
from gui.Scaleform.daapi.view.lobby.storage.inventory.crew_books_tab import CrewBooksTabView as CrewBooksTabView
from gui.Scaleform.daapi.view.lobby.storage.offers.offers_view import StorageCategoryOffersView as StorageCategoryOffersView
from gui.Scaleform.daapi.view.lobby.storage.personalreserves.boosters_cm_handlers import PersonalReservesCMHandler as PersonalReservesCMHandler
from gui.Scaleform.daapi.view.lobby.storage.personalreserves.boosters_view import StorageCategoryPersonalReservesView as StorageCategoryPersonalReservesView
from gui.Scaleform.framework import ViewSettings as ViewSettings, ScopeTemplates as ScopeTemplates, GroupedViewSettings as GroupedViewSettings, ComponentSettings as ComponentSettings
from gui.Scaleform.framework.package_layout import PackageBusinessHandler as PackageBusinessHandler
from gui.Scaleform.genConsts.CONTEXT_MENU_HANDLER_TYPE import CONTEXT_MENU_HANDLER_TYPE as CONTEXT_MENU_HANDLER_TYPE
from gui.Scaleform.genConsts.STORAGE_CONSTANTS import STORAGE_CONSTANTS as STORAGE_CONSTANTS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.app_loader import settings as app_settings
from gui.impl.lobby.offers.offer_gifts_window import OfferGiftsWindow as OfferGiftsWindow
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE

class StoragePackageBusinessHandler(PackageBusinessHandler):
    def __init__(self):
        ...

def getContextMenuHandlers():
    ...
def getViewSettings():
    ...
def getSectionsList():
    ...
def getBusinessHandlers():
    ...
def getStateMachineRegistrators():
    ...
