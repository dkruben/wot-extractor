# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/trainings/trainings_list_base.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import ArenaType as ArenaType
from adisp import adisp_process as adisp_process
from constants import PREBATTLE_MAX_OBSERVERS_IN_TEAM as PREBATTLE_MAX_OBSERVERS_IN_TEAM, OBSERVERS_BONUS_TYPES as OBSERVERS_BONUS_TYPES
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle, g_currentVehicle as g_currentVehicle
from frameworks.wulf import WindowLayer as WindowLayer
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.Scaleform.settings import ICONS_SIZES as ICONS_SIZES
from helpers import dependency as dependency
from gui.Scaleform.daapi import LobbySubView as LobbySubView
from gui.Scaleform.daapi.view.lobby.trainings.sound_constants import TRAININGS_SOUND_SPACE as TRAININGS_SOUND_SPACE
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.meta.TrainingFormMeta import TrainingFormMeta as TrainingFormMeta
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.Scaleform.framework.managers.containers import POP_UP_CRITERIA as POP_UP_CRITERIA
from gui.shared.utils.functions import getArenaFullName as getArenaFullName, getArenaImage as getArenaImage
from gui.prb_control.entities.base.legacy.listener import ILegacyListener as ILegacyListener
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from gui.prb_control.entities.base.ctx import LeavePrbAction as LeavePrbAction
from gui.sounds.ambients import LobbySubViewEnv as LobbySubViewEnv
from gui.shared import events as events
from gui.shared.event_bus import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.formatters import text_styles as text_styles
from gui.impl import backport as backport
from gui.impl.gen import R as R
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext

class TrainingsListBase(LobbySubView, TrainingFormMeta, ILegacyListener):
    __sound_env__ = LobbySubViewEnv
    _COMMON_SOUND_SPACE = TRAININGS_SOUND_SPACE
    _lobbyContext: Any
    __requester: Any
    def __init__(self, **kwargs):
        ...
    def onLeave(self):
        ...
    def onWindowMinimize(self):
        ...
    def onEscape(self):
        ...
    def onLegacyListReceived(self, prebattles):
        ...
    def sendData(self, listData, playersTotal):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _getViewData(self):
        ...
    # decorador original: @adisp_process
    def _createTrainingRoom(self, event):
        ...
    def __setViewData(self):
        ...
    # decorador original: @adisp_process
    def __doLeave(self, isExit=True):
        ...
