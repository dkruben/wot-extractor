# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_matters/battle_matters_main_reward_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.battle_matters.battle_matters_main_reward_view_model import BattleMattersMainRewardViewModel as BattleMattersMainRewardViewModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.server_events.events_dispatcher import showBattleMatters as showBattleMatters
from gui.server_events.bonuses import VehiclesBonus as VehiclesBonus
from gui.shared.event_dispatcher import showHangar as showHangar, selectVehicleInHangar as selectVehicleInHangar, showVehicleHubOverview as showVehicleHubOverview
from gui.impl.lobby.battle_matters.battle_matters_bonus_packer import BattleMattersVehiclesBonusUIPacker as BattleMattersVehiclesBonusUIPacker
from helpers import dependency as dependency
from shared_utils import findFirst as findFirst
from skeletons.gui.battle_matters import IBattleMattersController as IBattleMattersController
from skeletons.gui.server_events import IEventsCache as IEventsCache
from typing import Tuple as Tuple, Sequence as Sequence, Callable as Callable, Optional as Optional
from Event import Event as Event
_logger: Any
_BATTLEMATTERS_VEHICLES_ORDER: tuple

class BattleMattersMainRewardView(ViewImpl):
    __slots__: tuple
    __battleMattersController: Any
    __eventsCache: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def onStateChanged(self):
        ...
    def onPreview(self, vehCDDict):
        ...
    @staticmethod
    def onBack():
        ...
    @staticmethod
    def onClose():
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def __update(self):
        ...

def _vehiclesSortKey(model):
    ...
