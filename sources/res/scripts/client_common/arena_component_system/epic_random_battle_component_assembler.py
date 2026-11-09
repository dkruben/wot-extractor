# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client_common/arena_component_system/epic_random_battle_component_assembler.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client_common/arena_component_system/epic_random_battle_component_assembler.py
from __future__ import absolute_import
from arena_component_system.client_arena_component_assembler import ClientArenaComponentAssembler
from arena_components.player_type_specific_components import getPlayerTypeSpecificComponentsForEpicRandom

class EpicRandomBattleComponentAssembler(ClientArenaComponentAssembler):

    @staticmethod
    def assembleComponents(componentSystem):
        ClientArenaComponentAssembler._assembleBonusCapsComponents(componentSystem)
        ClientArenaComponentAssembler._addArenaComponents(componentSystem, getPlayerTypeSpecificComponentsForEpicRandom())

    @staticmethod
    def disassembleComponents(componentSystem):
        pass
