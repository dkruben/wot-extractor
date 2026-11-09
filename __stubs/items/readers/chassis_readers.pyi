# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/readers/chassis_readers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import math as math
from future.utils import lrange as lrange
from past.builtins import intern as intern
import ResMgr as ResMgr
from items import _xml as _xml
from items.components import chassis_components as chassis_components
from items.components import component_constants as component_constants
from items.components.chassis_components import SplineTrackPairDesc as SplineTrackPairDesc
from items.readers import shared_readers as shared_readers
from debug_utils import LOG_ERROR as LOG_ERROR
from constants import IS_EDITOR as IS_EDITOR, IS_CLIENT as IS_CLIENT, IS_UE_EDITOR as IS_UE_EDITOR
import Vehicular as Vehicular

def readWheelsAndGroups(xmlCtx, section):
    ...
def readGroundNodesAndGroups(xmlCtx, section, cache):
    ...
def readTrackNodes(xmlCtx, section):
    ...
def readTrackSplineParams(xmlCtx, section):
    ...
def readTraces(xmlCtx, section, centerOffset, cache):
    ...
def readTrackBasicParams(xmlCtx, section, cache):
    ...
def __readDebrisParams(xmlCtx, section, cache):
    ...
def readLeveredSuspension(xmlCtx, section, cache):
    ...
def readSplineTrackPairDesc(xmlCtx, section, cache):
    ...
def readSplineConfig(xmlCtx, section, cache):
    ...
