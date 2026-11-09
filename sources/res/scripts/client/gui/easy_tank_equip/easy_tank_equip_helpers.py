# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/easy_tank_equip/easy_tank_equip_helpers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/easy_tank_equip/easy_tank_equip_helpers.py
import typing
from account_helpers import AccountSettings
from account_helpers.AccountSettings import EasyTankEquip
from helpers import dependency
from skeletons.gui.game_control import IEasyTankEquipController
if typing.TYPE_CHECKING:
    from gui.shared.gui_items.Vehicle import Vehicle

@dependency.replace_none_kwargs(easyTankEquipController=IEasyTankEquipController)
def isAvailableForVehicle(vehicle, easyTankEquipController=None):
    return vehicle is not None and vehicle.level >= easyTankEquipController.config.minVehicleLevel


def getEasyTankEquipSetting(settingName):
    return AccountSettings.getSettings(EasyTankEquip.EASY_TANK_EQUIP_SETTINGS).get(settingName)


def setEasyTankEquipSetting(settingName, settingValue):
    settings = AccountSettings.getSettings(EasyTankEquip.EASY_TANK_EQUIP_SETTINGS)
    settings.update({settingName: settingValue})
    AccountSettings.setSettings(EasyTankEquip.EASY_TANK_EQUIP_SETTINGS, settings)
