# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/classic/players_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers.settings_core.options import VehicleHPInPlayersPanelSetting as VehicleHPInPlayersPanelSetting
from account_helpers.settings_core.settings_constants import GAME as GAME
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.Scaleform.daapi.view.battle.shared.formatters import normalizeHealthPercent as normalizeHealthPercent
from gui.Scaleform.daapi.view.meta.PlayersPanelMeta import PlayersPanelMeta as PlayersPanelMeta
from gui.Scaleform.genConsts.PLAYERS_PANEL_STATE import PLAYERS_PANEL_STATE as PLAYERS_PANEL_STATE
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control.controllers.battle_field_ctrl import IBattleFieldListener as IBattleFieldListener
from gui.battle_control.controllers.period_ctrl import IAbstractPeriodView as IAbstractPeriodView
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore, IBattleCommunicationsSettings as IBattleCommunicationsSettings
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_PLAYERS_PANEL_STATE_RANGE: tuple
PLAYER_PANEL_SETTINGS_TO_HP_STATE: dict

class PlayerPanelStateSetting(object):
    settingsCore: Any
    @classmethod
    def read(cls):
        ...
    @classmethod
    def write(cls, state):
        ...

class PlayersPanel(IBattleFieldListener, PlayersPanelMeta, IAbstractPeriodView):
    guiSessionProvider: Any
    settingsCore: Any
    battleCommunications: Any
    _mode: Any
    def __init__(self):
        ...
    def updateVehicleHealth(self, vehicleID, newHealth, maxHealth):
        ...
    def tryToSetPanelModeByMouse(self, panelMode):
        ...
    def switchToOtherPlayer(self, vehicleID):
        ...
    def setInitialMode(self):
        ...
    def setLargeMode(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _handleNextMode(self, _):
        ...
    def __setMode(self, mode):
        ...
    def _handleShowExtendedInfo(self, event):
        ...
    def __onSettingsChanged(self, diff):
        ...
    def __onBattleCommunicationSettingsChanged(self):
        ...

def convertSettingToFeatures(value):
    ...
