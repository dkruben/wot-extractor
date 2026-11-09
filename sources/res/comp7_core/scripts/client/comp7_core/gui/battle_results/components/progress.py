# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_core/scripts/client/comp7_core/gui/battle_results/components/progress.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_core/scripts/client/comp7_core/gui/battle_results/components/progress.py
from __future__ import absolute_import
from gui.battle_results.components.progress import BattlePassProgressBlock
from gui.impl import backport
from gui.impl.gen import R
_POST_BATTLE_RES = R.strings.battle_pass.reward.postBattle

class Comp7CoreBattlePassProgressBlock(BattlePassProgressBlock):

    @staticmethod
    def _getDescription(progress):
        if progress.pointsAux:
            text = backport.text(_POST_BATTLE_RES.progress.pointsAux())
        else:
            text = backport.text(_POST_BATTLE_RES.comp7.progress())
        return text

    @staticmethod
    def _getProgressDiffTooltip(progress, chapterID):
        return backport.text(_POST_BATTLE_RES.comp7.progress.tooltip(), points=progress.getPointsDiff(chapterID))
