# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/easy_tank_equip/cards/opt_devices_card.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import TYPE_CHECKING as TYPE_CHECKING
from gui.impl.gen import R as R
from gui.impl.gen.view_models.constants.item_highlight_types import ItemHighlightTypes as ItemHighlightTypes
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.opt_devices_preset_model import OptDevicesPresetModel as OptDevicesPresetModel
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.opt_devices_preset_slot_model import OptDevicesPresetSlotModel as OptDevicesPresetSlotModel
from gui.impl.gen.view_models.views.lobby.tank_setup.common.specialization_model import SpecializationModel as SpecializationModel
from gui.impl.lobby.easy_tank_equip.cards.base_card import BasePreset as BasePreset, BaseCard as BaseCard
from gui.impl.lobby.tank_setup.tank_setup_helper import getCategoriesMask as getCategoriesMask
from typing import Optional as Optional
from gui.impl.lobby.easy_tank_equip.data_providers.opt_devices_data_provider import OptionalDevicesPresetInfo as OptionalDevicesPresetInfo, OptDevicesPresetSlotInfo as OptDevicesPresetSlotInfo
from gui.shared.gui_items.artefacts import OptionalDevice as OptionalDevice
from gui.shared.gui_items.vehicle_equipment import OptDeviceSlotData as OptDeviceSlotData
from gui.shared.money import Money as Money

class OptDevicesCard(BaseCard):
    def _getPreset(self):
        ...

class OptDevicesPreset(BasePreset):
    @classmethod
    def getPresetModel(cls):
        ...
    @classmethod
    def fillPresetModel(cls, model, presetInfo, balance=None):
        ...
    @classmethod
    def __fillPresetItemsModels(cls, model, presetInfo):
        ...
    @classmethod
    def __fillPresetSlotModel(cls, model, presetSlotInfo):
        ...
    @classmethod
    def __updateOverlayAspects(cls, model, presetSlotOptDevice):
        ...
    @classmethod
    def __updateSpecializations(cls, model, presetSlotOptDevice, slotData):
        ...
