# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/messenger/formatters/battle_results_formatters.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/messenger/formatters/battle_results_formatters.py
from __future__ import absolute_import
from adisp import adisp_async, adisp_process
from fun_random.gui.shared.fun_system_factory import collectBattleResultsMessageSubFormatter
from messenger.formatters.service_channel import WaitItemsSyncFormatter, BattleResultsFormatter
from messenger.formatters.service_channel_helpers import MessageData

class FunBattleResultsFormatter(WaitItemsSyncFormatter):

    @adisp_async
    @adisp_process
    def format(self, message, callback):
        isSynced = yield self._waitForSyncItems()
        if message.data and isSynced:
            battleResults = message.data
            arenaGuiType = battleResults.get('guiType')
            subFormatterCls = collectBattleResultsMessageSubFormatter(arenaGuiType)
            if subFormatterCls is not None:
                messages = yield subFormatterCls().format(message)
                callback(messages)
            else:
                callback([MessageData(None, None)])
        else:
            callback([MessageData(None, None)])
        return


class FunRandomBattleResultsSubFormatter(BattleResultsFormatter):
    pass
