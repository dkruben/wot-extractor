# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/marker_items.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import Math as Math
import copy as copy
import ResMgr as ResMgr
from extension_utils import importClass as importClass
from gui.Scaleform.daapi.view.battle.shared.component_marker.markers_components import ComponentBitMask as FLAG, COMPONENT_MARKER_TYPE_NAMES as COMPONENT_MARKER_TYPE_NAMES
from gui.Scaleform.daapi.view.battle.shared.component_marker.markers import MarkerBase as MarkerBase
from soft_exception import SoftException as SoftException
DEFAULT_MARKER = 'DEFAULT'
_COMPONENT_MARKERS_CONFIG = 'gui/component_marker_items.xml'

class MarkerParamsFactory(object):
    MARKER_DATA: dict
    @classmethod
    def readConfigs(cls, path=...):
        ...
    @classmethod
    def getMarkerParams(cls, matrix, markerStyle=..., bitMask=...):
        ...
    @classmethod
    def buildBitMask(cls, params):
        ...
    @classmethod
    def _readParams(cls, section):
        ...
    @classmethod
    def _readComponents(cls, config, section):
        ...
    @classmethod
    def _readComponent(cls, section, componentType):
        ...

def init():
    ...
