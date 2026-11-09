# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/skeletons/ls_quests_ui_cache.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/skeletons/ls_quests_ui_cache.py
from __future__ import absolute_import
import typing
from skeletons.gui.game_control import IGameController
if typing.TYPE_CHECKING:
    from Event import Event
    from gui.server_events.event_items import Quest
    from typing import Optional, Dict, Callable

class ILSQuestsUICache(IGameController):
    onCacheUpdated = None
    onSyncCompleted = None

    def getQuests(self, filterFunc=None):
        raise NotImplementedError
