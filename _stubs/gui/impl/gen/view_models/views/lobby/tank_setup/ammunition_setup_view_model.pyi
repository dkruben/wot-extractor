# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/ammunition_setup_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel as VehicleInfoModel
from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_panel_model import AmmunitionPanelModel as AmmunitionPanelModel
from gui.impl.gen.view_models.views.lobby.tank_setup.common.role_skill_slot_model import RoleSkillSlotModel as RoleSkillSlotModel
from gui.impl.gen.view_models.views.lobby.tank_setup.main_tank_setup_model import MainTankSetupModel as MainTankSetupModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.optional_devices_assistant_model import OptionalDevicesAssistantModel as OptionalDevicesAssistantModel
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_action_model import TankSetupActionModel as TankSetupActionModel

class AmmunitionSetupViewModel(ViewModel):
    __slots__: tuple
    onClose: Any
    onResized: Any
    onViewRendered: Any
    onAnimationEnd: Any
    def __init__(self, properties=8, commands=4):
        ...
    @property
    def tankSetup(self):
        ...
    @staticmethod
    def getTankSetupType():
        ...
    @property
    def ammunitionPanel(self):
        ...
    @staticmethod
    def getAmmunitionPanelType():
        ...
    @property
    def lastSlotAction(self):
        ...
    @staticmethod
    def getLastSlotActionType():
        ...
    @property
    def vehicleInfo(self):
        ...
    @staticmethod
    def getVehicleInfoType():
        ...
    @property
    def roleSkillSlot(self):
        ...
    @staticmethod
    def getRoleSkillSlotType():
        ...
    @property
    def optionalDevicesAssistant(self):
        ...
    @staticmethod
    def getOptionalDevicesAssistantType():
        ...
    def getShow(self):
        ...
    def setShow(self, value):
        ...
    def getIsReady(self):
        ...
    def setIsReady(self, value):
        ...
    def _initialize(self):
        ...
