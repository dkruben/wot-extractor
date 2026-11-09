# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/pve_base/messenger_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/pve_base/messenger_view.py
from __future__ import absolute_import
from pve_battle_hud import WidgetType
from messenger.gui.Scaleform.view.battle.messenger_view import BattleMessengerView

class PveBattleMessengerView(BattleMessengerView):

    def handleEnterPressed(self):
        settingsCtrl = self.sessionProvider.dynamic.vseHUDSettings
        if settingsCtrl is not None:
            chatSettings = settingsCtrl.getSettings(WidgetType.CHAT)
            if chatSettings is not None and chatSettings.hide:
                return
        super(PveBattleMessengerView, self).handleEnterPressed()
        return
