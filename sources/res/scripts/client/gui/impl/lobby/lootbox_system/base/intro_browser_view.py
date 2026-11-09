# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/lootbox_system/base/intro_browser_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/lootbox_system/base/intro_browser_view.py
from gui.Scaleform.daapi.view.lobby.shared.web_view import WebView
from gui.sounds.filters import switchHangarOverlaySoundFilter

class LootBoxSystemIntroBrowserView(WebView):

    def _populate(self):
        super(LootBoxSystemIntroBrowserView, self)._populate()
        switchHangarOverlaySoundFilter(on=True)

    def _dispose(self):
        switchHangarOverlaySoundFilter(on=False)
        super(LootBoxSystemIntroBrowserView, self)._dispose()
