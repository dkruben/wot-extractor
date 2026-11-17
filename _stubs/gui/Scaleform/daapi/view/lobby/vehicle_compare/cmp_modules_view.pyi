# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_compare/cmp_modules_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from future.utils import iteritems as iteritems
import BigWorld as BigWorld
from adisp import adisp_process as adisp_process
from gui.Scaleform.daapi.view.lobby.techtree import dumpers as dumpers, nodes as nodes
from gui.Scaleform.daapi.view.lobby.techtree.data import ResearchItemsData as ResearchItemsData
from gui.Scaleform.daapi.view.lobby.vehicle_compare import cmp_helpers as cmp_helpers
from gui.Scaleform.daapi.view.lobby.vehicle_compare.cmp_configurator_base import VehicleCompareConfiguratorBaseView as VehicleCompareConfiguratorBaseView
from gui.Scaleform.daapi.view.meta.VehicleModulesViewMeta import VehicleModulesViewMeta as VehicleModulesViewMeta
from gui.Scaleform.genConsts.NODE_STATE_FLAGS import NODE_STATE_FLAGS as NODE_STATE_FLAGS
from gui.Scaleform.locale.VEH_COMPARE import VEH_COMPARE as VEH_COMPARE
from gui.game_control.veh_comparison_basket import getInstalledModulesCDs as getInstalledModulesCDs
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from gui.shared.gui_items.processors.module import getPreviewInstallerProcessor as getPreviewInstallerProcessor
from helpers import dependency as dependency
from helpers.i18n import makeString as _ms
from items import getTypeOfCompactDescr as getTypeOfCompactDescr
from nations import AVAILABLE_NAMES as AVAILABLE_NAMES
from gui.Scaleform.genConsts.VEHICLE_COMPARE_CONSTANTS import VEHICLE_COMPARE_CONSTANTS as VEHICLE_COMPARE_CONSTANTS
from shared_utils.vehicle_utils import ModuleDependencies as ModulesInstaller
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any

class _MODULES_TYPES(object):
    BASIC = 'basic'
    CURRENT = 'current'
    CUSTOM = 'custom'

class _PreviewItemsData(ResearchItemsData):
    __previewVehicle: Any
    def __init__(self, dumper, vehicle):
        ...
    def setVehicle(self, vehicle):
        ...
    def clear(self, full=False):
        ...
    def getRootItem(self):
        ...
    def _getRootUnlocksDescrs(self, rootItem):
        ...
    def _getNodeData(self, nodeCD, previewItem, guiItem, unlockStats, unlockProps, path, level=-1, topLevel=False):
        ...
    def _loadTopLevel(self, rootItem, unlockStats):
        ...

class VehicleModulesView(VehicleModulesViewMeta, VehicleCompareConfiguratorBaseView):
    __nodes: Any
    __vehicle: Any
    __nodeDataGenerator: Any
    __currentModulesType: Any
    __isInited: Any
    __configuredVehModulesIDs: Any
    __initialModulesIDs: Any
    __modulesInstaller: Any
    def __init__(self):
        ...
    def _init(self):
        ...
    def _dispose(self):
        ...
    def onShow(self):
        ...
    def onCloseView(self):
        ...
    def resetConfig(self):
        ...
    def applyConfig(self):
        ...
    def onModuleHover(self, moduleId):
        ...
    def onModuleClick(self, moduleId):
        ...
    def __initialize(self, strCD, modulesType):
        ...
    def __updateChangedSlots(self):
        ...
    def __updateModulesData(self):
        ...
    def __updateModulesType(self, modulesType):
        ...
    def __detectModulesType(self, targetVeh):
        ...
    def __createVehicleData(self, strCD):
        ...
    def __resetData(self, strCD, modulesType):
        ...
    # decorador original: @dependency.replace_none_kwargs(...)
    def _getModule(self, moduleId, itemsCache=None):
        ...
    # decorador original: @adisp_process
    def _installModule(self, vehicle, module):
        ...
