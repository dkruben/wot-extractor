# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/customization/progressive_items_browser_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/customization/progressive_items_browser_view.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.lobby.shared.web_view import WebView
from gui.server_events.pm_constants import SOUNDS

class ProgressiveItemsBrowserView(WebView):

    def onCloseView(self):
        super(ProgressiveItemsBrowserView, self)._dispose()

    def _populate(self):
        super(ProgressiveItemsBrowserView, self)._populate()
        self.soundManager.setRTPC(SOUNDS.RTCP_OVERLAY, SOUNDS.MAX_MISSIONS_ZOOM)

    def _dispose(self):
        self.soundManager.setRTPC(SOUNDS.RTCP_OVERLAY, SOUNDS.MIN_MISSIONS_ZOOM)
        super(ProgressiveItemsBrowserView, self)._dispose()
