# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/event_boards/event_boards_maintenance.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/event_boards/event_boards_maintenance.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.meta.MaintenanceComponentMeta import MaintenanceComponentMeta
import Event

class EventBoardsMaintenance(MaintenanceComponentMeta):

    def __init__(self):
        super(EventBoardsMaintenance, self).__init__()
        self.onRefresh = Event.Event()

    def refresh(self):
        self.onRefresh()
