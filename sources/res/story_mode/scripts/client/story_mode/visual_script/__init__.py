# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/visual_script/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/visual_script/__init__.py
from __future__ import absolute_import
from constants import IS_UE_EDITOR
from visual_script.misc import ASPECT
from visual_script.registrar import VSBlockRegistrar
g_blockRegistrar = VSBlockRegistrar(ASPECT.CLIENT, ASPECT.HANGAR)

def registerForGeneral():
    from story_mode.visual_script import voiceover_blocks, ui_blocks, arena_blocks, vehicle_blocks, enums
    g_blockRegistrar.regBlocksFromModule(voiceover_blocks)
    g_blockRegistrar.regBlocksFromModule(ui_blocks)
    g_blockRegistrar.regBlocksFromModule(arena_blocks)
    g_blockRegistrar.regBlocksFromModule(vehicle_blocks)
    g_blockRegistrar.regTypesFromModule(enums)


if not IS_UE_EDITOR:
    registerForGeneral()
