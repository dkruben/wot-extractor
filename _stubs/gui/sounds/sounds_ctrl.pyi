# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/sounds/sounds_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
import MusicControllerWWISE as _MC
import SoundGroups as SoundGroups
from gui.sounds.ambients import GuiAmbientsCtrl as GuiAmbientsCtrl
from gui.sounds.sound_constants import EnabledStatus as EnabledStatus
from gui.sounds.sound_systems import getCurrentSoundSystem as getCurrentSoundSystem
from gui.sounds.sound_utils import SOUND_DEBUG as SOUND_DEBUG
from helpers import dependency as dependency
from skeletons.gui.game_control import IGameSessionController as IGameSessionController
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.sounds import ISoundsController as ISoundsController

class SoundsController(ISoundsController):
    itemsCache: Any
    gameSession: Any
    __soundSystem: Any
    __guiAmbients: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def start(self):
        ...
    def stop(self, isDisconnected=False):
        ...
    @property
    def system(self):
        ...
    def enable(self):
        ...
    def disable(self):
        ...
    def isEnabled(self):
        ...
    def setEnvForSpace(self, spaceID, newEnv):
        ...
    def __onPremiumChanged(self, isPremium, attrs, premiumExpiryTime):
        ...
    def __setAccountAttrs(self, restartSounds=False):
        ...
