# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/user_missions/tooltips/challenges_shields_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/user_missions/tooltips/challenges_shields_tooltip.py
from __future__ import absolute_import
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.user_missions.tooltips.challenges_shields_tooltip_model import ChallengesShieldsTooltipModel
from gui.impl.pub import ViewImpl

class ChallengesShieldsTooltip(ViewImpl):

    def __init__(self):
        settings = ViewSettings(R.views.mono.user_missions.tooltips.challenges_shields_tooltip())
        settings.model = ChallengesShieldsTooltipModel()
        super(ChallengesShieldsTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(ChallengesShieldsTooltip, self).getViewModel()
