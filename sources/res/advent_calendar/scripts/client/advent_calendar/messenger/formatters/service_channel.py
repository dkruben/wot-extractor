# wot-extractor: codigo DESCOMPILADO de sources/res/advent_calendar/scripts/client/advent_calendar/messenger/formatters/service_channel.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: advent_calendar/scripts/client/advent_calendar/messenger/formatters/service_channel.py
from __future__ import absolute_import
from constants import LOOTBOX_TOKEN_PREFIX
from messenger import g_settings
from messenger.formatters.service_channel import LootBoxAchievesFormatter

class AdventCalendarProgressionAchievesFormatter(LootBoxAchievesFormatter):

    @classmethod
    def _processTokens(cls, data):
        result = []
        tokens = data.get('tokens', {})
        count = 0
        newTokens = {}
        for tokenID, info in tokens.items():
            if tokenID.startswith(LOOTBOX_TOKEN_PREFIX):
                count += info.get('count', 0)
            else:
                newTokens[tokenID] = info

        if count > 0:
            result.append(g_settings.htmlTemplates.format('adventLootbox', {'count': count}))
            data['tokens'] = newTokens
        parentResult = super(AdventCalendarProgressionAchievesFormatter, cls)._processTokens(data)
        if parentResult:
            result.append(parentResult)
        return cls._SEPARATOR.join(result)
