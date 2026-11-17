# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/configs/hw_upgrades_config.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import os as os
import typing as typing
import ResMgr as ResMgr
import section2dict as section2dict
from dict2model import models as models, schemas as schemas, fields as fields
from soft_exception import SoftException as SoftException
_UPGRADES_CONFIG_PATH: Any
_DEFAULT_VARIANT = 'DEFAULT'
upgradeParamSchema: Any
upgradeVariantSchema: Any
upgradeSchema: Any
upgradesConfigSchema: Any
_g_upgradesConfig = None

class UpgradeParamModel(models.Model):
    __slots__: tuple
    name: Any
    value: Any
    def __init__(self, name, value=''):
        ...

class UpgradeVariantModel(models.Model):
    __slots__: tuple
    param: Any
    vehicle: Any
    def __init__(self, param, vehicle=None):
        ...

class UpgradeModel(models.Model):
    __slots__: tuple
    name: Any
    variant: Any
    def __init__(self, name, variant=None):
        ...
    def getVehicleConfig(self, vehicleName):
        ...
    def getDefaultConfig(self):
        ...

class UpgradesConfigModel(models.Model):
    __slots__: tuple
    upgrade: Any
    def __init__(self, upgrade):
        ...

def initialize():
    ...
def getConfig():
    ...
