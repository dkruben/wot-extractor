# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/skeletons/gui/battle_hints/newbie_battle_hints_controller.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/gui/battle_hints/newbie_battle_hints_controller.py
from __future__ import absolute_import
import typing

class INewbieBattleHintsController(object):

    def fini(self):
        raise NotImplementedError

    def isEnabled(self):
        raise NotImplementedError

    def isUserSettingEnabled(self):
        raise NotImplementedError

    def getDisplayCount(self, uniqueName):
        raise NotImplementedError

    def resetHistory(self):
        raise NotImplementedError
