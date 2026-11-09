# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/prebattle_highlights/sub_systems/pbh_sequence_handler.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import iteritems as iteritems
import CGF as CGF
import logging as logging
import typing as typing
from collections import OrderedDict as OrderedDict
from GenericComponents import Sequence as Sequence
from cgf_modules.sequence_events import sequenceSubscribe as sequenceSubscribe
from constants import PREBATTLE_SEQUENCE_EVENT_NAMES as PREBATTLE_SEQUENCE_EVENT_NAMES
from gui.battle_control.avatar_getter import getSpaceID as getSpaceID
from gui.battle_control.controllers.prebattle_highlights.pbh_helpers import getPbhPrefabGo as getPbhPrefabGo, timeUntilEndOfPeriod as timeUntilEndOfPeriod
from gui.battle_control.controllers.prebattle_highlights.sub_systems.base_sub_system import BasePbhSubSystem as BasePbhSubSystem
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import PrebattleEvent as PrebattleEvent, PetSystemEvent as PetSystemEvent
from pet_system_common.pet_constants import PetTrigger as PetTrigger
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from typing import Optional as Optional, Callable as Callable, Tuple as Tuple
from Event import Event as Event
_logger: Any
EXCLUDED_LAYERS: tuple
EMPTY_SEQUENCE_LAYER_VALUE: tuple

class PbhSequenceHandler(BasePbhSubSystem):
    __lobbyContext: Any
    __sessionProvider: Any
    __stopCallback: Any
    __onStartPbhStageEvent: Any
    __sequenceLayer: Any
    def __init__(self, readyCallback, stopCallback, onStartPbhStageEvent):
        ...
    def subscribe(self):
        ...
    def unsubscribe(self):
        ...
    def isReady(self):
        ...
    def prepareSequences(self, go, layer):
        ...
    def startFlow(self):
        ...
    def stopFlow(self):
        ...
    def clear(self):
        ...
    def getSequenceData(self):
        ...
    def getSequenceLayerInfo(self):
        ...
    @staticmethod
    def __handleAnimationEvent():
        ...
    def __handleStartPbhStageEvent(self):
        ...
    def __handlePbhEndsEvent(self):
        ...
    def __handlePbhPetHighlightAnim(self):
        ...
