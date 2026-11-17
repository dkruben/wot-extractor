# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/personal_missions_30/campaign_selector_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.personal_missions_30.campaign_model import CampaignModel as CampaignModel

class CampaignSelectorViewState(Enum):
    FIRST_TWO = 'firstTwo'
    THIRD = 'third'
    COMPLETED_WITH_HONOR = 'completedWithHonor'
    LOCKED = 'locked'

class CampaignSelectorModel(ViewModel):
    __slots__: tuple
    OPERATION_ID = 'operationId'
    CAMPAIGNS_STATE = 'campaignsState'
    FIRST_ACTIVATE = 'firstActivate'
    onOperation: Any
    switchCampaign: Any
    onClose: Any
    def __init__(self, properties=4, commands=3):
        ...
    def getCampaigns(self):
        ...
    def setCampaigns(self, value):
        ...
    @staticmethod
    def getCampaignsType():
        ...
    def getBlockedByVehicle(self):
        ...
    def setBlockedByVehicle(self, value):
        ...
    def getFirstTimeEntrance(self):
        ...
    def setFirstTimeEntrance(self, value):
        ...
    def getCampaignSelectorViewState(self):
        ...
    def setCampaignSelectorViewState(self, value):
        ...
    def _initialize(self):
        ...
