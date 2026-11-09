# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/helpers/DecalMap.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from functools import partial as partial
from future.utils import viewitems as viewitems
import BigWorld as BigWorld
import ResMgr as ResMgr
import material_kinds as material_kinds
import persistent_data_cache as pdc
from constants import IS_EDITOR as IS_EDITOR
from debug_utils import LOG_ERROR as LOG_ERROR, LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
g_instance = None

class DecalMap(object):
    __texMap: Any
    __textureSets: Any
    __chassisEffectGroups: Any
    def __init__(self, config):
        ...
    def _init(self, config):
        ...
    def _initGroups(self, config, scaleFactor=1.0):
        ...
    def getIndex(self, name):
        ...
    def getTextureSet(self, name):
        ...
    @property
    def textureSets(self):
        ...
    @property
    def chassisEffectGroups(self):
        ...

def _readFloat(dataSec, name, minVal, maxVal, defaultVal):
    ...
def _readCfg(dataSec):
    ...
def init(section):
    ...
