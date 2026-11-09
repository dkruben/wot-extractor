# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/battle/phase_indicator.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/battle/phase_indicator.py
from __future__ import absolute_import
from typing import Optional
from LSArenaPhasesComponent import LSArenaPhasesComponent
from gui.impl import backport
from last_stand.gui.scaleform.daapi.view.meta.PhaseIndicatorMeta import PhaseIndicatorMeta
from helpers import dependency
from gui.impl.gen import R
from skeletons.gui.battle_session import IBattleSessionProvider
_R_INDICATOR = R.strings.last_stand_battle.arena
_PHASE = 'phase'
_WAVE = 'wave'

class LSPhaseIndicator(PhaseIndicatorMeta):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def _populate(self):
        super(LSPhaseIndicator, self)._populate()
        LSArenaPhasesComponent.onPhaseChanged += self._update

    def _dispose(self):
        LSArenaPhasesComponent.onPhaseChanged -= self._update
        super(LSPhaseIndicator, self)._dispose()

    def _update(self, arenaPhases):
        if not arenaPhases:
            return
        self.__updateProgressInfo(arenaPhases.activePhase, arenaPhases.phasesCount)

    def __updateProgressInfo(self, activePhase, phasesCount):
        progressInfo = backport.text(_R_INDICATOR.dyn(_WAVE)(), current=activePhase, total=phasesCount)
        self.as_setDataS(progressInfo)
