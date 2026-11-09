# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/trainings/training_room.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from constants import PREBATTLE_TYPE as PREBATTLE_TYPE
from gui.Scaleform.daapi.view.lobby.trainings.TrainingRoomBase import TrainingRoomBase as TrainingRoomBase
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.Scaleform.genConsts.MESSENGER_CHANNEL_CAROUSEL_ITEM_TYPES import MESSENGER_CHANNEL_CAROUSEL_ITEM_TYPES as MESSENGER_CHANNEL_CAROUSEL_ITEM_TYPES
from gui.Scaleform.genConsts.PREBATTLE_ALIASES import PREBATTLE_ALIASES as PREBATTLE_ALIASES
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from gui.prb_control.entities.training.legacy.ctx import TrainingSettingsCtx as TrainingSettingsCtx
from gui.prb_control.settings import PREBATTLE_ROSTER as PREBATTLE_ROSTER, REQUEST_TYPE as REQUEST_TYPE
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, g_eventBus as g_eventBus
from gui.impl.gen import R as R
from gui.shared.events import ChannelCarouselEvent as ChannelCarouselEvent
from messenger.ext import channel_num_gen as channel_num_gen
from messenger.ext.channel_num_gen import SPECIAL_CLIENT_WINDOWS as SPECIAL_CLIENT_WINDOWS

class TrainingRoom(TrainingRoomBase):
    def __init__(self, **kwargs):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _addListeners(self):
        ...
    def _removeListeners(self):
        ...
    def showTrainingSettings(self):
        ...
    def onRostersChanged(self, entity, rosters, full):
        ...
    def _handleSetPrebattleCoolDown(self, event):
        ...
    def _closeWindows(self):
        ...
    def _showRosters(self, entity, rosters):
        ...
    def _updateTrainingRoom(self, event):
        ...
    def __updateWindowOpenState(self, flag):
        ...
