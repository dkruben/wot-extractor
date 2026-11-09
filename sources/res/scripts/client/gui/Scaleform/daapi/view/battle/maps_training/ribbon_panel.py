# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/maps_training/ribbon_panel.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/maps_training/ribbon_panel.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.battle.shared.ribbons_panel import BattleRibbonsPanel
from gui.Scaleform.genConsts.BATTLE_EFFICIENCY_TYPES import BATTLE_EFFICIENCY_TYPES as _BET
_PROHIB_BATTLE_EFFICIENCY_TYPES = (
 _BET.CAPTURE, _BET.DEFENCE, _BET.BASE_CAPTURE_BLOCKED)

class MapsTrainingRibbonPanel(BattleRibbonsPanel):

    def _shouldShowRibbon(self, ribbon):
        if ribbon.getType() in _PROHIB_BATTLE_EFFICIENCY_TYPES:
            return False
        return super(MapsTrainingRibbonPanel, self)._shouldShowRibbon(ribbon)
