# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/dialogs/confirm_actions_with_equipment_dialog_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from frameworks.wulf import Array as Array
from gui.impl.gen.view_models.views.dialogs.dialog_template_view_model import DialogTemplateViewModel as DialogTemplateViewModel
from gui.impl.gen.view_models.views.lobby.tank_setup.dialogs.details_device_model import DetailsDeviceModel as DetailsDeviceModel
from gui.impl.gen.view_models.views.lobby.tank_setup.dialogs.details_price_block_model import DetailsPriceBlockModel as DetailsPriceBlockModel
from gui.impl.gen.view_models.views.lobby.tank_setup.dialogs.sub_views.current_balance_model import CurrentBalanceModel as CurrentBalanceModel

class DialogType(Enum):
    DECONSTRUCTFROMSTORAGE = 'deconstructFromStorage'
    DECONSTRUCTFROMSLOTS = 'deconstructFromSlots'

class ConfirmActionsWithEquipmentDialogModel(DialogTemplateViewModel):
    __slots__: tuple
    onDeconstruct: Any
    onClose: Any
    def __init__(self, properties=11, commands=4):
        ...
    @property
    def detailsDevice(self):
        ...
    @staticmethod
    def getDetailsDeviceType():
        ...
    @property
    def detailsPriceBlock(self):
        ...
    @staticmethod
    def getDetailsPriceBlockType():
        ...
    def getAlertText(self):
        ...
    def setAlertText(self, value):
        ...
    def getDialogType(self):
        ...
    def setDialogType(self, value):
        ...
    def getBalance(self):
        ...
    def setBalance(self, value):
        ...
    @staticmethod
    def getBalanceType():
        ...
    def _initialize(self):
        ...
