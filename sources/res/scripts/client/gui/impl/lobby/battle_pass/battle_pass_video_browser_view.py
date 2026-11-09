# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/battle_pass/battle_pass_video_browser_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/battle_pass/battle_pass_video_browser_view.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.lobby.shared.web_view import WebView
from gui.sounds.filters import switchVideoOverlaySoundFilter

class BattlePassVideoBrowserView(WebView):

    def _populate(self):
        super(BattlePassVideoBrowserView, self)._populate()
        switchVideoOverlaySoundFilter(on=True)

    def _dispose(self):
        switchVideoOverlaySoundFilter(on=False)
        super(BattlePassVideoBrowserView, self)._dispose()
