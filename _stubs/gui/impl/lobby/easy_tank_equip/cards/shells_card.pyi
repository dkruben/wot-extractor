# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/easy_tank_equip/cards/shells_card.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from frameworks.wulf.view.array import fillViewModelsArray as fillViewModelsArray
from gui.impl.gen.view_models.common.vehicle_mechanic_model import VehicleMechanicModel as VehicleMechanicModel
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.shells_preset_slot_model import ShellsPresetSlotModel as ShellsPresetSlotModel
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.shells_preset_model import ShellsPresetModel as ShellsPresetModel
from gui.impl.lobby.common.vehicle_model_helpers import fillVehicleMechanicModel as fillVehicleMechanicModel
from gui.impl.lobby.easy_tank_equip.cards.base_card import BasePreset as BasePreset, BaseCard as BaseCard
from gui.impl.lobby.easy_tank_equip.data_providers.shells_data_provider import ShellsPresetInfo as ShellsPresetInfo, ShellsPresetSlotInfo as ShellsPresetSlotInfo
from gui.shared.money import Money as Money
from typing import Optional as Optional

class ShellsCard(BaseCard):
    def _getPreset(self):
        ...

class ShellsPreset(BasePreset):
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
