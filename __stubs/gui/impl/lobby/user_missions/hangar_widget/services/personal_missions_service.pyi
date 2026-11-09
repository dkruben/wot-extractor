# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/user_missions/hangar_widget/services/personal_missions_service.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewvalues as viewvalues
import Event as Event
from PlayerEvents import g_playerEvents as g_playerEvents
from config_schemas.umg_config import umgConfigSchema as umgConfigSchema
from constants import QUEUE_TYPE as QUEUE_TYPE
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, g_eventBus as g_eventBus
from gui.shared.events import PersonalMissionsEvent as PersonalMissionsEvent
from helpers import dependency as dependency
from personal_missions import PM_BRANCH as PM_BRANCH
from skeletons.gui.server_events import IEventsCache as IEventsCache
from gui.impl.lobby.user_missions.hangar_widget.services import IPersonalMissionsService as IPersonalMissionsService
from gui.impl.lobby.user_missions.hangar_widget.services.service_events import ServiceEvents as ServiceEvents

class PersonalMissionsService(IPersonalMissionsService, ServiceEvents):
    _eventsCache: Any
    _enabledQueues: tuple
    onPersonalMissionsChanged: Any
    onWidgetQuestIDMarkedAsNew: Any
    onServicePMSyncCompleted: Any
    __widgetQuestIDMarkedAsNew: Any
    __curPM3widgetQuests: Any
    def __init__(self):
        ...
    def isVisible(self):
        ...
    def onPrbEntitySwitched(self):
        ...
    def startListening(self):
        ...
    def stopListening(self):
        ...
    def finalize(self):
        ...
    def clearWidgetQuestIDMarkedAsNew(self):
        ...
    def setWidgetQuestIDMarkedAsNew(self, questID, doUpdateWidget=True):
        ...
    def getWidgetQuestIDMarkedAsNew(self):
        ...
    def _isQueueEnabled(self):
        ...
    def __onConfigModelUpdated(self, gpKey):
        ...
    def __onNextQuestSelected(self, event):
        ...
    def updateCurPM3widgetQuestsID(self):
        ...
    def __onPMSyncCompleted(self, *_):
        ...
