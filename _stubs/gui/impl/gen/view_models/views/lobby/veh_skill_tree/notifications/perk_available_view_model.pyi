# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/veh_skill_tree/notifications/perk_available_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.gen.view_models.common.notification_base_model import NotificationBaseModel as NotificationBaseModel
from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel as VehicleModel

class PerkAvailableViewModel(NotificationBaseModel):
    __slots__: tuple
    onClose: Any
    onGoToProgression: Any
    def __init__(self, properties=3, commands=2):
        ...
    @property
    def vehicle(self):
        ...
    @staticmethod
    def getVehicleType():
        ...
    def getIsDisabled(self):
        ...
    def setIsDisabled(self, value):
        ...
    def _initialize(self):
        ...
