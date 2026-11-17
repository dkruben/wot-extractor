# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/perk_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from copy import deepcopy as deepcopy
from future.utils import viewitems as viewitems
from typing import TYPE_CHECKING as TYPE_CHECKING
import BigWorld as BigWorld
import Event as Event
import BattleReplay as BattleReplay
from helpers import dependency as dependency
from PlayerEvents import g_playerEvents as g_playerEvents
from constants import ARENA_PERIOD as ARENA_PERIOD
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.battle_control.view_components import ViewComponentsController as ViewComponentsController
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from items.tankmen import getSkillsConfig as getSkillsConfig
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore, ISettingsCache as ISettingsCache
from account_helpers.settings_core import settings_constants as settings_constants
from items.components.perks_constants import PerkState as PerkState
from Vehicle import Vehicle as Vehicle
_UPDATE_FUN_PREFIX = '_updatePerk'
_DATA_KEY_PERK_ID = 'perkID'
_INTERVAL_FOR_SAME_NOTIFICATION = 6
_CREW_SETTING: Any

class PerksController(ViewComponentsController):
    sessionProvider: Any
    settingsCore: Any
    settingsCache: Any
    onPerkChanged: Any
    _prevPanelState: Any
    _prevRibbonsState: Any
    _prevArenaPeriod: Any
    __hiddenPerks: Any
    __hiddenAllPerks: Any
    def __init__(self):
        ...
    def getControllerID(self):
        ...
    def updatePerks(self, perks):
        ...
    def notifyRibbonChanges(self, ribbons):
        ...
    def startControl(self, *args):
        ...
    def stopControl(self, *args):
        ...
    def _canShowPerk(self, perkID):
        ...
    def _onVehicleControlling(self, vehicle):
        ...
    def _isInBattle(self):
        ...
    def _onArenaPeriodChange(self, period, *args):
        ...
    def _getCurrentState(self, source, prevState):
        ...
    def _updatePerk403(self, perkID, state, coolDown, lifeTime, vehicle=None):
        ...
    def __checkPerksBySettings(self, perks):
        ...
    def __checkRibbonsBySettings(self, ribbons):
        ...
    def __onSettingsSyncCompleted(self):
        ...
    def __onSettingsChanged(self, diff):
        ...
    def __updateHiddenPerks(self):
        ...
