# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/views/loadout_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_royale_equipment_model import BattleRoyaleEquipmentModel as BattleRoyaleEquipmentModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_royale_respawn_ability_model import BattleRoyaleRespawnAbilityModel as BattleRoyaleRespawnAbilityModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_royale_shell_model import BattleRoyaleShellModel as BattleRoyaleShellModel

class LoadoutViewModel(ViewModel):
    __slots__: tuple
    showUpgrades: Any
    def __init__(self, properties=3, commands=1):
        ...
    @property
    def respawnAbility(self):
        ...
    @staticmethod
    def getRespawnAbilityType():
        ...
    def getShells(self):
        ...
    def setShells(self, value):
        ...
    @staticmethod
    def getShellsType():
        ...
    def getEquipment(self):
        ...
    def setEquipment(self, value):
        ...
    @staticmethod
    def getEquipmentType():
        ...
    def _initialize(self):
        ...
