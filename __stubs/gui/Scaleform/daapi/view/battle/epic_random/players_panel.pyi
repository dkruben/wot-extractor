# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/epic_random/players_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers.settings_core.settings_constants import GAME as GAME
from gui.Scaleform.daapi.view.meta.EpicRandomPlayersPanelMeta import EpicRandomPlayersPanelMeta as EpicRandomPlayersPanelMeta
from gui.Scaleform.genConsts.PLAYERS_PANEL_STATE import PLAYERS_PANEL_STATE as PLAYERS_PANEL_STATE
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_EPIC_RANDOM_PLAYERS_PANEL_STATE_RANGE: tuple
_EPIC_RANDOM_PLAYERS_PANEL_MULTI_COLUMN_STATE_RANGE: tuple
_EPIC_RANDOM_MULTI_COLUMN_TO_STATE: dict
_EPIC_RANDOM_BUTTON_STATE_TO_MODE: dict

class EpicPlayerPanelStateSetting(object):
    settingsCore: Any
    @classmethod
    def read(cls):
        ...
    @classmethod
    def write(cls, state):
        ...

class EpicRandomPlayersPanel(EpicRandomPlayersPanelMeta):
    guiSessionProvider: Any
    _mode: Any
    __focusedColumn: Any
    def __init__(self):
        ...
    def _dispose(self):
        ...
    def focusedColumnChanged(self, value):
        ...
    def tryToSetPanelModeByMouse(self, panelMode):
        ...
    def setInitialMode(self):
        ...
    def setLargeMode(self):
        ...
    def _handleNextMode(self, _):
        ...
    def __onPostMortemSwitched(self, noRespawnPossible, respawnAvailable):
        ...
    def __onRespawnBaseMoving(self):
        ...
