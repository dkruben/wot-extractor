# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/battle/prebattle_highlights/utils.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/battle/prebattle_highlights/utils.py
from __future__ import absolute_import
from constants import ARENA_BONUS_TYPE
from gui.battle_control import avatar_getter
from gui.impl.battle.prebattle_highlights.prebattle_highlights_view import PrebattleHighlightsWindow
from gui.shared.system_factory import collectPrebattleHighlightsWindow, registerPrebattleHighlightsWindow

def getPrebattleHighlightsWindow():
    arena = avatar_getter.getArena()
    bonusType = None if not arena else arena.bonusType
    if not bonusType:
        return
    else:
        window = collectPrebattleHighlightsWindow(bonusType)
        if not window:
            return PrebattleHighlightsWindow
        return window


registerPrebattleHighlightsWindow(ARENA_BONUS_TYPE.REGULAR, PrebattleHighlightsWindow)
registerPrebattleHighlightsWindow(ARENA_BONUS_TYPE.RANDOM_NP2, PrebattleHighlightsWindow)
