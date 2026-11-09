# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/skeletons/gui/prebattle_hints/controller.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/gui/prebattle_hints/controller.py
from __future__ import absolute_import
import typing
if typing.TYPE_CHECKING:
    from hints_common.prebattle.schemas import BaseHintModel

class IPrebattleHintsController(object):

    def fini(self):
        raise NotImplementedError

    def isEnabled(self):
        raise NotImplementedError

    def isEnabledForCurrentBattleSession(self):
        raise NotImplementedError

    def addControlStrategy(self, arenaBonusType, strategy):
        raise NotImplementedError

    def removeControlStrategy(self, arenaBonusType):
        raise NotImplementedError

    def onShowHintsWindowSuccess(self, hint):
        raise NotImplementedError


class IPrebattleHintsControlStrategy(object):

    def hasHintToShow(self, arenaBonusType):
        raise NotImplementedError

    def getHintToShow(self, arenaBonusType):
        raise NotImplementedError

    def onShowHintsWindowSuccess(self, hint):
        raise NotImplementedError
