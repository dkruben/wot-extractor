# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/frag_correlation_bar.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
import typing as typing
from account_helpers.settings_core.settings_constants import ScorePanelStorageKeys as ScorePanelStorageKeys, GAME as GAME
from constants import ARENA_GUI_TYPE as ARENA_GUI_TYPE, IS_DEVELOPMENT as IS_DEVELOPMENT
from gui.Scaleform.daapi.view.meta.FragCorrelationBarMeta import FragCorrelationBarMeta as FragCorrelationBarMeta
from gui.battle_control.controllers.battle_field_ctrl import IBattleFieldListener as IBattleFieldListener
from gui.impl import backport as backport
from gui.shared import g_eventBus as g_eventBus, events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from helpers import dependency as dependency
from shared_utils import BitmaskHelper as BitmaskHelper
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
GuiTypeViewStateBehaviour: Any
_DEFAULT_GUI_TYPE: Any
_GUI_TYPE_VIEW_STATE_BEHAVIOUR: dict

class _FragBarViewState(BitmaskHelper):
    DEFAULT = 0
    SHOW_HP_VALUES = 1
    SHOW_HP_DIFFERENCE = 2
    SHOW_TIER_GROUPING = 4
    SHOW_VEHICLES_COUNTER = 8
    SHOW_HP_BAR = 16

class FragCorrelationBar(FragCorrelationBarMeta, IBattleFieldListener):
    sessionProvider: Any
    settingsCore: Any
    __viewSettings: Any
    def __init__(self):
        ...
    def updateVehicleHealth(self, vehicleID, newHealth, maxHealth):
        ...
    def updateDeadVehicles(self, aliveAllies, deadAllies, aliveEnemies, deadEnemies):
        ...
    def updateTeamHealth(self, alliesHP, enemiesHP, totalAlliesHP, totalEnemiesHP):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __formatValuesToUserPreferences(self, value):
        ...
    def __handleBattleLoading(self, event):
        ...
    def __initializeSettings(self):
        ...
    def __onSettingsChanged(self, diff):
        ...
    def __getArenaTypeBehaviour(self):
        ...
    def __changeSetting(self, mask, newValue, flag):
        ...
