# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/maps_training/maps_training_queue_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import random as random
import BigWorld as BigWorld
from PlayerEvents import g_playerEvents as g_playerEvents
from constants import QUEUE_TYPE as QUEUE_TYPE
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.maps_training.maps_training_queue_model import MapsTrainingQueueModel as MapsTrainingQueueModel
from gui.prb_control import prbEntityProperty as prbEntityProperty
from helpers import dependency as dependency
from helpers.time_utils import getCurrentTimestamp as getCurrentTimestamp
from skeletons.gui.game_control import IMapsTrainingController as IMapsTrainingController
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.impl.lobby.maps_training.maps_training_base_view import MapsTrainingBaseView as MapsTrainingBaseView

class MapsTrainingQueueView(MapsTrainingBaseView):
    __slots__: tuple
    mapsTrainingController: Any
    itemsCache: Any
    _REQUEST_QUEUE_INFO_TIMEOUT = 5
    _TIPS_OF_ALL = 21
    _QUEUE_INFO_PARAMS_COUNT = 2
    _WAIT_TIME_AVG = 15
    _WAIT_TIME_LONG = 180
    __timerCallback: Any
    __queueCallback: Any
    __createTime: Any
    __tipNum: Any
    __status: Any
    def __init__(self, *args, **kwargs):
        ...
    # decorador original: @prbEntityProperty
    def prbEntity(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _addListeners(self):
        ...
    def _removeListeners(self):
        ...
    def __requestQueueInfo(self):
        ...
    def __updateTimer(self):
        ...
    def __onArenaCreated(self):
        ...
    def __stopUpdateScreen(self):
        ...
    def __onQuitButtonClick(self):
        ...
    @staticmethod
    def __onMenu():
        ...
    def __onShowPrevTipClick(self):
        ...
    def __onShowNextTipClick(self):
        ...
