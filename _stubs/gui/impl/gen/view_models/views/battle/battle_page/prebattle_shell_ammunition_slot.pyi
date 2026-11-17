# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/battle/battle_page/prebattle_shell_ammunition_slot.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import IntEnum as IntEnum
from gui.impl.gen.view_models.views.lobby.tank_setup.common.shell_ammunition_slot import ShellAmmunitionSlot as ShellAmmunitionSlot

class ShellBattleState(IntEnum):
    NORMAL = 0
    CURRENT = 1
    NEXT = 2

class PrebattleShellAmmunitionSlot(ShellAmmunitionSlot):
    __slots__: tuple
    def __init__(self, properties=17, commands=0):
        ...
    def getShellState(self):
        ...
    def setShellState(self, value):
        ...
    def _initialize(self):
        ...
