# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/tooltips/warning_tooltip_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class WarningDescription(Enum):
    SIMILARDEVICEALREADYINSTALLED = 'similar_device_already_installed'
    USELESSBATTLEBOOSTER = 'useless_battle_booster'
    USELESSCREWSKILLBATTLEBOOSTER = 'useless_crew_skill_battle_booster'

class WarningTooltipViewModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=2, commands=0):
        ...
    def getReason(self):
        ...
    def setReason(self, value):
        ...
    def getIsCritical(self):
        ...
    def setIsCritical(self, value):
        ...
    def _initialize(self):
        ...
