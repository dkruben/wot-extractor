# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/sounds/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import SoundGroups as SoundGroups
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.battle_control.avatar_getter import getSoundNotifications as getSoundNotifications
from last_stand.gui.ls_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from LSArenaPhasesComponent import LSArenaPhasesComponent as LSArenaPhasesComponent

class SoundComponentBase(object):
    _sessionProvider: Any
    _parent: Any
    def __init__(self, parent):
        ...
    @property
    def parent(self):
        ...
    @property
    def arenaPhases(self):
        ...
    @property
    def lsBattleGuiCtrl(self):
        ...
    def clearAndDestroy(self):
        ...
    def onAvatarReady(self):
        ...
    def onDestroy(self):
        ...

class ComponentsHolder(object):
    _components: Any
    _parent: Any
    _isDestroyed: Any
    def __init__(self, components, parent):
        ...
    def addComponents(self, components):
        ...
    def onAvatarReady(self):
        ...
    def onDestroy(self):
        ...
    def call(self, method, *args):
        ...

def playSound(eventName):
    ...
def getSound2D(eventName):
    ...
def playVoiceover(voiceover):
    ...
