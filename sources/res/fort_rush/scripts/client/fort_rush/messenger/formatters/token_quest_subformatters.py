# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/messenger/formatters/token_quest_subformatters.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/messenger/formatters/token_quest_subformatters.py
from __future__ import absolute_import
from fort_rush.helpers.utils import isFREventProgressionQuest
from messenger.formatters.service_channel_helpers import MessageData
from messenger.formatters.token_quest_subformatters import SyncTokenQuestsSubFormatter

class FortRushProgressionQuestFormatter(SyncTokenQuestsSubFormatter):

    def format(self, message, *args):
        return [
         MessageData(None, None)]

    @classmethod
    def _isQuestOfThisGroup(cls, questID):
        return isFREventProgressionQuest(questID)
