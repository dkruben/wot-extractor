# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/frontline_platoon_panel.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/frontline_platoon_panel.py
from __future__ import absolute_import
from frontline.gui.Scaleform.daapi.view.meta.FrontlinePlatoonPanelMeta import FrontlinePlatoonPanelMeta
from helpers import i18n
from gui.Scaleform.locale.EPIC_BATTLE import EPIC_BATTLE
_MAX_INVITES_DISPLAYED = 4

class FrontlinePlatoonPanel(FrontlinePlatoonPanelMeta):

    def _populate(self):
        super(FrontlinePlatoonPanel, self)._populate()
        self.as_setPlatoonTitleS(str(i18n.makeString(EPIC_BATTLE.SUPER_PLATOON_PANEL_TITLE)))
        self.as_setMaxDisplayedInviteMessagesS(_MAX_INVITES_DISPLAYED)

    def _handleNextMode(self, _):
        pass
