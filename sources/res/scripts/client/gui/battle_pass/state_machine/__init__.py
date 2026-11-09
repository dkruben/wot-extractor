# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_pass/state_machine/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_pass/state_machine/__init__.py
from __future__ import absolute_import
from helpers import dependency
from skeletons.gui.impl import INotificationWindowController
_LOCK_SOURCE_NAME = 'BATTLE_PASS_REWARD_LOGIC'

@dependency.replace_none_kwargs(notificationManager=INotificationWindowController)
def lockNotificationManager(lock, notificationManager=None):
    isLocked = notificationManager.hasLock(_LOCK_SOURCE_NAME)
    if lock and not isLocked:
        notificationManager.lock(_LOCK_SOURCE_NAME)
    elif not lock and isLocked:
        notificationManager.unlock(_LOCK_SOURCE_NAME)
