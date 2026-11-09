# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/cgf_components/soul_collector_wrappers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from builtins import range as range
import CGF as CGF
import GenericComponents as GenericComponents
from halloween.cgf_components.soul_collector_components import SoulCollectorComponent as SoulCollectorComponent, SoulCollectorProgressComponent as SoulCollectorProgressComponent
_logger: Any

class _AnimatorStatus(object):
    STATUS_ENABLED = 1.0
    STATUS_DISABLED = 0.0

class SoulCollectorProgressWrapper(object):
    _currentProgress: Any
    _gos: Any
    _dynAccess: Any
    progressSectors: Any
    sectorOffsetY: Any
    progressSequence: Any
    def __init__(self, dynAccess, goLink):
        ...
    def isReady(self):
        ...
    def onDestroy(self):
        ...
    def update(self, progress):
        ...
    def _getAnimator(self, go, isWritable=False):
        ...

class SoulCollectorWrapper(object):
    _isReady: Any
    _go: Any
    _dynAccess: Any
    loadProgressGO: Any
    energyGlowAnimator: Any
    auraAnimator: Any
    drainerAnimator: Any
    _progressComponent: Any
    def __init__(self, go, component):
        ...
    def onDestroy(self):
        ...
    @property
    def isReady(self):
        ...
    def updateProgress(self, progress):
        ...
    def updateIsCollecting(self, isCollecting):
        ...
    def _getAnimator(self, uuid):
        ...
    @staticmethod
    def init(go):
        ...
