# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/phase_indicator.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/phase_indicator.py
from __future__ import absolute_import
from typing import Optional
from HWArenaPhasesComponent import HWArenaPhasesComponent
from halloween.gui.scaleform.daapi.view.meta.PhaseIndicatorMeta import PhaseIndicatorMeta

class HWPhaseIndicator(PhaseIndicatorMeta):

    def _populate(self):
        super(HWPhaseIndicator, self)._populate()
        HWArenaPhasesComponent.onPhaseChanged += self._update

    def _dispose(self):
        HWArenaPhasesComponent.onPhaseChanged -= self._update
        super(HWPhaseIndicator, self)._dispose()

    def _update(self, arenaPhases):
        if arenaPhases:
            self.as_setDataS(arenaPhases.activePhase, arenaPhases.phasesCount)
