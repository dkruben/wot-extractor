# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/pve_base/damage_log_panel.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/pve_base/damage_log_panel.py
from __future__ import absolute_import
from account_helpers.settings_core.settings_constants import GRAPHICS
from gui.Scaleform.daapi.view.battle.shared.damage_log_panel import DamageLogPanel

class PveDamageLogPanel(DamageLogPanel):

    def _invalidatePanelVisibility(self):
        if self._isFullStatsShown or self._isWinnerScreenShown:
            return
        if not self._isVisible:
            self._isVisible = True
            self._setSettings(self._isVisible, bool(self.settingsCore.getSetting(GRAPHICS.COLOR_BLIND)))
