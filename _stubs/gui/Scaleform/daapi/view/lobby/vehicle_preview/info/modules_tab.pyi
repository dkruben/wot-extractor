# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/info/modules_tab.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle
from account_helpers.settings_core.ServerSettingsManager import SETTINGS_SECTIONS as SETTINGS_SECTIONS
from gui.Scaleform.daapi.view.lobby.shared.fitting_slot_vo import FittingSlotVO as FittingSlotVO
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.Scaleform.daapi.view.meta.ModulesPanelMeta import ModulesPanelMeta as ModulesPanelMeta
from gui.Scaleform.daapi.view.meta.VehiclePreviewModulesTabMeta import VehiclePreviewModulesTabMeta as VehiclePreviewModulesTabMeta
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.shared import event_dispatcher as shared_events
from gui.shared.formatters import text_styles as text_styles, icons as icons
from gui.shared.gui_items import GUI_ITEM_TYPE_NAMES as GUI_ITEM_TYPE_NAMES, GUI_ITEM_TYPE_INDICES as GUI_ITEM_TYPE_INDICES
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from gui.shared.utils.vehicle_collector_helper import wasModulesAnimationShown as wasModulesAnimationShown
from helpers import dependency as dependency
from items import ITEM_TYPES as ITEM_TYPES
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.shared import IItemsCache as IItemsCache
_MODULE_SLOTS: tuple

class VehiclePreviewModulesTab(VehiclePreviewModulesTabMeta):
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def setActiveState(self, isActive):
        ...
    def update(self):
        ...
    @classmethod
    def __makeStatusInfo(cls):
        ...
    @staticmethod
    def __needToShowAnim():
        ...

class ModulesPanel(ModulesPanelMeta):
    __settingsCore: Any
    __itemsCache: Any
    __hasCounter: Any
    def __init__(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def update(self, *args):
        ...
    def showModuleInfo(self, moduleId):
        ...
    def _update(self):
        ...
    def __setHasCounter(self, devices):
        ...
    def __onSettingsChanged(self, diff):
        ...

def _makeStatusText(textRes, iconRes, style):
    ...
def _makeStatusIcon(iconRes):
    ...
