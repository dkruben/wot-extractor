# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/vehicle_hub/sub_presenters/armor/config/models.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from dict2model import models as models

class ColorListModel(models.Model):
    __slots__: tuple
    normalArmor: Any
    spacedArmor: Any
    ricochet: Any
    noDamage: Any
    def __init__(self, normalArmor, spacedArmor, ricochet, noDamage):
        ...
    def __repr__(self):
        ...

class ArmorScaleModel(models.Model):
    __slots__: tuple
    min: Any
    max: Any
    def __init__(self, min, max):
        ...
    def __repr__(self):
        ...

class TierModel(models.Model):
    __slots__: tuple
    number: Any
    normalArmor: Any
    spacedArmor: Any
    defaultVehicle: Any
    def __init__(self, number, normalArmor, spacedArmor, defaultVehicle):
        ...
    def __repr__(self):
        ...

class TierListModel(models.Model):
    __slots__: tuple
    tier: Any
    def __init__(self, tier):
        ...
    def __repr__(self):
        ...
    def getTierModel(self, tier):
        ...

class ConfigModel(models.Model):
    __slots__: tuple
    tierList: Any
    colorList: Any
    blindColorList: Any
    blendingAlpha: Any
    def __init__(self, tierList, colorList, blindColorList, blendingAlpha):
        ...
    def getActualColorList(self, isColorBlind):
        ...
    def _reprArgs(self):
        ...
