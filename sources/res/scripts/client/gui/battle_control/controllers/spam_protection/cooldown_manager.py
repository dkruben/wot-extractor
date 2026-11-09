# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_control/controllers/spam_protection/cooldown_manager.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/spam_protection/cooldown_manager.py
from __future__ import absolute_import
import typing, BigWorld
from gui.battle_control.controllers.spam_protection.spam_constants import DEFAULT_COOLDOWN

class SpamCooldownManager(object):

    def __init__(self):
        self.__cooldowns = {}

    def destroy(self):
        self.__cooldowns.clear()

    def isInProcess(self, eventKey):
        if eventKey in self.__cooldowns:
            return self.__cooldowns[eventKey] > BigWorld.time()
        return False

    def process(self, eventKey, coolDown=None):
        coolDown = coolDown or DEFAULT_COOLDOWN
        self.__cooldowns[eventKey] = BigWorld.time() + coolDown
