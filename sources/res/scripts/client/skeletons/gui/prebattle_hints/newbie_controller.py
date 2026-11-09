# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/skeletons/gui/prebattle_hints/newbie_controller.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/gui/prebattle_hints/newbie_controller.py
from __future__ import absolute_import
from skeletons.gui.prebattle_hints.controller import IPrebattleHintsControlStrategy

class INewbiePrebattleHintsController(IPrebattleHintsControlStrategy):

    def fini(self):
        raise NotImplementedError

    def isEnabled(self):
        raise NotImplementedError

    def onConfirmationWindowShown(self):
        raise NotImplementedError
