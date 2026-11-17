# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/items_actions/factory.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from adisp import adisp_process as adisp_process, adisp_async as adisp_async
from gui.shared.gui_items.items_actions import actions as actions
from gui.shared.gui_items.items_actions.actions import PurchaseVehSkillTreeSteps as PurchaseVehSkillTreeSteps
_logger: Any
SELL_ITEM = 'sellItemAction'
SELL_MULTIPLE = 'sellMultipleItems'
BUY_VEHICLE = 'vehBuyAction'
BUY_MODULE = 'moduleBuyAction'
UNLOCK_ITEM = 'unlockAction'
INSTALL_ITEM = 'installItemAction'
BUY_AND_INSTALL_ITEM = 'buyAndInstallItemAction'
BUY_AND_INSTALL_AND_SELL_ITEM = 'BuyAndInstallWithOptionalSellItemAction'
VEHICLE_AUTO_FILL_LAYOUT = 'vehicleAutoFillLayoutAction'
BUY_BERTHS = 'buyBerths'
BUY_VEHICLE_SLOT = 'buyVehClot'
ACTIVATE_BOOSTER = 'activateBooster'
BUY_BOOSTER = 'buyBooster'
BUY_AND_ACTIVATE_BOOSTER = 'buyAndActivateBooster'
CONVERT_BLUEPRINT_FRAGMENT = 'convertFragment'
USE_CREW_BOOK = 'useCrewBook'
USE_FREE_XP_TO_TANKMAN = 'useFreeXpToTankman'
RETRAIN_TANKMAN = 'retrainTankman'
CHANGE_ROLE_TANKMAN = 'changeRoleTankman'
UNLOAD_TANKMAN = 'unloadTankman'
EQUIP_TANKMAN = 'equipTankman'
QUICK_SERVICE_EQUIP_TANKMAN = 'quickServiceEquipTankman'
BUY_AND_EQUIP_TANKMAN = 'buyAndEquipTankman'
CHANGE_TANKMAN_PASSPORT = 'changeTankmanPassport'
DISMISS_TANKMAN = 'dismissTankman'
RESTORE_TANKMAN = 'restoreTankman'
CONVERT_JUNK_TANKMEN = 'convertJunkTankmen'
TRANSFER_TANKMAN_XP = 'transferTankmanXp'
CHANGE_NATION = 'changeNation'
INSTALL_BATTLE_ABILITIES = 'installBattleAbilities'
FRONTLINE_INSTALL_RESERVES = 'frontlineInstallReserves'
BUY_BATTLE_ABILITIES = 'buyBattleAbilities'
BUY_AND_INSTALL_OPT_DEVICES = 'buyAndInstallOptDevices'
BUY_AND_INSTALL_CONSUMABLES = 'buyAndInstallConsumables'
BUY_AND_INSTALL_SHELLS = 'buyAndInstallShells'
BUY_AND_INSTALL_BATTLE_BOOSTERS = 'buyAndInstallBattleBoosters'
UPGRADE_OPT_DEVICE = 'upgradeOptDevice'
DECONSTRUCT_OPT_DEVICE = 'deconstructOptDevice'
DECONSTRUCT_MULT_OPT_DEVICE = 'deconstructMultOptDevice'
REMOVE_OPT_DEVICE = 'removeOptDevice'
CHANGE_SETUP_EQUIPMENTS_INDEX = 'changeSetupEquipmentsIndex'
SET_EQUIPMENT_SLOT_TYPE = 'setEquipmentSlotType'
DISCARD_POST_PROGRESSION_PAIRS = 'discardPostProgressionPairs'
PURCHASE_POST_PROGRESSION_PAIR = 'purchasePostProgressionPair'
PURCHASE_POST_PROGRESSION_STEPS = 'purchasePostProgressionSteps'
SWITCH_PREBATTLE_AMMO_PANEL_AVAILABILITY = 'switchPrebattleAmmoPanelAvailability'
ADD_SKILLS_TANKMAN = 'addSkillsTankman'
PURCHASE_VEH_SKILL_TREE_STEPS = 'purchaseVehSkillTreeSteps'
_ACTION_MAP: dict

# decorador original: @adisp_process
def doAction(actionType, *args, **kwargs):
    ...
# decorador original: @adisp_async
# decorador original: @adisp_process
def asyncDoAction(action, callback):
    ...
def getAction(actionType, *args, **kwargs):
    ...
