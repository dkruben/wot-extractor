# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/prb_control/entities/pre_queue/permissions.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/prb_control/entities/pre_queue/permissions.py
from __future__ import absolute_import
from gui.prb_control.entities.base.pre_queue.permissions import PreQueuePermissions
from helpers import dependency
from skeletons.gui.game_control import IComp7Controller

class Comp7Permissions(PreQueuePermissions):
    __comp7Controller = dependency.descriptor(IComp7Controller)

    def canCreateSquad(self):
        if self.__comp7Controller.isOffline or self.__comp7Controller.isBanned:
            return False
        if not self.__comp7Controller.hasPlayableVehicle():
            return False
        if not self.__comp7Controller.isQualificationSquadAllowed():
            return False
        return super(Comp7Permissions, self).canCreateSquad()
