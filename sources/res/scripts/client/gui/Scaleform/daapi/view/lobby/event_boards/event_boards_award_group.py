# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/event_boards/event_boards_award_group.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/event_boards/event_boards_award_group.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.meta.AwardGroupsMeta import AwardGroupsMeta
import Event

class EventBoardsAwardGroup(AwardGroupsMeta):

    def __init__(self):
        super(EventBoardsAwardGroup, self).__init__()
        self.onShowRewardCategory = Event.Event()

    def showGroup(self, groupId):
        self.onShowRewardCategory(groupId)

    def setActiveRewardGroup(self, groupID):
        self.as_setSelectedS(groupID - 1, True)
