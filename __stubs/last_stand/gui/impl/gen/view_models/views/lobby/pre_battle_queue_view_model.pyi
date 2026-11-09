# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/gen/view_models/views/lobby/pre_battle_queue_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from last_stand.gui.impl.gen.view_models.views.lobby.vehicle_info_block_model import VehicleInfoBlockModel as VehicleInfoBlockModel
from last_stand.gui.impl.gen.view_models.views.lobby.widgets.difficulty_item_model import DifficultyItemModel as DifficultyItemModel
from gui.impl.gen.view_models.views.selectable_view_model import SelectableViewModel as SelectableViewModel

class PreBattleQueueViewModel(SelectableViewModel):
    __slots__: tuple
    onExitBattle: Any
    onEscape: Any
    def __init__(self, properties=4, commands=4):
        ...
    @property
    def selectedVehicle(self):
        ...
    @staticmethod
    def getSelectedVehicleType():
        ...
    @property
    def selectedDifficulty(self):
        ...
    @staticmethod
    def getSelectedDifficultyType():
        ...
    def getIsExitButtonAvailable(self):
        ...
    def setIsExitButtonAvailable(self, value):
        ...
    def getTimerStartTime(self):
        ...
    def setTimerStartTime(self, value):
        ...
    def _initialize(self):
        ...
