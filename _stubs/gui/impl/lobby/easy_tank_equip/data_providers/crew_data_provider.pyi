# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/easy_tank_equip/data_providers/crew_data_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import TYPE_CHECKING as TYPE_CHECKING
import nations as nations
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.common.preset_model import PresetDisableReason as PresetDisableReason
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.crew_preset_model import CrewPresetType as CrewPresetType
from gui.impl.lobby.easy_tank_equip.data_providers.base_data_provider import BaseDataProvider as BaseDataProvider, PresetInfo as PresetInfo
from gui.shared.gui_items import checkForTags as checkForTags
from gui.shared.gui_items.Vehicle import VEHICLE_TAGS as VEHICLE_TAGS, sortCrew as sortCrew
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA, RequestCriteria as RequestCriteria
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.shared.gui_items import IGuiItemsFactory as IGuiItemsFactory
from typing import List as List, Optional as Optional, Tuple as Tuple
from gui.shared.gui_items import Tankman as Tankman, Vehicle as Vehicle

class CrewPresetInfo(PresetInfo):
    recruitsCount: Any
    presetType: Any
    tankmen: Any
    tankmenNativeVeh: Any
    def __init__(self, installed, recruitsCount, presetType, tankmen, tankmenNativeVeh, disableReason=...):
        ...

class CrewDataProvider(BaseDataProvider):
    EXPERIENCED_PRESET_NUMBER = 0
    NEW_CREW_PRESET_NUMBER = 1
    PRESET_INDEXES: list
    NEW_TANKMAN_INV_ID = -1
    __itemsCache: Any
    __itemsFactory: Any
    __currentVehicleCrew: Any
    __vehDescrType: Any
    __tankmenInTank: Any
    __countTankmenInTank: Any
    __tankmenRoles: Any
    __countRolesInTank: Any
    __vehicleCrewIsLocked: Any
    __inventoryTankmen: Any
    __freeBerthsCount: Any
    __tankmenPresets: Any
    __countEmptySlotInPreset: Any
    __tankmenNativeVeh: Any
    __tankmenPresetsForTTC: Any
    __tankmenPresetsForApplying: Any
    isProposalSelected: Any
    def __init__(self, vehicle, balance):
        ...
    def initialize(self):
        ...
    def finalize(self):
        ...
    def getPresets(self):
        ...
    def updatePresets(self, fullUpdate=False):
        ...
    def swapSlots(self, firstSlot, secondSlot):
        ...
    def setValuesFromCurrentPreset(self):
        ...
    def revertChangesFromSelectedPreset(self):
        ...
    def getCurrentPresetItemsIds(self):
        ...
    def _getPresetDataForApplying(self):
        ...
    def __isEnoughBunksForPreset(self, presetIndex):
        ...
    def __getPresetInfo(self, installed, presetType, presetIndex):
        ...
    def __setTankmenForApplying(self):
        ...
    def __hasNotSuitableTankmen(self):
        ...
    def __isExperiencedPresetNeeded(self):
        ...
    def __getSortedTankmenByRoles(self):
        ...
    def __getSortedTankmen(self, presetIndex):
        ...
    def __getSortedTankmenForTTC(self, presetIndex):
        ...
    def __isExperiencedTankmenPresetInstalled(self):
        ...
    def __getFreeBerthsCount(self):
        ...
    def __getInventoryTankmen(self):
        ...
    def __setTankmenPresets(self):
        ...
    def __getInitialFilterCriteria(self):
        ...
    def __getFilterByTankmanRoleCriteria(self, tankmanRole):
        ...
    def __getExperiencedTankmen(self):
        ...
    def __getTankmanCandidateForRole(self, sortedTankmenByRating, experiencedTankmen, tankmanInVehicle=None):
        ...
