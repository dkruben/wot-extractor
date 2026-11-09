# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/arena_components/player_type_specific_components.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/arena_components/player_type_specific_components.py
from __future__ import absolute_import
from arena_components.epic_battle_player_data_component import EpicBattlePlayerDataComponent
from arena_components.player_data_component import PlayerDataComponent
from arena_components.advanced_chat_component import AdvancedChatComponent
from arena_component_system.epic_sector_warning_component import EpicSectorWarningComponent
from arena_component_system.arena_equipment_component import ArenaEquipmentComponent
from arena_component_system.overtime_component import OvertimeComponent
from gui.shared.system_factory import collectAdvancedChatComponent

def getPlayerTypeSpecificComponentsForEpicRandom():
    return {'playerDataComponent': PlayerDataComponent}


def getPlayerTypeSpecificComponentsForEpicBattle():
    return {'playerDataComponent': EpicBattlePlayerDataComponent, 
       'sectorWarningComponent': EpicSectorWarningComponent, 
       'overtimeComponent': OvertimeComponent}


def getDefaultComponents(bonusType):
    return {'arenaEquipmentComponent': ArenaEquipmentComponent, 
       'advancedChatComponent': (collectAdvancedChatComponent(bonusType) or AdvancedChatComponent)}
