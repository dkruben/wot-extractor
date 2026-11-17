# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/sounds/souls_collector_sound.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import SoundGroups as SoundGroups
from halloween.gui.sounds.sound_constants import SoulsCollectorSounds as SoulsCollectorSounds, SOULS_COLLECTOR_OBJ_NAME as SOULS_COLLECTOR_OBJ_NAME
from halloween.gui.sounds import playSound as playSound

class SoulsCollectorSound(object):
    _soulsCollectorSoundObject: Any
    _needNotifyCollectorFullFilled: Any
    def __init__(self, collectorComp):
        ...
    def destroy(self):
        ...
    def updateSoulsCollectorState(self, collected, capacity, isCollecting):
        ...
    def onFilling(self, collected):
        ...
