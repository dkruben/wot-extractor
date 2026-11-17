# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/badges_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from future.utils import viewvalues as viewvalues
import Event as Event
import constants as constants
from adisp import adisp_process as adisp_process
from gui import SystemMessages as SystemMessages
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.shared.gui_items.processors.common import BadgesSelector as BadgesSelector
from gui.shared.tutorial_helper import getTutorialGlobalStorage as getTutorialGlobalStorage
from gui.shared.utils.scheduled_notifications import Notifiable as Notifiable, AcyclicNotifier as AcyclicNotifier
from helpers import dependency as dependency
from skeletons.gui.game_control import IBadgesController as IBadgesController
from skeletons.gui.shared import IItemsCache as IItemsCache
from tutorial.control.context import GLOBAL_FLAG as GLOBAL_FLAG
from typing import Optional as Optional
from gui.shared.gui_items.badge import Badge as Badge

class BadgesController(IBadgesController, Notifiable):
    __itemsCache: Any
    onUpdated: Any
    __currentSelectedPrefix: Any
    __currentSelectedSuffix: Any
    __pendingBadges: Any
    __tutorStorage: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def onDisconnected(self):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def onLobbyStarted(self, ctx):
        ...
    def select(self, badges):
        ...
    def getPrefix(self):
        ...
    def getSuffix(self):
        ...
    def __clear(self):
        ...
    def __updateBadges(self, *_):
        ...
    def __initCurrentBadges(self):
        ...
    @staticmethod
    def __getTimer():
        ...
    def __timerUpdate(self):
        ...
    def __selectOnClient(self, badges):
        ...
    # decorador original: @adisp_process
    def __selectOnServer(self):
        ...
    def __badgesProcessing(self):
        ...
