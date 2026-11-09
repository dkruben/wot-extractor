# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_core/scripts/client/comp7_core/gui/Scaleform/daapi/view/battle/full_stats.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_core/scripts/client/comp7_core/gui/Scaleform/daapi/view/battle/full_stats.py
from __future__ import absolute_import
from comp7_core.gui.Scaleform.daapi.view.battle.comp7_voip_helper import Comp7VoipHelper, VoiceChatControlTextStyles
from comp7_core.gui.Scaleform.daapi.view.meta.Comp7FullStatsMeta import Comp7FullStatsMeta

class FullStatsComponent(Comp7FullStatsMeta):

    def __init__(self):
        super(FullStatsComponent, self).__init__()
        self.__voipHelper = Comp7VoipHelper(component=self, textStyle=VoiceChatControlTextStyles.FULL_STATS)

    def onVoiceChatControlClick(self):
        self.__voipHelper.onVoiceChatControlClick()

    def _populate(self):
        super(FullStatsComponent, self)._populate()
        self.__voipHelper.populate()
        self.__voipHelper.enable(enable=True)

    def _dispose(self):
        self.__voipHelper.dispose()
        super(FullStatsComponent, self)._dispose()

    @staticmethod
    def _buildTabs(builder):
        builder.addStatisticsTab()
        builder.addBoostersTab()
        return builder.getTabs()
