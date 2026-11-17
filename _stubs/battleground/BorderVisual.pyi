# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/battleground/BorderVisual.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
from collections import namedtuple as namedtuple
from future.utils import viewitems as viewitems
import BigWorld as BigWorld
import ResMgr as ResMgr
from Math import Matrix as Matrix, Vector3 as Vector3
import math_utils as math_utils
from epic_constants import SECTOR_EDGE_STATE as SECTOR_EDGE_STATE
from items import _xml as _xml
CONFIG_FILE = 'scripts/dynamic_objects.xml'
BORDER_VISUAL_TAG = 'SectorBorderVisual'
VisualSetting: Any
ModelSetting: Any
DashesParams: Any
g_borderVisualSettings: Any

class BorderVisual(object):
    __DEFAULT_DASH_SIZE: tuple
    __DEFAULT_DASH_COLOR = 4294967295
    __direction: Any
    __length: Any
    __numModelsPerEdgeState: Any
    __terrainModels: Any
    __attachNodes: Any
    __modelOffsets: Any
    __rootModel: Any
    __rootMatrix: Any
    __edgeState: Any
    def __init__(self):
        ...
    def create(self, fromPos, toPos, currentEdgeState=...):
        ...
    def destroy(self):
        ...
    def showState(self, edgeState):
        ...
    def __getDashesParams(self, edgeState):
        ...

def _readModelSetting(ctx, section):
    ...
def _readVisualSettings():
    ...
