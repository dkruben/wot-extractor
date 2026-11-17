# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/sounds/SoundManager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from debug_utils import LOG_ERROR as LOG_ERROR, LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from gui.Scaleform.framework.entities.abstract.SoundManagerMeta import SoundManagerMeta as SoundManagerMeta
from gui.doc_loaders.GuiSoundsLoader import GuiSoundsLoader as GuiSoundsLoader
import SoundGroups as SoundGroups
_logger: Any

class SoundManager(SoundManagerMeta):
    sounds: Any
    def __init__(self):
        ...
    def _populate(self):
        ...
    def soundEventHandler(self, soundsTypeSection, state, eventType, eventID):
        ...
    def playControlSound(self, state, eventType, eventID):
        ...
    def playEffectSound(self, effectName):
        ...
