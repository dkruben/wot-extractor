# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/personal_missions_30/main_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel as VehicleInfoModel
from gui.impl.gen.view_models.views.lobby.personal_missions_30.missions_state_model import MissionsStateModel as MissionsStateModel
from gui.impl.gen.view_models.views.lobby.personal_missions_30.new_operation_banner import NewOperationBanner as NewOperationBanner
from gui.impl.gen.view_models.views.lobby.personal_missions_30.operation_model import OperationModel as OperationModel
from gui.impl.gen.view_models.views.lobby.personal_missions_30.operation_status_model import OperationStatusModel as OperationStatusModel
from gui.impl.gen.view_models.views.lobby.personal_missions_30.select_operation_model import SelectOperationModel as SelectOperationModel

class MainScreenState(Enum):
    ASSEMBLING = 'assembling'
    MISSIONS = 'missions'
    PROGRESSION = 'progression'

class AnimationState(Enum):
    IDLE = 'idle'
    ANIMATION_STARTED = 'animationStarted'
    ASSEMBLING = 'assembling'
    CONTINUE_DETAIL_INFO = 'continueDetailInfo'
    CONTINUE_CLAIM_DETAIL = 'continueClaimDetail'
    CONTINUE_BACK = 'continueBack'

class MainViewModel(ViewModel):
    __slots__: tuple
    OPERATION_ID = 'operationId'
    DETAIL_ID = 'detailId'
    ANIMATION_STATE = 'animationState'
    onBack: Any
    onSwitchOperation: Any
    showOperationVehicleVideo: Any
    onOperationStatusButtonClick: Any
    onDetailInfo: Any
    onClaimDetail: Any
    onMission: Any
    onAdditionalMission: Any
    onVehiclePreview: Any
    showVehicleInHangar: Any
    showDetailVideo: Any
    onMoveSpace: Any
    onMouseOver3dScene: Any
    showStylePreview: Any
    setFreeCamera: Any
    updateAnimationState: Any
    def __init__(self, properties=11, commands=16):
        ...
    @property
    def vehicle(self):
        ...
    @staticmethod
    def getVehicleType():
        ...
    @property
    def status(self):
        ...
    @staticmethod
    def getStatusType():
        ...
    @property
    def missionsModel(self):
        ...
    @staticmethod
    def getMissionsModelType():
        ...
    @property
    def banner(self):
        ...
    @staticmethod
    def getBannerType():
        ...
    def getActiveOperationId(self):
        ...
    def setActiveOperationId(self, value):
        ...
    def getAnimationState(self):
        ...
    def setAnimationState(self, value):
        ...
    def getCampaignName(self):
        ...
    def setCampaignName(self, value):
        ...
    def getMenuItems(self):
        ...
    def setMenuItems(self, value):
        ...
    @staticmethod
    def getMenuItemsType():
        ...
    def getOperations(self):
        ...
    def setOperations(self, value):
        ...
    @staticmethod
    def getOperationsType():
        ...
    def getMainScreenState(self):
        ...
    def setMainScreenState(self, value):
        ...
    def getCameraFlightInProgress(self):
        ...
    def setCameraFlightInProgress(self, value):
        ...
    def _initialize(self):
        ...
