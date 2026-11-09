# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/messenger/formatters/service_channel.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/messenger/formatters/service_channel.py
from __future__ import absolute_import
import ArenaType
from fort_rush_common.fort_rush_constants import EventStates
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import text_styles
from gui.shared.money import Currency
from messenger import g_settings
from messenger.formatters.service_channel import BattleResultsFormatter, ServiceChannelFormatter
from messenger.formatters.service_channel_helpers import MessageData

class FortRushBattleResultsFormatter(BattleResultsFormatter):
    _battleResultKeys = {(-1): 'FortRushBattleDefeatResult', 
       0: 'FortRushBattleDrawResult', 
       1: 'FortRushBattleVictoryResult'}

    def _prepareFormatData(self, message):
        templateName, ctx = super(FortRushBattleResultsFormatter, self)._prepareFormatData(message)
        battleResults = message.data
        accessor = R.strings.arenas.num(ArenaType.g_cache[battleResults.get('arenaTypeID', 0)].geometryName)
        ctx['mapName'] = backport.text(accessor.name())
        ctx['vehicles'] = ctx.get('vehicleNames', '')
        ctx[Currency.CREDITS] = text_styles.credits(backport.getIntegralFormat(battleResults.get(Currency.CREDITS, 0)))
        progressionPoints = sum(data.get('count', 0) for data in battleResults.get('tokens', {}).values() if isinstance(data, dict))
        ctx['progressionPoints'] = backport.getIntegralFormat(progressionPoints) if progressionPoints else ''
        return (
         templateName, ctx)


class FortRushEventStatesFormatter(ServiceChannelFormatter):
    __TEMPLATES = {(EventStates.START): 'FortRushEventStateStart', 
       (EventStates.PAUSE): 'FortRushEventStatePause', 
       (EventStates.RESUME): 'FortRushEventStateResume', 
       (EventStates.ENDED): 'FortRushEventStateEnded'}

    def format(self, message, *args):
        template = self.__TEMPLATES.get(message.get('state'))
        formatted = g_settings.msgTemplates.format(template)
        return [MessageData(formatted, self._getGuiSettings(message, template))]
