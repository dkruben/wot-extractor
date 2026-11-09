# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/skeletons/gui/battle_hints/battle_hints_overlap_controller.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/gui/battle_hints/battle_hints_overlap_controller.py
from __future__ import absolute_import
import typing
if typing.TYPE_CHECKING:
    from gui.battle_control.controllers.battle_hints.queues import BattleHint

class IBattleHintsOverlapController(object):

    def fini(self):
        raise NotImplementedError

    def hintShown(self, battleHInt):
        raise NotImplementedError

    def hintHidden(self):
        raise NotImplementedError
