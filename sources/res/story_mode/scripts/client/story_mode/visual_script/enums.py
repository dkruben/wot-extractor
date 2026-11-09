# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/visual_script/enums.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/visual_script/enums.py
from __future__ import absolute_import
import typing
from visual_script.type import VScriptEnum
from visual_script import ASPECT
from story_mode_common.story_mode_constants import AwarenessState

class SMAwarenessStateEnum(VScriptEnum):

    @classmethod
    def slotType(cls):
        return 'ESMAwarenessStateEnum'

    @classmethod
    def vs_enum(cls):
        return AwarenessState

    @classmethod
    def vs_aspects(cls):
        return [
         ASPECT.CLIENT]
