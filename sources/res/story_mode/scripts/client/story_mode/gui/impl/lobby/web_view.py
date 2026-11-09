# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/impl/lobby/web_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/impl/lobby/web_view.py
from __future__ import absolute_import
import typing
from gui.Scaleform.daapi.view.lobby.shared.web_view import WebViewTransparent
from story_mode.uilogging.story_mode.consts import LogWindows
from story_mode.uilogging.story_mode.loggers import WindowLogger

class StoryModeWebViewTransparent(WebViewTransparent):

    def __init__(self, ctx=None):
        super(StoryModeWebViewTransparent, self).__init__(ctx)
        self._uiLogger = WindowLogger(LogWindows.INFO_PAGE)

    def _populate(self):
        super(StoryModeWebViewTransparent, self)._populate()
        self._uiLogger.logOpen()

    def _dispose(self):
        self._uiLogger.logClose()
        super(StoryModeWebViewTransparent, self)._dispose()
