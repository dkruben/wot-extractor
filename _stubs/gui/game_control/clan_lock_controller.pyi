# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/clan_lock_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import iteritems as iteritems
import Event as Event
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.shared.gui_items import CLAN_LOCK as CLAN_LOCK
from gui.shared.utils.scheduled_notifications import Notifiable as Notifiable, PeriodicNotifier as PeriodicNotifier
from helpers import dependency as dependency
from skeletons.gui.game_control import IClanLockController as IClanLockController
from skeletons.gui.shared import IItemsCache as IItemsCache
_UPDATE_LOCKS_PERIOD = 60

class ClanLockController(IClanLockController, Notifiable):
    itemsCache: Any
    onClanLockUpdate: Any
    __lockedVehicles: Any
    __isFullLock: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def onLobbyStarted(self, ctx):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def onDisconnected(self):
        ...
    def __stop(self):
        ...
    def __updateVehicleLocks(self, locks):
        ...
    def __updateGlobalLocks(self, locks):
        ...
    def __notificationStartStop(self):
        ...
