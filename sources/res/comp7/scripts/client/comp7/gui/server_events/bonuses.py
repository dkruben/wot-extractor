# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/server_events/bonuses.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/server_events/bonuses.py
from __future__ import absolute_import
import logging
from comp7_common_const import COMP7_WEEKLY_QUESTS_COMPLETE_TOKEN_REGEXP
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.server_events.bonuses import TokensBonus
from gui.shared.utils.functions import makeTooltip
COMP7_TOKEN_WEEKLY_REWARD_NAME = 'comp7TokenWeeklyReward'
_logger = logging.getLogger(__name__)

class Comp7TokenWeeklyRewardBonus(TokensBonus):

    def __init__(self, name, value, isCompensation=False, ctx=None):
        super(Comp7TokenWeeklyRewardBonus, self).__init__(name, value, isCompensation, ctx)
        self._name = COMP7_TOKEN_WEEKLY_REWARD_NAME

    def isShowInGUI(self):
        return False

    def getTooltip(self):
        header = TOOLTIPS.getAwardHeader(self.getName())
        body = TOOLTIPS.getAwardBody(self.getName())
        return makeTooltip(header or None, body or None)


def isComp7WeeklyQuestToken(tID):
    return COMP7_WEEKLY_QUESTS_COMPLETE_TOKEN_REGEXP.match(tID)
