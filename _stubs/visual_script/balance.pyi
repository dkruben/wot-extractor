# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/visual_script/balance.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import os as os
import BigWorld as BigWorld
import ResMgr as ResMgr
import constants as constants
import nations as nations
import items.vehicles as iv
from visual_script.block import Meta as Meta, Block as Block, InitParam as InitParam, buildStrKeysValue as buildStrKeysValue
from visual_script.misc import errorVScript as errorVScript, ASPECT as ASPECT, EDITOR_TYPE as EDITOR_TYPE
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE, arrayOf as arrayOf
from visual_script.type import VScriptStruct as VScriptStruct, VScriptStructField as VScriptStructField
_dataSection = None
_gList = None

class VsePaths(object):
    cwd: Any
    def __enter__(self):
        ...
    def __exit__(self, exc_type, exc_val, exc_tb):
        ...

class EquipmentMeta(Meta):
    @classmethod
    def blockColor(cls):
        ...
    @classmethod
    def blockCategory(cls):
        ...
    @classmethod
    def blockIcon(cls):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class ConfigParamStruct(VScriptStruct):
    name: Any
    value: Any
    def __repr__(self):
        ...

class ReloadClientPlan(Block, EquipmentMeta):
    _inSlot: Any
    _out: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self):
        ...

class ResMgrSpy(object):
    spyParams: Any
    __spyParamsPaths: Any
    __block: Any
    def __init__(self, block, params):
        ...
    def stop(self):
        ...
    def traceCalls(self, frame, event, arg):
        ...
    def __traceCalls(self, frame, event):
        ...
    def __path(self, section):
        ...

class IntCompDescrDecoder(Block, EquipmentMeta):
    _intCDs: Any
    def __init__(self, *args, **kwargs):
        ...
    def captionText(self):
        ...
    def __parseCDs(self):
        ...
    def _execute(self):
        ...
    def validate(self):
        ...

class EquipmentParams(Block, EquipmentMeta):
    eqName: Any
    _inSlot: Any
    _params: Any
    _out: Any
    def __init__(self, *args, **kwargs):
        ...
    def captionText(self):
        ...
    @classmethod
    def initParams(cls):
        ...
    def _execute(self):
        ...
    def validate(self):
        ...
    def _processParams(self):
        ...

def cache():
    ...
def getVehicleList(naton):
    ...
def eqDataSection(eqName):
    ...
def getArtefact(name):
    ...
