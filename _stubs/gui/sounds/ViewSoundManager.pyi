# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/sounds/ViewSoundManager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import WWISE as WWISE
import SoundGroups as SoundGroups
from debug_utils import LOG_WARNING as LOG_WARNING
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader, GuiGlobalSpaceID as GuiGlobalSpaceID

class _ViewSoundsManager(object):
    __sounds: Any
    __exitStates: Any
    __soundSpaceSettings: Any
    __started: Any
    __consumers: Any
    __privateSounds: Any
    def __init__(self):
        ...
    @property
    def isUsed(self):
        ...
    def clear(self, stopPersistent=False, requester=None):
        ...
    def playSound(self, eventName, owner=None):
        ...
    def isSoundPlaying(self, eventName):
        ...
    def stopSound(self, eventName):
        ...
    def playInstantSound(self, eventName):
        ...
    @staticmethod
    def setState(name, value):
        ...
    @staticmethod
    def setRTPC(name, value):
        ...
    def register(self, consumerID, soundSpaceSettings):
        ...
    def unregister(self, consumerID):
        ...
    def startSpace(self, spaceSettings):
        ...
    def __stopAllSounds(self, stopPersistent):
        ...
    def __setStates(self, states):
        ...
    def __invalidatePriority(self, eventName):
        ...
