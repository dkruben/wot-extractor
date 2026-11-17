# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/helpers/blueprint_generator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from collections import namedtuple as namedtuple
import BigWorld as BigWorld
import Math as Math
import ResMgr as ResMgr
from items import vehicles as vehicles, parseIntCompactDescr as parseIntCompactDescr, ITEM_TYPES as ITEM_TYPES
from vehicle_systems import model_assembler as ma
from vehicle_systems.stricted_loading import makeCallbackWeak as makeCallbackWeak
from vehicle_systems.tankStructure import ModelsSetParams as ModelsSetParams
_logger: Any
_BLUEPRINT_BG_TEXTURE = 'gui/maps/blueprint_bg.png'
_BLUEPRINT_TEXTURE_PATH = 'img://customTexture:blueprint'
_BLUEPRINT_LAYOUTS_PATH = 'gui/blueprint_layouts.xml'
_BpProjections: Any
_BpLayout: Any
_BLUEPRINT_DEFAULT_LAYOUT: Any
g_blueprintGenerator: Any

class BlueprintGenerator(object):
    __cachedCompound: Any
    __pendingCompound: Any
    __layouts: Any
    __inProgress: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def generate(self, vehicleCD=None, vehicleName=None, clear=False):
        ...
    def cancel(self, vehicleCD=None, vehicleName=None):
        ...
    @classmethod
    def __getTexturePath(cls):
        ...
    def __loadVehicleCompound(self, vehicleDescr):
        ...
    def __onResourcesLoaded(self, vehicleName, resourceRefs):
        ...
    def __readConfig(self):
        ...
    def __getVehicleDescr(self, vehicleCD=None, vehicleName=None):
        ...
