# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/lobby/hangar/halloween_browser.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/scaleform/daapi/view/lobby/hangar/halloween_browser.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.lobby.shared.web_view import WebViewTransparent
from halloween.gui.sounds import playSound
from halloween.gui.sounds.sound_constants import ABOUT_GAME_MODE_ENTER, ABOUT_GAME_MODE_EXIT
from halloween.uilogging.loggers import HWMetricsLogger
from halloween.uilogging.logging_constants import HWLogKeys, HWLogActions

class HalloweenBrowser(WebViewTransparent):

    def __init__(self, ctx=None):
        super(HalloweenBrowser, self).__init__(ctx)
        playSound(ABOUT_GAME_MODE_ENTER)
        self.__uiLogger = HWMetricsLogger(HWLogKeys.HW_WEB_VIEW)

    def _populate(self):
        super(HalloweenBrowser, self)._populate()
        self.__uiLogger.onStartView(HWLogActions.LIFETIME)

    def _dispose(self):
        playSound(ABOUT_GAME_MODE_EXIT)
        self.__uiLogger.onStopView(HWLogActions.LIFETIME, self._url)
        super(HalloweenBrowser, self)._dispose()
