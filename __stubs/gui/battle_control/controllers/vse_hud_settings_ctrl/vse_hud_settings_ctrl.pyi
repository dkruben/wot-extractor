# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/vse_hud_settings_ctrl/vse_hud_settings_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from Event import Event as Event, EventManager as EventManager
from gui.battle_control.arena_info.interfaces import IVSEHUDSettingsController as IVSEHUDSettingsController
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.battle_control.controllers.vse_hud_settings_ctrl.settings.ally_list import AllyListClientModel as AllyListClientModel
from gui.battle_control.controllers.vse_hud_settings_ctrl.settings.battle_communication import BattleCommunicationModel as BattleCommunicationModel
from gui.battle_control.controllers.vse_hud_settings_ctrl.settings.chat import ChatModel as ChatModel
from gui.battle_control.controllers.vse_hud_settings_ctrl.settings.enemy_list import EnemyListClientModel as EnemyListClientModel
from gui.battle_control.controllers.vse_hud_settings_ctrl.settings.minimap import MinimapClientModel as MinimapClientModel
from gui.battle_control.controllers.vse_hud_settings_ctrl.settings.respawn_hud import RespawnHUDClientModel as RespawnHUDClientModel
from gui.battle_control.controllers.vse_hud_settings_ctrl.settings.countdown import CountdownClientModel as CountdownClientModel
from gui.battle_control.controllers.vse_hud_settings_ctrl.settings.primary_objective import PrimaryObjectiveClientModel as PrimaryObjectiveClientModel
from gui.battle_control.controllers.vse_hud_settings_ctrl.settings.progress_counter import ProgressCounterClientModel as ProgressCounterClientModel
from gui.battle_control.controllers.vse_hud_settings_ctrl.settings.secondary_objective import SecondaryObjectiveClientModel as SecondaryObjectiveClientModel
from pve_battle_hud import getPveHudLogger as getPveHudLogger, WidgetType as WidgetType
_logger: Any
SettingsTypes: Any
ItemSettingsTypes: Any

class VSEHUDSettingsController(IVSEHUDSettingsController):
    __slots__: tuple
    _settings: Any
    _eManager: Any
    onSettingsChanged: Any
    onItemSettingsChanged: Any
    def __init__(self):
        ...
    def getControllerID(self):
        ...
    def startControl(self, *args):
        ...
    def stopControl(self):
        ...
    def setSettings(self, settingsID, settings):
        ...
    def getSettings(self, settingsID):
        ...
    def setItemSettings(self, settingsID, itemID, settings):
        ...
    def getItemSettings(self, settingsID, itemID):
        ...
