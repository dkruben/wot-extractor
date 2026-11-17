# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/trainings/Trainings.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from adisp import adisp_process as adisp_process
from constants import PREBATTLE_TYPE as PREBATTLE_TYPE
from frameworks.wulf import WindowLayer as WindowLayer
from gui.Scaleform.daapi.view.lobby.trainings.trainings_list_base import TrainingsListBase as TrainingsListBase
from gui.Scaleform.framework.managers.containers import POP_UP_CRITERIA as POP_UP_CRITERIA
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.Scaleform.genConsts.BATTLE_TYPES import BATTLE_TYPES as BATTLE_TYPES
from gui.Scaleform.genConsts.MESSENGER_CHANNEL_CAROUSEL_ITEM_TYPES import MESSENGER_CHANNEL_CAROUSEL_ITEM_TYPES as MESSENGER_CHANNEL_CAROUSEL_ITEM_TYPES
from gui.Scaleform.genConsts.PREBATTLE_ALIASES import PREBATTLE_ALIASES as PREBATTLE_ALIASES
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from gui.prb_control.entities.training.legacy.ctx import JoinTrainingCtx as JoinTrainingCtx
from gui.prb_control.entities.training.legacy.ctx import TrainingSettingsCtx as TrainingSettingsCtx
from gui.shared import events as events, g_eventBus as g_eventBus
from gui.shared.event_bus import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.events import ChannelCarouselEvent as ChannelCarouselEvent
from messenger.ext import channel_num_gen as channel_num_gen
from messenger.ext.channel_num_gen import SPECIAL_CLIENT_WINDOWS as SPECIAL_CLIENT_WINDOWS

class Trainings(TrainingsListBase):
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _getViewData(self):
        ...
    # decorador original: @adisp_process
    def joinTrainingRequest(self, prbID, prbClusterID):
        ...
    def createTrainingRequest(self):
        ...
    def __updateWindowOpenState(self, flag):
        ...
