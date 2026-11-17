# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/lobby/tank_setup/context_menu/consumable.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.lobby.tank_setup.context_menu.consumable import consumableDecorator as consumableDecorator, HangarConsumableSlotContextMenu as HangarConsumableSlotContextMenu
from last_stand.gui.shared.event_dispatcher import showModuleInfo as showModuleInfo
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from LSAccountEquipmentController import getLSConsumables as getLSConsumables
from last_stand.gui.impl.lobby.tank_setup import LSTankSetupConstants as LSTankSetupConstants
from gui.shared.gui_items.items_actions import factory as ActionsFactory
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel as BaseSetupModel
from last_stand.gui.impl.lobby.tank_setup.interactor import ActionTypes as ActionTypes
from adisp import adisp_process as adisp_process, adisp_async as adisp_async

# decorador original: @consumableDecorator
class LSHangarConsumableSlotContextMenu(HangarConsumableSlotContextMenu):
    _sqGen: Any
    def _putOnAction(self, onId):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def _doPutOnAction(self, vehicle, callback):
        ...
    def _getVehicleItems(self):
        ...
    # decorador original: @adisp_process
    def _unloadAction(self):
        ...
    def _showInfo(self):
        ...
