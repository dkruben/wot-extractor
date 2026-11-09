# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/easy_tank_equip/shells_preset_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import Array as Array
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.common.preset_model import PresetModel as PresetModel
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.shells_preset_slot_model import ShellsPresetSlotModel as ShellsPresetSlotModel

class ShellsPresetType(Enum):
    STANDARD = 'standard'
    ADVANCED = 'advanced'

class ShellsPresetModel(PresetModel):
    __slots__: tuple
    def __init__(self, properties=7, commands=0):
        ...
    def getType(self):
        ...
    def setType(self, value):
        ...
    def getItems(self):
        ...
    def setItems(self, value):
        ...
    @staticmethod
    def getItemsType():
        ...
    def _initialize(self):
        ...
