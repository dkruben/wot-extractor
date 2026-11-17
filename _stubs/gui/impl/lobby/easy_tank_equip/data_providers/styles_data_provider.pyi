# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/easy_tank_equip/data_providers/styles_data_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import random as random
from typing import TYPE_CHECKING as TYPE_CHECKING
from gui.Scaleform.daapi.view.lobby.customization.shared import getStyledModeRequestData as getStyledModeRequestData
from gui.customization.shared import C11N_ITEM_TYPE_MAP as C11N_ITEM_TYPE_MAP
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.common.proposal_model import ProposalDisableReason as ProposalDisableReason
from gui.impl.lobby.easy_tank_equip.data_providers.base_data_provider import BaseDataProvider as BaseDataProvider, PresetInfo as PresetInfo
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.gui_item_economics import ITEM_PRICE_ZERO as ITEM_PRICE_ZERO
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from items import vehicles as vehicles
from items.components.c11n_constants import EMPTY_ITEM_ID as EMPTY_ITEM_ID
from items.components.c11n_constants import SeasonType as SeasonType
from shared_utils import first as first
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.server_events import IEventsCache as IEventsCache
from gui.shared.gui_items.customization.c11n_items import Style as Style
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from typing import List as List, Optional as Optional, Dict as Dict
from vehicle_outfit.outfit import Outfit as Outfit

class StylesPresetInfo(PresetInfo):
    style: Any
    def __init__(self, installed, storedItemsCount, installedItemsCount, itemPrice, style):
        ...

class StylesDataProvider(BaseDataProvider):
    PRESETS_COUNT = 3
    __eventsCache: Any
    __c11nService: Any
    __currentStyle: Any
    __season: Any
    __vehicleCD: Any
    __stylesPresets: Any
    __customizationCache: Any
    isProposalSelected: Any
    presets: Any
    currentPresetIndex: Any
    proposalDisableReason: Any
    def __init__(self, vehicle, balance):
        ...
    def initialize(self):
        ...
    def finalize(self):
        ...
    def setValuesFromCurrentPreset(self):
        ...
    def revertChangesFromSelectedPreset(self):
        ...
    def getPresets(self):
        ...
    def updatePresets(self, fullUpdate=False):
        ...
    def swapSlots(self, firstSlot, secondSlot):
        ...
    def getCurrentPresetItemsIds(self):
        ...
    def _getPresetDataForApplying(self):
        ...
    def __applyCamouflageTTC(self):
        ...
    def __getPresetsInfo(self):
        ...
    def __setStylesPresets(self):
        ...
    def __getStylesPresetInfo(self, style):
        ...
    def __isStyleInstalled(self, style):
        ...
    def __getAvailableStyles(self):
        ...
    def __getStyleRequestData(self, vehicle, vehicleCD, style, season):
        ...
    @staticmethod
    def __getRandomStyles(styles, count):
        ...
