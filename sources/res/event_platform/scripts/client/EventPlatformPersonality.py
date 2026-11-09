# wot-extractor: codigo DESCOMPILADO de sources/res/event_platform/scripts/client/EventPlatformPersonality.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: event_platform/scripts/client/EventPlatformPersonality.py
from __future__ import absolute_import
from debug_utils import LOG_DEBUG
from constants_utils import addArenaBonusCapsFromExtension
from event_platform_common.event_platform_constants import ARENA_BONUS_TYPE_CAPS

def preInit():
    addArenaBonusCapsFromExtension(ARENA_BONUS_TYPE_CAPS, __name__)


def init():
    LOG_DEBUG('init', __name__)


def start():
    pass


def fini():
    pass
