# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/easy_tank_equip/cards/consumables_card.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.impl.gen.view_models.constants.item_highlight_types import ItemHighlightTypes as ItemHighlightTypes
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.consumables_preset_model import ConsumablesPresetModel as ConsumablesPresetModel
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.consumables_preset_slot_model import ConsumablesPresetSlotModel as ConsumablesPresetSlotModel
from gui.impl.lobby.easy_tank_equip.cards.base_card import BasePreset as BasePreset, BaseCard as BaseCard
from gui.impl.lobby.easy_tank_equip.data_providers.consumables_data_provider import ConsumablesPresetInfo as ConsumablesPresetInfo, ConsumablesPresetSlotInfo as ConsumablesPresetSlotInfo
from gui.shared.money import Money as Money
from typing import Optional as Optional

class ConsumablesCard(BaseCard):
    def _getPreset(self):
        ...

class ConsumablesPreset(BasePreset):
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
