# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/utils/requesters/quest_deltas_settings.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/utils/requesters/quest_deltas_settings.py
from __future__ import absolute_import
import typing
from future.utils import PY3, iteritems
from account_helpers import AccountSettings
from account_helpers.AccountSettings import QUEST_DELTAS, QUESTS
if PY3:
    from collections import UserDict as IterableUserDict
else:
    from UserDict import IterableUserDict
if typing.TYPE_CHECKING:
    from typing import Any, Hashable

class QuestDeltasSettings(IterableUserDict):

    def __init__(self, subKey=''):
        IterableUserDict.__init__(self)
        self._subKey = subKey
        savedSettings = AccountSettings.getSettings(QUESTS).get(QUEST_DELTAS, {}).get(self._subKey)
        if savedSettings is None:
            return
        else:
            for k, v in iteritems(savedSettings):
                self.data[k] = v

            return

    def __setitem__(self, key, item):
        IterableUserDict.__setitem__(self, key, item)
        self._saveToSettings()

    def __delitem__(self, key):
        IterableUserDict.__delitem__(self, key)
        self._saveToSettings()

    def _saveToSettings(self):
        questSettings = AccountSettings.getSettings(QUESTS)
        questSettings.get(QUEST_DELTAS, {})[self._subKey] = dict(self.data)
        AccountSettings.setSettings(QUESTS, questSettings)
