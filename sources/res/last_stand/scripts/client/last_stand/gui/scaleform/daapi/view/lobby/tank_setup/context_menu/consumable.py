# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/lobby/tank_setup/context_menu/consumable.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/lobby/tank_setup/context_menu/consumable.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.lobby.tank_setup.context_menu.consumable import consumableDecorator, HangarConsumableSlotContextMenu
from last_stand.gui.shared.event_dispatcher import showModuleInfo
from ids_generators import SequenceIDGenerator
from LSAccountEquipmentController import getLSConsumables
from last_stand.gui.impl.lobby.tank_setup import LSTankSetupConstants
from gui.shared.gui_items.items_actions import factory as ActionsFactory
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel
from last_stand.gui.impl.lobby.tank_setup.interactor import ActionTypes
from adisp import adisp_process, adisp_async

@consumableDecorator
class LSHangarConsumableSlotContextMenu(HangarConsumableSlotContextMenu):
    _sqGen = SequenceIDGenerator(HangarConsumableSlotContextMenu._sqGen.currSequenceID)

    def _putOnAction(self, onId):
        copyVehicle = self._getCopyVehicle()
        extConsumables = getLSConsumables(copyVehicle)
        extConsumables.layout = extConsumables.installed.copy()
        layout = extConsumables.layout
        self._makePutOnAction(LSTankSetupConstants.LS_CONSUMABLES, onId, copyVehicle, layout)

    @adisp_async
    @adisp_process
    def _doPutOnAction(self, vehicle, callback):
        actionName = ActionTypes.BUY_AND_INSTALL_LS_CONSUMABLES_ACTION
        action = ActionsFactory.getAction(actionName, vehicle, confirmOnlyExchange=True)
        result = yield ActionsFactory.asyncDoAction(action)
        callback(result)

    def _getVehicleItems(self):
        return self._getVehicle().consumables

    @adisp_process
    def _unloadAction(self):
        copyVehicle = self._getCopyVehicle()
        extConsumables = getLSConsumables(copyVehicle)
        extConsumables.layout = extConsumables.installed.copy()
        extConsumables.layout[self._installedSlotId] = None
        result = yield self._doPutOnAction(copyVehicle)
        if result:
            self._sendLastSlotAction(LSTankSetupConstants.LS_CONSUMABLES, BaseSetupModel.REVERT_SLOT_ACTION, {'slotID': (self._installedSlotId)})
        return

    def _showInfo(self):
        showModuleInfo(self._intCD, self._getVehicle().descriptor)
