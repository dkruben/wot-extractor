# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_compare/cmp_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from future.utils import itervalues as itervalues
from constants import NEW_PERK_SYSTEM as NPS
from frameworks.wulf import WindowLayer as WindowLayer
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.vehicle_compare.cmp_top_modules import TopModulesChecker as TopModulesChecker
from gui.Scaleform.framework.managers.containers import POP_UP_CRITERIA as POP_UP_CRITERIA
from gui.shared.gui_items import GUI_ITEM_TYPE_NAMES as GUI_ITEM_TYPE_NAMES, GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.Tankman import Tankman as Tankman
from gui.shared.gui_items.tankman_skill import BROTHERHOOD_SKILL_NAME as BROTHERHOOD_SKILL_NAME
from helpers import dependency as dependency
from items import tankmen as tankmen
from items.components.c11n_components import SeasonType as SeasonType
from items.tankmen import SKILLS_BY_ROLES as SKILLS_BY_ROLES, ROLES_BY_SKILLS as ROLES_BY_SKILLS
from shared_utils import first as first
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.shared.gui_items import IGuiItemsFactory as IGuiItemsFactory
from gui.shared.gui_items.customization.c11n_items import Camouflage as Camouflage
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from gui.Scaleform.daapi.view.lobby.vehicle_compare.cmp_configurator_view import VehicleCompareConfiguratorMain as VehicleCompareConfiguratorMain
MODULES_INSTALLING_ORDER: tuple
NOT_AFFECTED_DEVICES: dict
NOT_AFFECTED_EQUIPMENTS: set
OPTIONAL_DEVICE_TYPE_NAME: Any
EQUIPMENT_TYPE_NAME: Any
BATTLE_BOOSTER_TYPE_NAME: Any

def createTankman(nationID, vehicleTypeID, role, roleLevel, skills, vehicle, vehicleSlotIDx, rolesBonusSkills=None, bonusSkillNamesMaxLvl=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getVehCrewInfo(vehIntCD, itemsCache=None):
    ...
def isEquipmentSame(equipment1, equipment2):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getCmpConfiguratorMainView(appLoader=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getSuitableCamouflage(vehicle, c11nService=None):
    ...
def isCamouflageSet(vehicle):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def applyCamouflage(vehicle, select, factory=None, itemsCache=None):
    ...
def removeVehicleCamouflages(vehicle):
    ...
def getVehicleModules(vehicle):
    ...
def getVehicleTopModules(vehicle):
    ...
def isSkillMajor(skillName, role):
    ...
def splitSkills(selectedSkills):
    ...
