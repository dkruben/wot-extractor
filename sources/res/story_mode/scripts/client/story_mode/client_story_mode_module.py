# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/client_story_mode_module.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/client_story_mode_module.py
from __future__ import absolute_import
import CGF
from cgf_script.registration import registerModule
from story_mode.cgf_components.bunkers import BunkersSystem
from BunkerLogicComponent import BunkerLogicComponent

@registerModule
class ClientStoryModeModule(object):
    name = 'Client Story Mode Module'
    desc = 'Client Story Mode Functionalities'
    group = 'Store Mode'
    systems = [
     CGF.RegisterSystem(BunkersSystem, domain=CGF.Domain.Client, updateAfter=(
      CGF.TransformUpdateSystem,))]
    components = [
     BunkerLogicComponent]
