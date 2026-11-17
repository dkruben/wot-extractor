# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/user_missions/hangar_widget/services/missions_service.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import Event as Event
from PlayerEvents import g_playerEvents as g_playerEvents
from config_schemas.umg_config import umgConfigSchema as umgConfigSchema
from gui.impl.lobby.user_missions.hangar_widget.services import IMissionsService as IMissionsService
from gui.impl.lobby.user_missions.hangar_widget.services.service_events import ServiceEvents as ServiceEvents
from helpers import dependency as dependency
from skeletons.gui.game_control import IHangarGuiController as IHangarGuiController

class MissionsService(IMissionsService, ServiceEvents):
    __hangarGuiCtrl: Any
    onMissionsChanged: Any
    def __init__(self):
        ...
    def onPrbEntitySwitched(self):
        ...
    def isVisible(self):
        ...
    def startListening(self):
        ...
    def stopListening(self):
        ...
    def finalize(self):
        ...
    def __onConfigModelUpdated(self, gpKey):
        ...
    def _onMissionsChangedEvent(self, *_):
        ...
