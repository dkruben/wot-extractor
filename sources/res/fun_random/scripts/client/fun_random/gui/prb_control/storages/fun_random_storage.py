# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/prb_control/storages/fun_random_storage.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/prb_control/storages/fun_random_storage.py
from __future__ import absolute_import
from fun_random_common.fun_constants import UNKNOWN_EVENT_ID
from gui.prb_control.storages.local_storage import SessionStorage
from helpers import dependency
from skeletons.gui.game_control import IFunRandomController

class FunRandomStorage(SessionStorage):
    __funRandomController = dependency.descriptor(IFunRandomController)

    def isModeSelected(self):
        desiredSubMode = self.__funRandomController.subModesHolder.getDesiredSubMode()
        isSelected = desiredSubMode is not None and desiredSubMode.isAvailable()
        desiredSubModeID = desiredSubMode.getSubModeID() if isSelected else UNKNOWN_EVENT_ID
        self.__funRandomController.setDesiredSubModeID(desiredSubModeID)
        return isSelected
