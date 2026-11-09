# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/maps_training/battle_goals.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BigWorld as BigWorld
from constants import ARENA_PERIOD as ARENA_PERIOD
from hints.battle.schemas.maps_training import HintType as HintType
from gui.battle_control.arena_info.interfaces import IArenaVehiclesController as IArenaVehiclesController
from gui.battle_control.controllers.battle_hints.queues import BattleHintQueueParams as BattleHintQueueParams
from gui.Scaleform.daapi.view.meta.MapsTrainingGoalsMeta import MapsTrainingGoalsMeta as MapsTrainingGoalsMeta
from gui.battle_control.controllers.battle_hints.controller import BattleHintComponent as BattleHintComponent
from helpers import dependency as dependency, isPlayerAvatar as isPlayerAvatar
from PlayerEvents import g_playerEvents as g_playerEvents
from items import vehicles as vehicles
from maps_training_common.maps_training_constants import VEHICLE_CLASSES_ORDER as VEHICLE_CLASSES_ORDER
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from items.vehicles import VEHICLE_CLASS_TAGS as VEHICLE_CLASS_TAGS
from skeletons.gui.game_control import IMapsTrainingController as IMapsTrainingController
from vehicle_systems.stricted_loading import makeCallbackWeak as makeCallbackWeak
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from account_helpers.settings_core.settings_constants import OnceOnlyHints as OnceOnlyHints
import ArenaType as ArenaType
from hints.battle.schemas.maps_training import MTClientHintModel as MTClientHintModel

class MapsTrainingBattleGoals(BattleHintComponent, MapsTrainingGoalsMeta, IArenaVehiclesController):
    sessionProvider: Any
    mapsTrainingController: Any
    settingsCore: Any
    goalsByType: Any
    _loaded: Any
    def __init__(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __onRoundFinished(self, *args):
        ...
    def _setGoals(self):
        ...
    def _showHint(self, model, params):
        ...
    def _hideHint(self):
        ...
    def _destroyGoal(self, vehType):
        ...
    def _onArenaPeriodChange(self, period, *args):
        ...
