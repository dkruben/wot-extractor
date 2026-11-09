# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/modifier_widget.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/modifier_widget.py
from __future__ import absolute_import
from HWArenaPhasesComponent import HWArenaPhasesComponent
from halloween.gui.scaleform.daapi.view.battle.fullscreen_watcher_mixin import FullscreenWatcherMixin
from halloween.gui.scaleform.daapi.view.meta.PhaseModifierMeta import PhaseModifierMeta
from typing import Optional
from gui.impl import backport
from gui.impl.gen import R

class HWModifierWidget(FullscreenWatcherMixin, PhaseModifierMeta):
    ICONS_PATH = R.images.halloween.gui.maps.icons.battleHints
    BATTLE_HINT = R.strings.halloween_battle.battleHint

    def _populate(self):
        super(HWModifierWidget, self)._populate()
        HWArenaPhasesComponent.onPhaseModifierChanged += self._update

    def _dispose(self):
        HWArenaPhasesComponent.onPhaseModifierChanged -= self._update
        super(HWModifierWidget, self)._dispose()

    def _update(self, arenaPhases):
        if not arenaPhases:
            return
        hasModifierName = bool(arenaPhases.modifierName)
        self.needToShow = hasModifierName
        self.updateVisibility()
        if hasModifierName:
            self.as_updateHintS({'phaseName': (backport.text(self.BATTLE_HINT.phase.dyn(str(arenaPhases.activePhase))())), 
               'modifierName': (backport.text(self.BATTLE_HINT.modifierName.dyn(arenaPhases.modifierName)())), 
               'modifierRule': (backport.text(self.BATTLE_HINT.modifierRule.dyn(arenaPhases.modifierName)())), 
               'modifierColor': (arenaPhases.modifierColor), 
               'iconSource': (backport.image(self.ICONS_PATH.dyn(arenaPhases.modifierName)()))})

    def _modifierChanged(self, modifierName):
        self.__modifierName = modifierName
