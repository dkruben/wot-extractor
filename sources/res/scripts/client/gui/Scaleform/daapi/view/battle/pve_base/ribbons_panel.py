# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/pve_base/ribbons_panel.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/pve_base/ribbons_panel.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.battle.shared.ribbons_panel import BattleRibbonsPanel

class PveRibbonsPanel(BattleRibbonsPanel):

    def _populate(self):
        super(PveRibbonsPanel, self)._populate()
        ctrl = self.sessionProvider.shared.vehicleState
        if ctrl is not None:
            ctrl.onPostMortemSwitched += self._onPostMortemSwitched
        return

    def _dispose(self):
        ctrl = self.sessionProvider.shared.vehicleState
        if ctrl is not None:
            ctrl.onPostMortemSwitched -= self._onPostMortemSwitched
        super(PveRibbonsPanel, self)._dispose()
        return

    def _onPostMortemSwitched(self, *_):
        if not self.sessionProvider.getCtx().isPlayerObserver():
            self._ribbonsAggregator.clearRibbonsData()
            self.as_resetS()
