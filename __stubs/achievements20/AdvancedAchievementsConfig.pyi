# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/achievements20/AdvancedAchievementsConfig.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import TYPE_CHECKING as TYPE_CHECKING
from achievements20.settings import AdvancedAchievementsConst as AdvancedAchievementsConst
from typing import Optional as Optional

class AdvancedAchievementsConfig(object):
    __slots__: tuple
    _config: Any
    def __init__(self, config):
        ...
    def isAdvancedAchievementEnabled(self):
        ...
    def isVehicleAchievementsEnabled(self):
        ...
    def isCustomizationAchievementsEnabled(self):
        ...
    def getExcludedVehicles(self):
        ...
    def getExcludedCustomizations(self):
        ...
