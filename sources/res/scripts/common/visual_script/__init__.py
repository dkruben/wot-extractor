# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/visual_script/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/visual_script/__init__.py
from __future__ import absolute_import
from visual_script.misc import ASPECT
from visual_script.registrar import VSBlockRegistrar
from visual_script.contexts.perks_context import PerkContext, CrewContext, PerkNotifyState
from visual_script.contexts.cgf_context import CGFGameObjectContext
from visual_script import ability_common, example, general, vehicle_blocks, qa_blocks, qa_education_blocks, balance, entity_blocks, arena_blocks, dictionary_blocks, debug_manager_blocks, cgf_blocks, commendations_common, vehicle_mechanics_blocks, command_flow
g_blockRegistrar = VSBlockRegistrar(ASPECT.CLIENT, ASPECT.SERVER)
g_blockRegistrar.regBlocksFromModule(example)
g_blockRegistrar.regTypesFromModule(example)
g_blockRegistrar.regBlocksFromModule(qa_blocks)
g_blockRegistrar.regBlocksFromModule(qa_education_blocks)
g_blockRegistrar.regBlocksFromModule(balance)
g_blockRegistrar.regTypesFromModule(balance)
g_blockRegistrar.regBlocksFromModule(general)
g_blockRegistrar.regBlocksFromModule(vehicle_blocks)
g_blockRegistrar.regBlocksFromModule(ability_common)
g_blockRegistrar.regType(ability_common.Stage)
g_blockRegistrar.regType(ability_common.EquipmentErrorState)
g_blockRegistrar.regBlocksFromModule(entity_blocks)
g_blockRegistrar.regBlock(arena_blocks.GetFlyDirection)
g_blockRegistrar.regContext(PerkContext)
g_blockRegistrar.regContext(CrewContext)
g_blockRegistrar.regType(PerkNotifyState)
g_blockRegistrar.regContext(CGFGameObjectContext)
g_blockRegistrar.regBlocksFromModule(dictionary_blocks)
g_blockRegistrar.regTypesFromModule(dictionary_blocks)
g_blockRegistrar.regBlocksFromModule(debug_manager_blocks)
g_blockRegistrar.regBlocksFromModule(cgf_blocks)
g_blockRegistrar.regTypesFromModule(commendations_common)
g_blockRegistrar.regTypesFromModule(cgf_blocks)
g_blockRegistrar.regBlocksFromModule(vehicle_mechanics_blocks)
g_blockRegistrar.regTypesFromModule(vehicle_mechanics_blocks)
g_blockRegistrar.regBlocksFromModule(command_flow)
