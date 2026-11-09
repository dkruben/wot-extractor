# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/clans/cache_providers/missions_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from adisp import adisp_process as adisp_process
from gui import DialogsInterface as DialogsInterface
from gui.Scaleform.genConsts.QUESTS_ALIASES import QUESTS_ALIASES as QUESTS_ALIASES
from gui.clans.cache_providers.base_provider import IBaseProvider as IBaseProvider
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.shared import g_eventBus as g_eventBus, events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.personality import ServicesLocator as ServicesLocator
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
TIME_TO_UPDATE_HANGAR_FLAG = 60

class ClientMissionsProvider(IBaseProvider, IGlobalListener):
    lobbyContext: Any
    __formActive: Any
    __elenActive: Any
    __elenFlagTimerID: Any
    __elenTimerID: Any
    def __init__(self):
        ...
    def start(self):
        ...
    def stop(self, withClear=False):
        ...
    def __onServerSettingChanged(self, diff):
        ...
    # decorador original: @adisp_process
    def __showElenPopupDlg(self):
        ...
    def __onMissionsActivate(self, _):
        ...
    def __onMissionsDeactivate(self, _):
        ...
    def __onMissionsTabChanged(self, event):
        ...
    def __startEventboardsTimer(self):
        ...
    def __stopEventboardsTimer(self):
        ...
    def __updateEventboardsTimer(self):
        ...
    def __updateEventboardsFlagTimer(self):
        ...
    # decorador original: @adisp_process
    def __requestEventboardsData(self):
        ...
