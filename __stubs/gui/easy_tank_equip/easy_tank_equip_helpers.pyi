# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/easy_tank_equip/easy_tank_equip_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import EasyTankEquip as EasyTankEquip
from helpers import dependency as dependency
from skeletons.gui.game_control import IEasyTankEquipController as IEasyTankEquipController
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle

# decorador original: @dependency.replace_none_kwargs(...)
def isAvailableForVehicle(vehicle, easyTankEquipController=None):
    ...
def getEasyTankEquipSetting(settingName):
    ...
def setEasyTankEquipSetting(settingName, settingValue):
    ...
