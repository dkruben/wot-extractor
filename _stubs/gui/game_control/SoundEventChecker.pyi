# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/SoundEventChecker.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.app_loader import sf_lobby as sf_lobby
from gui.shared.SoundEffectsId import SoundEffectsId as SoundEffectsId
from gui.shared.money import Money as Money, Currency as Currency, MONEY_UNDEFINED as MONEY_UNDEFINED
from helpers import dependency as dependency
from skeletons.gui.game_control import ISoundEventChecker as ISoundEventChecker
from skeletons.gui.shared import IItemsCache as IItemsCache
_SPEND_SINGLE_SOUNDS: dict
_EARN_SINGLE_SOUNDS: dict
_SPEND_MULTI_SOUNDS: dict
_EARN_MULTI_SOUNDS: dict

class SoundEventChecker(ISoundEventChecker):
    itemsCache: Any
    __currentMoney: Any
    __isLocked: Any
    __spendCurrencies: Any
    __earnCurrencies: Any
    def __init__(self):
        ...
    # decorador original: @sf_lobby
    def app(self):
        ...
    def onLobbyStarted(self, ctx):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def onDisconnected(self):
        ...
    def lockPlayingSounds(self):
        ...
    def unlockPlayingSounds(self, restore=True):
        ...
    def __stop(self):
        ...
    def __playSound(self, soundName):
        ...
    def __playAllSounds(self):
        ...
    def __onStatsChanged(self, stats):
        ...
    @classmethod
    def __getSoundID(cls, currencies, singleSounds, multiSounds, defSound):
        ...
