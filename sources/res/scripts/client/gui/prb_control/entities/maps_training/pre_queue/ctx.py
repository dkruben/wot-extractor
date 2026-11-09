# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/prb_control/entities/maps_training/pre_queue/ctx.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/maps_training/pre_queue/ctx.py
from constants import QUEUE_TYPE
from gui.prb_control.entities.base.pre_queue.ctx import QueueCtx
from gui.shared.utils.decorators import ReprInjector

@ReprInjector.withParent(('getVehicleInventoryIDs', 'vInvIDs'))
class MapsTrainingQueueCtx(QueueCtx):

    def __init__(self, mapGeometryID, vehCompDescr, team, waitingID=''):
        super(MapsTrainingQueueCtx, self).__init__(entityType=QUEUE_TYPE.MAPS_TRAINING, waitingID=waitingID)
        self.__mapGeometryID = mapGeometryID
        self.__vehCompDescr = vehCompDescr
        self.__team = team

    def getSelectedMap(self):
        return self.__mapGeometryID

    def getSelectedVehicle(self):
        return self.__vehCompDescr

    def getSelectedTeam(self):
        return self.__team
