# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/params_utils.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import namedtuple as namedtuple
from constants import IS_CLIENT as IS_CLIENT, IS_WEB as IS_WEB, IS_CGF_DUMP as IS_CGF_DUMP, IS_LOAD_GLOSSARY as IS_LOAD_GLOSSARY, IS_EDITOR as IS_EDITOR
from items.components.shared_components import TemperatureGunParams as TemperatureGunParams, OverheatGunParams as OverheatGunParams
from math_common import round_py2_style as round_py2_style
from items.vehicles import VehicleDescriptor as VehicleDescriptor
AttributeModifier: Any

def convertModifiersList(modifiersList):
    ...
def extractModifier(modifiers, name):
    ...
def getTemperatureModifier(descr, modifierName):
    ...
def getHeatedAimingTime(aimingTime, descr):
    ...
def getHeatedShotDispersion(shotDispersion, descr):
    ...
def getTemperatureRateOfFire(descr, isVehicle=True):
    ...
