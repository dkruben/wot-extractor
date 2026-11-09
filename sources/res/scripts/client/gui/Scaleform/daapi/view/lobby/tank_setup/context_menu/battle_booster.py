# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/tank_setup/context_menu/battle_booster.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/tank_setup/context_menu/battle_booster.py
from __future__ import absolute_import
import SoundGroups
from adisp import adisp_process, adisp_async
from gui import shop
from gui.Scaleform.daapi.view.lobby.shared.cm_handlers import CMLabel, option
from gui.Scaleform.daapi.view.lobby.tank_setup.context_menu.base import BaseItemContextMenu, BaseSlotContextMenu, TankSetupCMLabel
from gui.Scaleform.daapi.view.lobby.tank_setup.context_menu.base_equipment import BaseHangarEquipmentSlotContextMenu
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants
from gui.impl.lobby.tank_setup.tank_setup_sounds import TankSetupSoundEvents
from gui.shared.gui_items.items_actions import factory as ActionsFactory
from ids_generators import SequenceIDGenerator

class BattleBoosterItemContextMenu(BaseItemContextMenu):
    __sqGen = SequenceIDGenerator()

    @option(__sqGen.nextSequenceID, TankSetupCMLabel.SELECT)
    def select(self):
        self._sendSlotAction(BaseSetupModel.SELECT_SLOT_ACTION)

    @option(__sqGen.nextSequenceID, CMLabel.BUY_MORE)
    def buyMore(self):
        shop.showBattleBooster(itemId=self._intCD, source=shop.Source.EXTERNAL, origin=shop.Origin.BATTLE_BOOSTERS)

    def _isVisible(self, label):
        if label == CMLabel.BUY_MORE:
            return not self._itemsCache.items.getItemByCD(self._intCD).isHidden
        return super(BattleBoosterItemContextMenu, self)._isVisible(label)

    def _getVehicleItems(self):
        return self._getVehicle().battleBoosters


class BattleBoosterSlotContextMenu(BaseSlotContextMenu):
    __sqGen = SequenceIDGenerator()

    @option(__sqGen.nextSequenceID, CMLabel.BUY_MORE)
    def buyMore(self):
        shop.showBattleBooster(itemId=self._intCD, source=shop.Source.EXTERNAL, origin=shop.Origin.BATTLE_BOOSTERS)

    @option(__sqGen.nextSequenceID, TankSetupCMLabel.UNLOAD)
    def unload(self):
        SoundGroups.g_instance.playSound2D(TankSetupSoundEvents.INSTRUCTIONS_DEMOUNT)
        self._sendSlotAction(BaseSetupModel.SELECT_SLOT_ACTION, intCD=None, currentSlotId=self._installedSlotId)
        return

    @option(__sqGen.nextSequenceID, TankSetupCMLabel.TAKE_OFF)
    def takeOff(self):
        SoundGroups.g_instance.playSound2D(TankSetupSoundEvents.INSTRUCTIONS_DEMOUNT)
        self._sendSlotAction(BaseSetupModel.REVERT_SLOT_ACTION)

    def _isVisible(self, label):
        if label == CMLabel.BUY_MORE:
            return not self._itemsCache.items.getItemByCD(self._intCD).isHidden
        return super(BattleBoosterSlotContextMenu, self)._isVisible(label)

    def _getVehicleItems(self):
        return self._getVehicle().battleBoosters


class HangarBattleBoosterSlotContextMenu(BaseHangarEquipmentSlotContextMenu):
    _sqGen = SequenceIDGenerator(BaseHangarEquipmentSlotContextMenu._sqGen.currSequenceID)

    @option(_sqGen.nextSequenceID, CMLabel.BUY_MORE)
    def buyMore(self):
        shop.showBattleBooster(itemId=self._intCD, source=shop.Source.EXTERNAL, origin=shop.Origin.BATTLE_BOOSTERS)

    @option(_sqGen.nextSequenceID, TankSetupCMLabel.UNLOAD)
    def unload(self):
        self.__unloadAction()

    @option(_sqGen.nextSequenceID, TankSetupCMLabel.TAKE_OFF)
    def takeOffFromSlot(self):
        self.__unloadAction()

    def _isVisible(self, label):
        if label == CMLabel.INFORMATION:
            return False
        if label == CMLabel.BUY_MORE:
            return not self._itemsCache.items.getItemByCD(self._intCD).isHidden
        return super(HangarBattleBoosterSlotContextMenu, self)._isVisible(label)

    @adisp_async
    @adisp_process
    def _doPutOnAction(self, vehicle, callback):
        action = ActionsFactory.getAction(ActionsFactory.BUY_AND_INSTALL_BATTLE_BOOSTERS, vehicle, confirmOnlyExchange=True)
        result = yield ActionsFactory.asyncDoAction(action)
        callback(result)

    def _getVehicleItems(self):
        return self._getVehicle().battleBoosters

    @adisp_process
    def __unloadAction(self):
        copyVehicle = self._getCopyVehicle()
        copyVehicle.battleBoosters.layout[self._installedSlotId] = None
        result = yield self._doPutOnAction(copyVehicle)
        if result:
            SoundGroups.g_instance.playSound2D(TankSetupSoundEvents.INSTRUCTIONS_DEMOUNT)
            self._sendLastSlotAction(TankSetupConstants.BATTLE_BOOSTERS, BaseSetupModel.REVERT_SLOT_ACTION, {'slotID': (self._installedSlotId)})
        return
