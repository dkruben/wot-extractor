# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/easy_tank_equip/data_providers/base_data_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from typing import TYPE_CHECKING as TYPE_CHECKING
import Event as Event
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.common.preset_model import PresetDisableReason as PresetDisableReason
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.common.proposal_model import ProposalDisableReason as ProposalDisableReason
from shared_utils import first as first
from gui.shared.money import ZERO_MONEY as ZERO_MONEY
from gui.shared.gui_items.gui_item_economics import ITEM_PRICE_ZERO as ITEM_PRICE_ZERO
from gui.shared.gui_items.gui_item_economics import ItemPrice as ItemPrice
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from gui.shared.money import Money as Money
from typing import List as List, Optional as Optional, Tuple as Tuple, Dict as Dict

class CardLogStatuses(str, Enum):
    SELECTED = 'selected'
    NOT_SELECTED = 'not_selected'
    DISABLED = 'disabled'
    INSTALLED = 'installed'

class SlotInfo(object):
    storedItemsCount: Any
    installedItemsCount: Any
    itemPrice: Any
    def __init__(self, storedItemsCount, installedItemsCount, itemPrice):
        ...

class PresetInfo(object):
    installed: Any
    storedItemsCount: Any
    installedItemsCount: Any
    itemPrice: Any
    disableReason: Any
    def __init__(self, installed, storedItemsCount=0, installedItemsCount=0, itemPrice=..., disableReason=...):
        ...

class BaseDataProvider(object):
    vehicle: Any
    lastCheckedBalance: Any
    currentPresetIndex: Any
    proposalDisableReason: Any
    __presets: Any
    __isProposalSelected: Any
    __em: Any
    onSelect: Any
    onSwitchPreset: Any
    onPricesUpdated: Any
    onPresetsUpdated: Any
    def __init__(self, vehicle, balance):
        ...
    @property
    def presets(self):
        ...
    @presets.setter
    def presets(self, value):
        ...
    @property
    def isProposalSelected(self):
        ...
    @isProposalSelected.setter
    def isProposalSelected(self, value):
        ...
    def initialize(self):
        ...
    def finalize(self):
        ...
    def selectProposal(self):
        ...
    def switchPreset(self, presetIndex):
        ...
    def updateBalance(self, balance):
        ...
    def isCurrentPresetDisableReasonChanged(self):
        ...
    def isCurrentPresetDisabledForApplying(self):
        ...
    def getBalanceRemains(self):
        ...
    def getPresetPrice(self):
        ...
    def isProposalDisabled(self):
        ...
    def isCurrentPresetDisabled(self):
        ...
    def getCardLogStatus(self):
        ...
    def applyNewPresetOnVehicle(self):
        ...
    def selectStatusChanged(self):
        ...
    def getPresetDataForApplying(self):
        ...
    def saveAccountSettings(self):
        ...
    def getPresets(self):
        ...
    def updatePresets(self, fullUpdate=False):
        ...
    def getCurrentPresetItemsIds(self):
        ...
    def setValuesFromCurrentPreset(self):
        ...
    def revertChangesFromSelectedPreset(self):
        ...
    def swapSlots(self, firstSlot, secondSlot):
        ...
    def _getPresetDataForApplying(self):
        ...
    def _getCurrentPresetInfo(self, defaultIndex):
        ...
