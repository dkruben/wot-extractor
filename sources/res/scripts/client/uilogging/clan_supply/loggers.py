# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/uilogging/clan_supply/loggers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/clan_supply/loggers.py
from __future__ import absolute_import
import json
from typing import TYPE_CHECKING
from gui.clans.clan_cache import g_clanCache
from uilogging.base.logger import MetricsLogger
from uilogging.clan_supply.constants import FEATURE, ClanSupplyLogAction
if TYPE_CHECKING:
    from uilogging.types import ItemType, ParentScreenType, InfoType

class ClanSupplyEventLogger(MetricsLogger):
    __slots__ = ('_eventParent', )

    def __init__(self):
        super(ClanSupplyEventLogger, self).__init__(FEATURE)

    def logCloseEvent(self, item, info):
        infoStr = json.dumps({'clan_id': (g_clanCache.clanDBID), 'event_trigger': (info.value)})
        self.stopAction(action=ClanSupplyLogAction.CLOSE, item=item, info=infoStr)

    def logOpenEvent(self, item, parentScreen):
        self.startAction(ClanSupplyLogAction.CLOSE)
        self.log(action=ClanSupplyLogAction.OPEN, item=item, parentScreen=parentScreen, info=json.dumps({'clan_id': (g_clanCache.clanDBID)}))
