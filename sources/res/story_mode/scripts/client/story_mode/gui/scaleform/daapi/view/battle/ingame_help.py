# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/battle/ingame_help.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/battle/ingame_help.py
from __future__ import absolute_import
import typing
from gui.Scaleform.daapi.view.battle.shared.ingame_help import IngameHelpWindow
from story_mode.uilogging.story_mode.consts import LogWindows
from story_mode.uilogging.story_mode.loggers import WindowLogger

class StoryModeIngameHelpWindow(IngameHelpWindow):

    def __init__(self, ctx=None):
        super(StoryModeIngameHelpWindow, self).__init__(ctx)
        self._uiLogger = WindowLogger(LogWindows.HELP)

    def _populate(self):
        self._uiLogger.logOpen()
        super(StoryModeIngameHelpWindow, self)._populate()

    def _dispose(self):
        super(StoryModeIngameHelpWindow, self)._dispose()
        self._uiLogger.logClose()
