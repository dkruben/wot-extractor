# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/prb_control/storages/comp7_storage.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/prb_control/storages/comp7_storage.py
from __future__ import absolute_import
from gui.prb_control.storages.local_storage import SessionStorage
from helpers import dependency
from skeletons.gui.game_control import IComp7Controller
from comp7_common.comp7_constants import ARENA_GUI_TYPE

class Comp7Storage(SessionStorage):
    _GUI_TYPE = ARENA_GUI_TYPE.COMP7
    __comp7Controller = dependency.descriptor(IComp7Controller)

    def isModeSelected(self):
        return self.__comp7Controller.isEnabled() and not self.__comp7Controller.isFrozen() and super(Comp7Storage, self).isModeSelected()

    def _determineSelection(self, arenaVisitor):
        return arenaVisitor.gui.guiType == self._GUI_TYPE
