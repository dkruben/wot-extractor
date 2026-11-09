# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_control/controllers/vse_hud_settings_ctrl/settings/countdown.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/vse_hud_settings_ctrl/settings/countdown.py
from __future__ import absolute_import
from gui.battle_control.controllers.vse_hud_settings_ctrl.settings.base_models import TextClientModel

class CountdownClientModel(TextClientModel):
    __slots__ = ('header', 'subheader', 'battleStartMessage')

    def __init__(self, header, subheader, battleStartMessage):
        super(CountdownClientModel, self).__init__()
        self.header = header
        self.subheader = subheader
        self.battleStartMessage = battleStartMessage

    def getHeader(self):
        return self._getText(self.header)

    def getSubheader(self):
        return self._getText(self.subheader)

    def getBattleStartMessage(self):
        return self._getText(self.battleStartMessage)

    def __repr__(self):
        return '<CountdownClientModel>: header=%s, subheader=%s, battleStartMessage=%s' % (
         self.header, self.subheader, self.battleStartMessage)
