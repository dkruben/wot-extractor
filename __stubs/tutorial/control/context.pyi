# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/tutorial/control/context.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
import Event as Event
import SoundGroups as SoundGroups
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from tutorial.control import TutorialProxyHolder as TutorialProxyHolder
from tutorial.logger import LOG_MEMORY as LOG_MEMORY, LOG_ERROR as LOG_ERROR
__all__: tuple

class StartReqs(object):
    lobbyContext: Any
    def __del__(self):
        ...
    def isEnabled(self):
        ...
    def prepare(self, ctx):
        ...
    def process(self, descriptor, ctx):
        ...

class BonusesRequester(TutorialProxyHolder):
    _completed: Any
    def __init__(self, completed):
        ...
    def getCompleted(self):
        ...
    def setCompleted(self, completed):
        ...
    def isStillRunning(self):
        ...
    def getChapter(self, chapterID=None):
        ...
    def request(self, chapterID=None):
        ...

class SOUND_EVENT(object):
    HINT_SHOWN = 4
    ANIMATION_STARTED = 5

class SoundPlayer(object):
    _muted: Any
    _enabled: Any
    def __init__(self):
        ...
    def setMuted(self, value):
        ...
    def isMuted(self):
        ...
    def setEnabled(self, value):
        ...
    def isEnabled(self):
        ...
    def play(self, event, sndID=None):
        ...
    def stop(self):
        ...
    def isPlaying(self, event, sndID=None):
        ...
    def goToNextChapter(self):
        ...

class NoSound(SoundPlayer):
    def play(self, event, sndID=None):
        ...
    def stop(self):
        ...

class SimpleSoundPlayer(SoundPlayer):
    def play(self, _, sndID=None):
        ...
    def stop(self):
        ...

class GLOBAL_FLAG(object):
    MAY_PAWN_PERSONAL_MISSION = '_MayPawnPersonalMission'
    HAVE_NEW_BADGE = '_HaveNewBadge'
    LOBBY_MENU_ITEM_MANUAL = '_LobbyMenuItemManual'
    HAVE_NEW_SUFFIX_BADGE = '_HaveNewSuffixBadge'
    BADGE_PAGE_HAS_NEW_SUFFIX_BADGE = '_BadgePageHasNewSuffixBadge'
    COLLECTIBLE_VEHICLE_PREVIEW_ENABLED = '_CollectibleVehiclePreviewEnabled'
    DOGTAGS_ENABLED = '_DogTagsEnabled'
    HAVE_NEW_ANIMATED_DOGTAG = '_HaveNewAnimatedDogTag'
    VEH_POST_PROGRESSION_ENABLED = '_VehPostProgressionEnabled'
    HANGAR_VEH_POST_PROGRESSION_PURCHASABLE = '_HangarVehPostProgressionPurchasable'
    RESEARCH_VEH_POST_PROGRESSION_PURCHASABLE = '_ResearchVehPostProgressionPurchasable'
    VISITED_ACHIEVEMENTS_FROM_NOTIFICATION = '_VisitedAchievementsFromNotification'
    UNLOCKED_3D_CUSTOMIZATION = '_Unlocked3DCustomization'
    ALL: tuple

class GlobalStorage(object):
    __slots__: tuple
    __storage: dict
    __default: dict
    onSetValue: Any
    attribute: Any
    def __init__(self, attribute, defaultValue):
        ...
    def __repr__(self):
        ...
    def __set__(self, _, value):
        ...
    def __get__(self, instance, owner=None):
        ...
    def value(self):
        ...
    @classmethod
    def setFlags(cls, flags):
        ...
    @classmethod
    def clearFlags(cls):
        ...
    @classmethod
    def all(cls):
        ...
    @classmethod
    def getValue(cls, attribute):
        ...
    @classmethod
    def setValue(cls, attribute, value, showImmediately=True):
        ...
