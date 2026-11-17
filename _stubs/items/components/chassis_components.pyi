# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/components/chassis_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from future.utils import viewitems as viewitems
from items.components import path_builder as path_builder
from py2to3.patched_future import with_metaclass as with_metaclass
from wrapped_reflection_framework import reflectedNamedTuple as reflectedNamedTuple, ReflectionMetaclass as ReflectionMetaclass
__all__: tuple
Wheel: Any
WheelGroup: Any
WheelsConfig: Any
TrackPair: Any
TrackNode: Any
TrackBasicVisualParams: Any
TrackPairParams: Any
TrackPairDebris: Any
TrackDebrisParams: Any
TrackSplineParams: Any
GroundNode: Any
GroundNodeGroup: Any
Traces: Any
LeveredSuspensionConfig: Any
SuspensionLever: Any
SplineSegmentModelSet: Any
SplineConfig: Any

# base nao representavel no stub: with_metaclass(...)
class SplineTrackPairDesc:
    __slots__: tuple
    trackPairIdx: Any
    leftDesc: Any
    rightDesc: Any
    segmentLength: Any
    segmentOffset: Any
    segment2Offset: Any
    atlasUTiles: Any
    atlasVTiles: Any
    segmentModelSets: Any
    def __init__(self, trackPairIdx, segmentModelSets, leftDesc, rightDesc, segmentLength, segmentOffset, segment2Offset, atlasUTiles, atlasVTiles):
        ...
    def segmentModelLeft(self, modelSetName=''):
        ...
    def segmentModelRight(self, modelSetName=''):
        ...
    def segment2ModelLeft(self, modelSetName=''):
        ...
    def segment2ModelRight(self, modelSetName=''):
        ...
    def _getModelSet(self, modelSetName):
        ...
    def prerequisites(self, modelSet):
        ...
