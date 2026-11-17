# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/hint_panel/dyn_squad_hint_plugin.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from typing import TYPE_CHECKING as TYPE_CHECKING
import CommandMapping as CommandMapping
from constants import ARENA_PERIOD as ARENA_PERIOD, ARENA_GUI_TYPE as ARENA_GUI_TYPE
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import DYN_SQUAD_HINT_SECTION as DYN_SQUAD_HINT_SECTION
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.Scaleform.daapi.view.battle.shared.hint_panel.hint_panel_plugin import HintPanelPlugin as HintPanelPlugin, HintData as HintData, HintPriority as HintPriority
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import GameEvent as GameEvent
from gui.shared.utils.key_mapping import getReadableKey as getReadableKey, getVirtualKey as getVirtualKey
from helpers import dependency as dependency
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
import VOIP as VOIP
from gui.Scaleform.daapi.view.battle.shared.hint_panel.component import BattleHintPanel as BattleHintPanel
from typing import Type as TType, Any as TAny
_logger: Any

class DynSquadHintPlugin(HintPanelPlugin):
    sessionProvider: Any
    _HINT_DAY_COOLDOWN = 30
    _HINT_BATTLES_COOLDOWN = 10
    _HINT_TIMEOUT = 6
    __shouldShowHint: Any
    __isHintShown: Any
    __isDestroyTimerDisplaying: Any
    __isObserver: Any
    __settings: Any
    __wasDisplayed: Any
    __callbackDelayer: Any
    _isInRecovery: Any
    _isUnderFire: Any
    _isInProgressCircle: Any
    __isInDisplayPeriod: Any
    def __init__(self, parentObj):
        ...
    @classmethod
    def isSuitable(cls):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def show(self):
        ...
    def hide(self):
        ...
    def setPeriod(self, period):
        ...
    def updateMapping(self):
        ...
    def _getHint(self):
        ...
    def __onToggleVoipChannel(self, *args, **kwargs):
        ...
    def __canShowHint(self):
        ...
    def __addHint(self):
        ...
    def __removeHint(self):
        ...
    def __onHintTimeOut(self):
        ...
    def __updateHint(self):
        ...
    def __onDynSquadCreatedOrJoined(self, isCreator, squadID):
        ...
    def __onVehicleStateUpdated(self, state, value):
        ...
    def __areOtherIndicatorsShown(self):
        ...
