# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/modifier_hint.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/modifier_hint.py
from __future__ import absolute_import
from gui.impl import backport
from halloween.gui.scaleform.daapi.view.battle.battle_hint import BattleHint
from halloween.gui.scaleform.daapi.view.meta.BattleHintModifierMeta import BattleHintModifierMeta
from gui.impl.gen import R
from halloween.gui.sounds import playSound
from halloween.gui.sounds.sound_constants import PhaseModifierSounds

class HWPhaseModifierHint(BattleHint, BattleHintModifierMeta):
    ICONS_PATH = R.images.halloween.gui.maps.icons.battleHints
    BATTLE_HINT = R.strings.halloween_battle.battleHint

    def _showHint(self, model, params):
        vo = model.createVO(params)
        if vo:
            phaseName = params['phaseName']
            modifierName = params['modifierName']
            modifierColor = params['modifierColor']
            self.as_showHintS(vo)
            self.as_updateHintS({'phaseName': (backport.text(self.BATTLE_HINT.phase.num(phaseName)())), 
               'modifierName': (backport.text(self.BATTLE_HINT.modifierName.dyn(modifierName)())), 
               'modifierRule': (backport.text(self.BATTLE_HINT.modifierRule.dyn(modifierName)())), 
               'modifierColor': modifierColor, 
               'iconSource': (backport.image(self.ICONS_PATH.dyn(modifierName)()))})
            playSound(PhaseModifierSounds.START.get(modifierName))
