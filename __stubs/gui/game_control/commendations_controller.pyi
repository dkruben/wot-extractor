# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/commendations_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
import Event as Event
from gui.server_events import settings as settings
from PlayerEvents import g_playerEvents as g_playerEvents
from commendations_schema import commendationsConfigSchema as commendationsConfigSchema
from gui import SystemMessages as SystemMessages
from gui.SystemMessages import SM_TYPE as SM_TYPE
from skeletons.gui.game_control import ICommendationsController as ICommendationsController

class NotificationTypeTemplate(Enum):
    MESSAGES: tuple
    LIVE_TAGS: tuple
    @property
    def getEnable(self):
        ...
    @property
    def getDisable(self):
        ...

class CommendationsController(ICommendationsController):
    _modifiable: Any
    _isCommendationsEnabled: Any
    _isLiveTagsEnabled: Any
    onSettingsChanged: Any
    def __init__(self):
        ...
    @property
    def isCommendationsEnabled(self):
        ...
    @property
    def isLiveTagsEnabled(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def onAccountBecomeNonPlayer(self):
        ...
    def onAccountBecomePlayer(self):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def _onConfigModelUpdated(self, gpKey):
        ...
    def _updateLocalCache(self):
        ...
    def _processSwitchNotifications(self):
        ...
    def _notifyClient(self, lastSeenStatus, currentStatus, notifications):
        ...
