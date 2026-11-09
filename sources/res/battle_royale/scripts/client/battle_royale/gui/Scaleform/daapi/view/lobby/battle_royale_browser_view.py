# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/lobby/battle_royale_browser_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/lobby/battle_royale_browser_view.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.lobby.shared.web_view import WebView
from helpers import dependency
from skeletons.gui.game_control import IBattleRoyaleController
from web.web_client_api.battle_royale import createBattleRoyaleWebHanlders

class BattleRoyaleBrowserView(WebView):
    __battleRoyaleController = dependency.descriptor(IBattleRoyaleController)

    def webHandlers(self):
        return createBattleRoyaleWebHanlders()

    def _populate(self):
        super(BattleRoyaleBrowserView, self)._populate()
        self.__battleRoyaleController.onUpdated += self.__onSettingsChange

    def _dispose(self):
        super(BattleRoyaleBrowserView, self)._dispose()
        self.__battleRoyaleController.onUpdated -= self.__onSettingsChange

    def __onSettingsChange(self, diff):
        if not self.__battleRoyaleController.isEnabled():
            self.destroy()
