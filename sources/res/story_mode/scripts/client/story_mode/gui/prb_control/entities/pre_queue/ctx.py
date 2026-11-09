# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/prb_control/entities/pre_queue/ctx.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/prb_control/entities/pre_queue/ctx.py
from __future__ import absolute_import
from constants import QUEUE_TYPE
from gui.prb_control.entities.base.pre_queue.ctx import QueueCtx
from gui.shared.utils.decorators import ReprInjector

@ReprInjector.withParent(('getVehicleInventoryID', 'vInvID'))
class StoryModeQueueCtx(QueueCtx):

    def __init__(self, waitingID=''):
        super(StoryModeQueueCtx, self).__init__(entityType=QUEUE_TYPE.STORY_MODE, waitingID=waitingID)
