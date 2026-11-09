# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/veh_post_progression/post_progression_intro.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/veh_post_progression/post_progression_intro.py
from __future__ import absolute_import
import typing
from account_helpers.settings_core.ServerSettingsManager import UI_STORAGE_KEYS
from gui.impl.gen import R
from gui.impl.lobby.common.info_view import getInfoWindowProc
if typing.TYPE_CHECKING:
    from gui.impl.lobby.common.info_view import IInfoWindowProcessor

def getPostProgressionIntroWindowProc():
    return getInfoWindowProc(R.views.lobby.veh_post_progression.PostProgressionIntro(), uiStorageKey=UI_STORAGE_KEYS.POST_PROGRESSION_INTRO_SHOWN)


def getPostProgressionInfoWindowProc():
    return getInfoWindowProc(R.views.lobby.veh_post_progression.PostProgressionInfo())
