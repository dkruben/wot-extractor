# wot-extractor: codigo DESCOMPILADO de sources/res/server_side_replay/scripts/client/ServerSideReplayPersonality.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: server_side_replay/scripts/client/ServerSideReplayPersonality.py
from __future__ import absolute_import
from debug_utils import LOG_DEBUG
from server_side_replay.gui.Scaleform import registerMainMenuEntries

def preInit():
    registerMainMenuEntries()


def init():
    LOG_DEBUG('init', __name__)


def start():
    pass


def fini():
    pass
