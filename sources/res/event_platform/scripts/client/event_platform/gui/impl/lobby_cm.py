# wot-extractor: codigo DESCOMPILADO de sources/res/event_platform/scripts/client/event_platform/gui/impl/lobby_cm.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: event_platform/scripts/client/event_platform/gui/impl/lobby_cm.py
from __future__ import absolute_import
from debug_utils import LOG_ERROR
from gui.Scaleform.daapi.view.lobby.hangar.hangar_cm_handlers import VehicleContextMenuHandler

class EPVehicleContextMenuHandler(VehicleContextMenuHandler):

    def __init__(self, cmProxy, ctx=None):
        LOG_ERROR('INIT -- EPVehicleContextMenuHandler')
        super(EPVehicleContextMenuHandler, self).__init__(cmProxy, ctx)
