# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/visual_script_client/pve_battle_hud_blocks.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from pve_battle_hud import getPveHudLogger as getPveHudLogger, WidgetType as WidgetType
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE, arrayOf as arrayOf
from visual_script.dependency import dependencyImporter as dependencyImporter
from visual_script_client.pve_common import ClientBattleHUDWidgetSettings as ClientBattleHUDWidgetSettings, PropertySlotSpec as PropertySlotSpec, SettingType as SettingType
settings: Any
_logger: Any

class SetProgressCounterSettings(ClientBattleHUDWidgetSettings):
    _SETTINGS_MODEL = settings.progress_counter.ProgressCounterClientModel
    _WIDGET_TYPE = WidgetType.PROGRESS_COUNTER
    _SETTING_TYPE = SettingType.ITEM
    _SETTINGS_CONFIG: list

class SetEnemyListSettings(ClientBattleHUDWidgetSettings):
    _SETTINGS_MODEL = settings.enemy_list.EnemyListClientModel
    _WIDGET_TYPE = WidgetType.ENEMY_LIST
    _SETTING_TYPE = SettingType.GENERAL
    _SETTINGS_CONFIG: list

class SetPrimaryObjectiveSettings(ClientBattleHUDWidgetSettings):
    _ICONS: list
    _SETTINGS_MODEL = settings.primary_objective.PrimaryObjectiveClientModel
    _WIDGET_TYPE = WidgetType.PRIMARY_OBJECTIVE
    _SETTING_TYPE = SettingType.ITEM
    _SETTINGS_CONFIG: list

class SetSecondaryObjectiveSettings(ClientBattleHUDWidgetSettings):
    _ICONS: list
    _SETTINGS_MODEL = settings.secondary_objective.SecondaryObjectiveClientModel
    _WIDGET_TYPE = WidgetType.SECONDARY_OBJECTIVE
    _SETTING_TYPE = SettingType.ITEM
    _SETTINGS_CONFIG: list

class SetAllyListSettings(ClientBattleHUDWidgetSettings):
    _SETTINGS_MODEL = settings.ally_list.AllyListClientModel
    _WIDGET_TYPE = WidgetType.ALLY_LIST
    _SETTING_TYPE = SettingType.GENERAL
    _SETTINGS_CONFIG: list

class SetMinimapSettings(ClientBattleHUDWidgetSettings):
    _SETTINGS_MODEL = settings.minimap.MinimapClientModel
    _WIDGET_TYPE = WidgetType.MINIMAP
    _SETTING_TYPE = SettingType.GENERAL
    _SETTINGS_CONFIG: list

class SetPrebattleCountdownSettings(ClientBattleHUDWidgetSettings):
    _SETTINGS_MODEL = settings.countdown.CountdownClientModel
    _WIDGET_TYPE = WidgetType.COUNTDOWN
    _SETTING_TYPE = SettingType.GENERAL
    _SETTINGS_CONFIG: list

class SetChatSettings(ClientBattleHUDWidgetSettings):
    _SETTINGS_MODEL = settings.chat.ChatModel
    _WIDGET_TYPE = WidgetType.CHAT
    _SETTING_TYPE = SettingType.GENERAL
    _SETTINGS_CONFIG: list

class SetBattleCommunicationsSettings(ClientBattleHUDWidgetSettings):
    _SETTINGS_MODEL = settings.battle_communication.BattleCommunicationModel
    _WIDGET_TYPE = WidgetType.BATTLE_COMMUNICATION
    _SETTING_TYPE = SettingType.GENERAL
    _SETTINGS_CONFIG: list

class SetRespawnHUDSetting(ClientBattleHUDWidgetSettings):
    _SETTINGS_MODEL = settings.respawn_hud.RespawnHUDClientModel
    _WIDGET_TYPE = WidgetType.RESPAWN_HUD
    _SETTING_TYPE = SettingType.GENERAL
    _SETTINGS_CONFIG: list
