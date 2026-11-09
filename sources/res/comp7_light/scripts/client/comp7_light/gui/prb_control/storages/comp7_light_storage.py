# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/prb_control/storages/comp7_light_storage.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/prb_control/storages/comp7_light_storage.py
from __future__ import absolute_import
from comp7_light_constants import ARENA_GUI_TYPE
from gui.prb_control.storages.local_storage import SessionStorage
from helpers import dependency
from skeletons.gui.game_control import IComp7LightController

class Comp7LightStorage(SessionStorage):
    _GUI_TYPE = ARENA_GUI_TYPE.COMP7_LIGHT
    __comp7LightController = dependency.descriptor(IComp7LightController)

    def isModeSelected(self):
        return self.__comp7LightController.isAvailable() and super(Comp7LightStorage, self).isModeSelected()

    def _determineSelection(self, arenaVisitor):
        return arenaVisitor.gui.guiType == self._GUI_TYPE
