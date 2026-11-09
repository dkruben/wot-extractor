# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_hub/views/vehicle_hub_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel as VehicleInfoModel
from gui.impl.gen.view_models.views.lobby.common.router_model import RouterModel as RouterModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.armor_model import ArmorModel as ArmorModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.comparison_model import ComparisonModel as ComparisonModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.menu_item_model import MenuItemModel as MenuItemModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.modules_model import ModulesModel as ModulesModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.overview_model import OverviewModel as OverviewModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.research_purchase_model import ResearchPurchaseModel as ResearchPurchaseModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.stats_model import StatsModel as StatsModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.veh_skill_tree_model import VehSkillTreeModel as VehSkillTreeModel

class VehicleHubViewModel(ViewModel):
    __slots__: tuple
    OVERVIEW = 'overview'
    MODULES = 'modules'
    VEH_SKILL_TREE = 'vehSkillTree'
    STATS = 'stats'
    ARMOR = 'armor'
    onMoveSpace: Any
    onMouseOver3dScene: Any
    onResize: Any
    def __init__(self, properties=10, commands=3):
        ...
    @property
    def router(self):
        ...
    @staticmethod
    def getRouterType():
        ...
    @property
    def vehicleInfoModel(self):
        ...
    @staticmethod
    def getVehicleInfoModelType():
        ...
    @property
    def comparisonModel(self):
        ...
    @staticmethod
    def getComparisonModelType():
        ...
    @property
    def overviewModel(self):
        ...
    @staticmethod
    def getOverviewModelType():
        ...
    @property
    def modulesModel(self):
        ...
    @staticmethod
    def getModulesModelType():
        ...
    @property
    def vehSkillTreeModel(self):
        ...
    @staticmethod
    def getVehSkillTreeModelType():
        ...
    @property
    def statsModel(self):
        ...
    @staticmethod
    def getStatsModelType():
        ...
    @property
    def armorModel(self):
        ...
    @staticmethod
    def getArmorModelType():
        ...
    @property
    def researchPurchaseModel(self):
        ...
    @staticmethod
    def getResearchPurchaseModelType():
        ...
    def getMenuItems(self):
        ...
    def setMenuItems(self, value):
        ...
    @staticmethod
    def getMenuItemsType():
        ...
    def _initialize(self):
        ...
