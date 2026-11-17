# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/battle_pass_widget_final_rewards_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel as VehicleInfoModel
from gui.impl.gen.view_models.views.lobby.battle_pass.attachments_set_info_model import AttachmentsSetInfoModel as AttachmentsSetInfoModel
from gui.impl.gen.view_models.views.lobby.battle_pass.character_widget_view_model import CharacterWidgetViewModel as CharacterWidgetViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.style_info_model import StyleInfoModel as StyleInfoModel

class BattlePassWidgetFinalRewardsViewModel(ViewModel):
    __slots__: tuple
    showTankmen: Any
    onRewardPreviewClick: Any
    def __init__(self, properties=5, commands=2):
        ...
    @property
    def vehicleInfo(self):
        ...
    @staticmethod
    def getVehicleInfoType():
        ...
    @property
    def tankmanInfo(self):
        ...
    @staticmethod
    def getTankmanInfoType():
        ...
    @property
    def styleInfo(self):
        ...
    @staticmethod
    def getStyleInfoType():
        ...
    @property
    def attachmentsSetInfo(self):
        ...
    @staticmethod
    def getAttachmentsSetInfoType():
        ...
    def getBattleQuest(self):
        ...
    def setBattleQuest(self, value):
        ...
    def _initialize(self):
        ...
