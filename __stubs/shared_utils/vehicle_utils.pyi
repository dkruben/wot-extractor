# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client_common/shared_utils/vehicle_utils.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import NetworkFilters as NetworkFilters
import BigWorld as BigWorld
from adisp import adisp_process as adisp_process
from debug_utils import LOG_DEBUG as LOG_DEBUG
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.processors.module import getPreviewInstallerProcessor as getPreviewInstallerProcessor
from gui.shared.items_parameters.params_cache import g_paramsCache as g_paramsCache
from helpers import dependency as dependency
from items import getTypeOfCompactDescr as getTypeOfCompactDescr, vehicles as vehicles
from skeletons.gui.shared import IItemsCache as IItemsCache
from vehicle_systems.tankStructure import TankPartIndexes as TankPartIndexes
_MODULES_INSTALL_ORDER: tuple

class ModuleDependencies(object):
    __slots__: tuple
    __stockModules: Any
    __hasConflicted: Any
    __conflictedModulesCD: Any
    def __init__(self, stockModules):
        ...
    def dispose(self):
        ...
    def hasConflicted(self):
        ...
    def getConflictedModules(self):
        ...
    def updateConflicted(self, moduleId, vehicle):
        ...
    def clearConflictedModules(self):
        ...
    def __addConflicted(self, moduleTypeID, moduleCDs):
        ...
    def __getSuitableModulesForGun(self, gunIntCD, vehicle):
        ...
    def __initConflictedList(self):
        ...
    # decorador original: @adisp_process
    def _installModule(self, vehicle, module):
        ...
    # decorador original: @dependency.replace_none_kwargs(...)
    def _getModule(self, moduleId, itemsCache=None):
        ...
    # decorador original: @dependency.replace_none_kwargs(...)
    def getSuitableChassis(self, vehicle, itemsCache=None):
        ...

def createWheelFilters(typeDescriptor):
    ...
def getMatinfo(vehicleEntity, partIndex, matKind, isWheeledVehicle):
    ...
