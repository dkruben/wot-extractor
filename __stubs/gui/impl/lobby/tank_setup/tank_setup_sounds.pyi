# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/tank_setup_sounds.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import SoundGroups as SoundGroups
import WWISE as WWISE
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel as BaseSetupModel
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants as TankSetupConstants
from helpers import dependency as dependency
from shared_utils import CONST_CONTAINER as CONST_CONTAINER, first as first
from skeletons.gui.shared import IItemsCache as IItemsCache

class TankSetupSoundEvents(CONST_CONTAINER):
    STATE_PLACE = 'STATE_hangar_place'
    STATE_PLACE_ENTER = 'STATE_hangar_place_consumables'
    STATE_PLACE_GARAGE = 'STATE_hangar_place_garage'
    VIEW_ENTER = 'cons_enter'
    VIEW_EXIT = 'cons_exit'
    SELECT_VIEW = 'cons_select_view'
    ACCEPT = 'cons_accept'
    EQUIPMENT_SLOT_PREFIX = 'cons_equipment_slot_'
    EQUIPMENT_MOUNT = 'cons_equipment_mount'
    EQUIPMENT_DEMOUNT = 'cons_equipment_demount'
    EQUIPMENT_DEMOUNT_KIT = 'cons_equipment_demount_kit'
    EQUIPMENT_DESTROY = 'cons_equipment_destroy'
    EQUIPMENT_SWAP = 'cons_equipment_swipe'
    EQUIPMENT_BONUS = 'cons_equipment_bonus'
    CONSUMABLES_MOUNT = 'cons_consumables_mount'
    CONSUMABLES_DEMOUNT = 'cons_consumables_demount'
    INSTRUCTIONS_MOUNT = 'cons_instructions_mount'
    INSTRUCTIONS_DEMOUNT = 'cons_instructions_demount'
    INSTRUCTIONS_EQUIP_NOT_SUITABLE = 'cons_instructions_equip_not_suitable'
    RTPC_SHELLS_PROGRESS_BAR = 'RTPC_ext_ammo_progress_bar'
    AMMO_SINGLE_PLUS = 'cons_ammo_single_plus'
    AMMO_SINGLE_MINUS = 'cons_ammo_single_minus'

class ActionSoundHelper(object):
    _itemsCache: Any
    @classmethod
    def playActionSound(cls, actionType, vehicle, intCD=-1, leftIntCD=-1, rightIntCD=-1):
        ...
    @classmethod
    def playSelectSound(cls, vehicle, intCD):
        ...
    @classmethod
    def playRevertSound(cls, vehicle):
        ...
    @classmethod
    def playDemountSound(cls, vehicle, intCD):
        ...
    @classmethod
    def playDestroySound(cls, vehicle, intCD):
        ...
    @classmethod
    def playSwapSound(cls, vehicle, leftIntCD, rightIntCD):
        ...
    @classmethod
    def playDragAndDropSound(cls, vehicle, leftIntCD, rightIntCD):
        ...

class ConsumableActionSoundHelper(ActionSoundHelper):
    @classmethod
    def playSelectSound(cls, vehicle, intCD):
        ...
    @classmethod
    def playRevertSound(cls, vehicle):
        ...

class OptDeviceActionSound(ActionSoundHelper):
    @classmethod
    def playSelectSound(cls, vehicle, intCD):
        ...
    @classmethod
    def playSwapSound(cls, vehicle, leftIntCD, rightIntCD):
        ...
    @classmethod
    def playDragAndDropSound(cls, vehicle, leftIntCD, rightIntCD):
        ...
    @classmethod
    def _isCategoryMatch(cls, vehicle, intCD):
        ...

class BattleBoostersActionSoundHelper(ActionSoundHelper):
    _CREW_BOOSTER_SOUND: dict
    @classmethod
    def playSelectSound(cls, vehicle, intCD):
        ...
    @classmethod
    def playRevertSound(cls, vehicle):
        ...
    @classmethod
    def _playCrewBoosterSelectSound(cls, vehicle, item):
        ...
    @classmethod
    def _playOptDeviceBoosterSelectSound(cls, vehicle, item):
        ...

def playEnterTankSetupView():
    ...
def playExitTankSetupView():
    ...
def playOptDeviceSlotEnter(vehicle, slotID):
    ...
def playSound(eventName):
    ...
def playSectionSelectSound():
    ...
def playSlotActionSound(setupName, *args, **kwargs):
    ...
