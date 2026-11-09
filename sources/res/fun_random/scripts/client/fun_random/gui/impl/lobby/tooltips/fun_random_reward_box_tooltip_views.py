# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/tooltips/fun_random_reward_box_tooltip_views.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/impl/lobby/tooltips/fun_random_reward_box_tooltip_views.py
from __future__ import absolute_import
from fun_random.gui.feature.util.fun_mixins import FunProgressionWatcher
from gui.impl.gen import R
from gui.impl.lobby.tooltips.additional_rewards_tooltip import AdditionalRewardsTooltip

class NearestAdditionalRewardsTooltip(AdditionalRewardsTooltip, FunProgressionWatcher):
    __slots__ = ()

    @classmethod
    def _getHeader(cls):
        progression = cls.getActiveProgression()
        if progression is None or cls.getActiveProgression().isInUnlimitedProgression:
            return R.strings.tooltips.quests.awards.nearest.header()
        else:
            return R.strings.fun_random.quests.limitedProgression.awards.nearest.header()

    @classmethod
    def _getHeaderCount(cls):
        progression = cls.getActiveProgression()
        if progression is None or progression.isInUnlimitedProgression:
            return 0
        return progression.activeStage.requiredCounter
