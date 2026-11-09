# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/visual_script/commendations_common.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/visual_script/commendations_common.py
from __future__ import absolute_import
import typing
from live_tags_constants import LIVE_TAG_TYPES
from visual_script.type import VScriptEnum

class LiveTagTypes(VScriptEnum):

    @classmethod
    def vs_name(cls):
        return 'LiveTagTypesT'

    @classmethod
    def vs_enum(cls):
        return LIVE_TAG_TYPES
