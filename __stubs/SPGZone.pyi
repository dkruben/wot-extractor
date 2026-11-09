# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/SPGZone.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
import BigWorld as BigWorld
import Math as Math
import TriggersManager as TriggersManager
from AreaOfEffect import AreaOfEffect as AreaOfEffect

class SPGZone(AreaOfEffect, TriggersManager.ITriggerListener):
    _TRIGGER_NAME_TEMPLATE = 'spg_zone_{}'
    _TRIGGER_EXIT_INTERVAL = 1.0
    _TRIGGER_SCALE: tuple
    _TRIGGER_DIRECTION_AXIS = 1
    _triggerName: Any
    _triggerId: Any
    _hpCallbackId: Any
    __yawHitPrediction: Any
    __hitPredictionDuration: Any
    def __init__(self):
        ...
    def onEnterWorld(self, prereqs):
        ...
    def onLeaveWorld(self):
        ...
    def onTriggerActivated(self, args):
        ...
    def onTriggerDeactivated(self, args):
        ...
    def _removeHitPrediction(self):
        ...
    def _showMarker(self):
        ...
