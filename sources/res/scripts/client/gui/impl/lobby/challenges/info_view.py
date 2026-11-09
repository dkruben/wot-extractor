# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/challenges/info_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/challenges/info_view.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.lobby.shared.web_view import WebView
from gui.sounds.filters import switchHangarOverlaySoundFilter

class ChallengesInfoBrowserView(WebView):

    def _populate(self):
        super(ChallengesInfoBrowserView, self)._populate()
        switchHangarOverlaySoundFilter(on=True)

    def _dispose(self):
        super(ChallengesInfoBrowserView, self)._dispose()
        switchHangarOverlaySoundFilter(on=False)
