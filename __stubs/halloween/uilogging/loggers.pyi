# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/uilogging/loggers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from typing import TYPE_CHECKING as TYPE_CHECKING
from halloween.gui.sounds.halloween_sound_controller import getEventVoiceoverLanguage as getEventVoiceoverLanguage
from halloween.gui.sounds.sound_constants import SoundLanguage as SoundLanguage
from halloween.uilogging.logging_constants import FEATURE as FEATURE, HWLogActions as HWLogActions, HWLogKeys as HWLogKeys, MIN_VO_TIME as MIN_VO_TIME
from uilogging.base.logger import MetricsLogger as MetricsLogger, createPartnerID as createPartnerID
_logger: Any
VO_MAP: dict

class HWMetricsLogger(MetricsLogger):
    __slots__: tuple
    _view: Any
    _partnerID: Any
    def __init__(self, view, partnerID=None):
        ...
    def onStartView(self, action):
        ...
    def onStopView(self, action, itemState=None, info=None, timeLimit=0):
        ...
    def onLog(self, action, item, itemState=None):
        ...
    def onClick(self, item, itemState=None):
        ...

class DecryptionMetricsLogger(HWMetricsLogger):
    __slots__: tuple
    _voLang: Any
    def __init__(self):
        ...
    def onStartView(self, *_):
        ...
    def onStopView(self, itemState=None, stopVO=False, *_):
        ...
    def startVO(self):
        ...
    def stopVO(self, itemState):
        ...
