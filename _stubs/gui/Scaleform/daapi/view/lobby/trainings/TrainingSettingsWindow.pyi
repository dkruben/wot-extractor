# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/trainings/TrainingSettingsWindow.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
import ArenaType as ArenaType
from account_helpers import gameplay_ctx as gameplay_ctx
from constants import PREBATTLE_TYPE as PREBATTLE_TYPE, Configs as Configs
from debug_utils import LOG_ERROR as LOG_ERROR, LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from gui.Scaleform.daapi.view.meta.TrainingWindowMeta import TrainingWindowMeta as TrainingWindowMeta
from gui.prb_control import prbEntityProperty as prbEntityProperty
from gui.prb_control.prb_getters import getTrainingBattleRoundLimits as getTrainingBattleRoundLimits
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.utils.functions import getArenaImage as getArenaImage
from helpers import dependency as dependency
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.training_room_external_handlers import getAllTrainingRoomHandlers as getAllTrainingRoomHandlers, getTrainingRoomHandler as getTrainingRoomHandler
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
CONFIG_KEYS_FOR_UPDATE: set

class ArenasCache(object):
    __lobbyCtx: Any
    __cache: Any
    __isEpic: Any
    __settings: Any
    def __init__(self, ctx, settings):
        ...
    def fini(self):
        ...
    @property
    def cache(self):
        ...
    def build(self):
        ...
    def __getArenaTypeName(self, arena):
        ...
    def __isArenaSuitableForTraining(self, arena):
        ...
    def __getHandlerForArenaTypeName(self, arenaTypeName):
        ...

class TrainingSettingsWindow(TrainingWindowMeta):
    itemsCache: Any
    __lobbyContext: Any
    __isCreateRequest: Any
    __settings: Any
    __isEpic: Any
    __arenasCache: Any
    def __init__(self, ctx=None):
        ...
    # decorador original: @prbEntityProperty
    def prbEntity(self):
        ...
    def onWindowClose(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def getInfo(self):
        ...
    def updateTrainingRoom(self, key, time, isPrivate, description):
        ...
    def __updateVO(self):
        ...
    def __onServerSettingsChange(self, diff):
        ...
    def __isDescriptionEnabled(self):
        ...
